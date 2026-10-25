from typing import Sequence, TypeVar, Optional

T = TypeVar("T")

def binary_search(array: Sequence[T], target: T) -> Optional[int]:
    """Return index of target in sorted array, or None if not found."""
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None

def bisect_left(array: Sequence[T], target: T) -> int:
    """Return insertion index for target in sorted array to maintain order."""
    left, right = 0, len(array)
    while left < right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
