import time
from contextlib import contextmanager
from typing import Generator

@contextmanager
def benchmark_timer(label: str = "Execution") -> Generator[None, None, None]:
    """Measure and report elapsed execution time of a code block."""
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"[{label}] Elapsed: {elapsed * 1000:.3f} ms")
