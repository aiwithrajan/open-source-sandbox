from typing import Generic, TypeVar, List, Optional
from collections import deque

T = TypeVar("T")

class Stack(Generic[T]):
    """LIFO Stack data structure."""
    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> Optional[T]:
        return self._items.pop() if self._items else None

    def peek(self) -> Optional[T]:
        return self._items[-1] if self._items else None

    def is_empty(self) -> bool:
        return len(self._items) == 0

class Queue(Generic[T]):
    """FIFO Queue data structure."""
    def __init__(self) -> None:
        self._items: deque[T] = deque()

    def enqueue(self, item: T) -> None:
        self._items.append(item)

    def dequeue(self) -> Optional[T]:
        return self._items.popleft() if self._items else None

    def is_empty(self) -> bool:
        return len(self._items) == 0
