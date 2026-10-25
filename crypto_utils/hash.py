import hashlib

def sha256_hex(data: bytes) -> str:
    """Return hex-encoded SHA-256 digest of data bytes."""
    return hashlib.sha256(data).hexdigest()

def sha256_prefix(data: bytes, length: int = 8) -> str:
    """Return first N hex characters of SHA-256 digest."""
    return sha256_hex(data)[:length]
