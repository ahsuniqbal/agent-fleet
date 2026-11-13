#!/usr/bin/env python3
"""Build the Agensi pack ZIP from this repo.

Agensi sells SKILL.md skills, not Claude Code plugins: subagents and slash commands are not
installed on the buyer's machine. This script adapts a copy of the plugin into a pack:

- every skill gets a "Role" note telling the agent to read agents/<role>.md
- the three slash commands become orchestrator skills (agent-fleet-*)
- agents/, templates/, CONVENTIONS.md ship as shared files at the pack root

The repo itself is never modified. Output: dist/agent-fleet-agensi-v<version>.zip

Usage: python3 scripts/build-agensi.py
"""

import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACK = "agent-fleet"

# Agensi limits (from the founder, Nov 2026).
MAX_SKILLS = 50
MAX_FILES = 1000
MAX_BYTES = 50 * 1024 * 1024
BLOCKED_PATTERNS = [
    r"rm\s+-rf\s+/(\s|$)",
    r"chmod\s+777",
    r"(curl|wget)[^\n|]*\|\s*(ba|z)?sh",
]

COMMANDS = {
    "foundation": {
        "name": "agent-fleet-foundation",
        "input": "the client brief, transcript, or notes the user provided",
    },
    "module": {
        "name": "agent-fleet-module",
        "input": "the module the user named (by name or number), or blank",
    },
    "close": {
        "name": "agent-fleet-close",
        "input": "the module the user named (by name or number), or blank",
    },
}

ROLE_NOTE = (
    "> **Role:** before starting, read {files} and work as {that}. If your tool can launch "
    "subagents, launch {one} with {it} as {its} instructions instead."
)

ORCHESTRATOR_NOTE = (
    "> **Roles:** each stage below names a role defined in `agents/<role>.md`. If your tool can "
    "launch subagents, launch one per stage with that file as its instructions, and launch the "
    "M.6 branches concurrently. Otherwise read the file and work as that role for the stage.\n"
)


def fail(msg):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(1)


def known_roles():
    return {p.stem for p in (ROOT / "agents").glob("*.md")}


def role_note(header_line, roles):
    found = [r for r in re.findall(r"[a-z]+(?:-[a-z]+)+|[a-z]+", header_line.split("Agent", 1)[1])
             if r in roles]
    if not found:
        fail(f"no known role in header: {header_line!r}")
    files = ", ".join(f"`agents/{r}.md`" for r in found)
    many = len(found) > 1
    return ROLE_NOTE.format(
        files=files,
        that="the role that fits your part of the work" if many else "that role",
        one="the one you need" if many else "one",
        it="that file" if many else "the file",
        its="its",
    )


def adapt_skill(text, roles):
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if line.startswith("**Stage:**") and "Agent" in line:
            j = i + 1
            while j < len(lines) and lines[j].strip():
                j += 1
            lines[j:j] = ["", role_note(line, roles)]
            return "\n".join(lines)
    fail("skill has no **Stage:** · **Agent:** line")


def adapt_command(stem, text):
    meta = COMMANDS[stem]
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        fail(f"commands/{stem}.md has no frontmatter")
    desc = re.search(r"^description:\s*(.+)$", m.group(1), re.M)
    if not desc:
        fail(f"commands/{stem}.md has no description")
    body = text[m.end():]
    body = body.replace("$ARGUMENTS", meta["input"])
    for other, om in COMMANDS.items():
        body = re.sub(rf"`/{other}`", f"the `{om['name']}` skill", body)
    body = body.replace("Run /close", "Run the `agent-fleet-close` skill")
    body = re.sub(r"Use the `([a-z-]+)` agent", r"Work as the `\1` role (`agents/\1.md`)", body)
    head = f"---\nname: {meta['name']}\ndescription: {desc.group(1).strip()}\n---\n"
    return head + "\n" + ORCHESTRATOR_NOTE + body


def adapt_shared(text):
    return text.replace("plugin root", "pack root")


def frontmatter_ok(text, folder):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return "missing frontmatter"
    name = re.search(r"^name:\s*(\S+)", m.group(1), re.M)
    desc = re.search(r"^description:\s*\S", m.group(1), re.M)
    if not name or not desc:
        return "missing name or description"
    if name.group(1) != folder:
        return f"name {name.group(1)!r} does not match folder {folder!r}"
    return None


def build():
    roles = known_roles()
    files = {}  # zip path -> text

    for path in sorted((ROOT / "skills").glob("*/SKILL.md")):
        folder = path.parent.name
        files[f"{PACK}/skills/{folder}/SKILL.md"] = adapt_shared(adapt_skill(path.read_text(), roles))
        for extra in sorted(path.parent.rglob("*")):
            if extra.is_file() and extra.name != "SKILL.md":
                rel = extra.relative_to(ROOT / "skills")
                files[f"{PACK}/skills/{rel}"] = extra.read_text()

    for stem in COMMANDS:
        text = (ROOT / "commands" / f"{stem}.md").read_text()
        files[f"{PACK}/skills/{COMMANDS[stem]['name']}/SKILL.md"] = adapt_shared(adapt_command(stem, text))

    for sub in ("agents", "templates"):
        for path in sorted((ROOT / sub).glob("*.md")):
            files[f"{PACK}/{sub}/{path.name}"] = adapt_shared(path.read_text())

    files[f"{PACK}/CONVENTIONS.md"] = adapt_shared((ROOT / "CONVENTIONS.md").read_text())
    files[f"{PACK}/README.md"] = (ROOT / "packaging/agensi/README.md").read_text()
    return files


def validate(files):
    errors = []
    skills = [p for p in files if p.endswith("/SKILL.md")]
    for p in skills:
        err = frontmatter_ok(files[p], p.split("/")[-2])
        if err:
            errors.append(f"{p}: {err}")
    for p, text in files.items():
        for pat in BLOCKED_PATTERNS:
            if re.search(pat, text):
                errors.append(f"{p}: matches blocked pattern {pat!r}")
        if re.search(r"(?<![\w`])/(foundation|module|close)\b(?!/)", text) and "/skills/" in p:
            errors.append(f"{p}: still references a slash command")
    size = sum(len(t.encode()) for t in files.values())
    if not 2 <= len(skills) <= MAX_SKILLS:
        errors.append(f"{len(skills)} skills; a pack needs 2..{MAX_SKILLS}")
    if len(files) > MAX_FILES:
        errors.append(f"{len(files)} files; limit {MAX_FILES}")
    if size > MAX_BYTES:
        errors.append(f"{size} bytes; limit {MAX_BYTES}")
    if errors:
        fail("validation failed:\n  " + "\n  ".join(errors))
    return len(skills), size


def main():
    version = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())["version"]
    files = build()
    n_skills, size = validate(files)

    out = ROOT / "dist" / f"agent-fleet-agensi-v{version}.zip"
    out.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(files):
            info = zipfile.ZipInfo(path, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, files[path])

    print(f"wrote {out.relative_to(ROOT)}")
    print(f"  {n_skills} skills, {len(files)} files, {size / 1024:.0f} KB uncompressed, "
          f"{out.stat().st_size / 1024:.0f} KB zipped")


if __name__ == "__main__":
    main()
