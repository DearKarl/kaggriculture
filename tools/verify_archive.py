"""Verify the preserved artifact without executing the competition agent."""
from pathlib import Path
import hashlib
import json
import tarfile

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "docs/provenance.json").read_text())
for name, expected in manifest["files"].items():
    content = (root / name).read_bytes()
    assert len(content) == expected["bytes"], f"Size mismatch: {name}"
    assert hashlib.sha256(content).hexdigest() == expected["sha256"], f"Hash mismatch: {name}"
with tarfile.open(root / "submission/submission.tar.gz", "r:gz") as archive:
    assert archive.getnames() == ["main.py"], "Unexpected archive members"
    source = archive.extractfile("main.py").read()
assert source == (root / "src/main.py").read_bytes(), "Source differs from submission"
compile(source, "main.py", "exec")
print("PASS: SHA-256, archive members, source byte identity, and Python syntax.")
print("Agent execution and historical evaluation results were not tested.")
