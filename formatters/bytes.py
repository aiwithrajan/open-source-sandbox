def format_byte_size(bytes_count: int, precision: int = 2) -> str:
    """Format bytes count into human-readable string (KB, MB, GB, etc.)."""
    if bytes_count < 0:
        raise ValueError("bytes_count must be non-negative")
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    value = float(bytes_count)
    for unit in units:
        if value < 1024.0 or unit == units[-1]:
            return f"{value:.{precision}f} {unit}" if unit != "B" else f"{int(value)} B"
        value /= 1024.0
    return f"{value:.{precision}f} PB"
