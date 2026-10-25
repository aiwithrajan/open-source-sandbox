from typing import List, TypeVar, Generator, Iterable

T = TypeVar("T")

def chunk(items: List[T], size: int) -> Generator[List[T], None, None]:
    """Yield successive chunks of length size from items list."""
    if size <= 0:
        raise ValueError("size must be greater than 0")
    for i in range(0, len(items), size):
        yield items[i : i + size]

def flatten(nested: Iterable[Iterable[T]]) -> List[T]:
    """Flatten an iterable of iterables into a single list."""
    return [item for sublist in nested for item in sublist]
