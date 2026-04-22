# enterprise-deep-debug

Standalone home for the OpenCode `enterprise-deep-debug` skill.

## What this repository contains
- `SKILL.md` — canonical skill definition
- `scripts/` — log capture, trace, coverage, and analysis tooling

## Current use
- Facts-first root cause analysis
- Parallel subagent orchestration
- Web validation and runtime correlation
- Minimal safe fix with persistent learning

## Install
```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/enterprise-deep-debug
git clone https://github.com/SIN-Skills/enterprise-deep-debug ~/.config/opencode/skills/enterprise-deep-debug
```

## Goal
Debug like an enterprise control plane, not a guesser.
