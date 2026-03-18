#!/usr/bin/env python3
"""
Stub redirect to actual tc-stop-hook in AIOS.
This exists because an older session-coordinator configuration was installed
with a relative path. The actual hook is in /workspace/AIOS/.
"""
import subprocess
import sys

actual_hook = "/workspace/AIOS/.claude/skills/session-coordinator/hooks/tc-stop-hook.py"
result = subprocess.run([sys.executable, actual_hook], stdin=sys.stdin, capture_output=True, text=True)
sys.stdout.write(result.stdout)
sys.stderr.write(result.stderr)
sys.exit(result.returncode)
