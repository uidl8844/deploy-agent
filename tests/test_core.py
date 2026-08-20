from pathlib import Path
from deploy_agent import ReleaseLog, file_sha256

def test_rollback():
    log = ReleaseLog()
    log.record("1.0.0", "aaaaaaaa")
    log.record("1.1.0", "bbbbbbbb")
    assert log.current().version == "1.1.0"
    assert log.rollback_target().version == "1.0.0"

def test_file_hash(tmp_path: Path):
    p = tmp_path / "a.bin"
    p.write_bytes(b"hello")
    assert file_sha256(p) == file_sha256(p)
