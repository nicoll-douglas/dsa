from ds import Array
from typing import TypeVar

T = TypeVar("T")

def binary_search(arr: Array[T], target: T) -> int:
    """Perform a binary search on a sorted array for a given target and return its index or -1 if not in the array.
    
    In the worst case, time complexity will be O(log(n)) as the array will be partitioned at most log(n) times. In the average case, the array will be partitioned some fraction of log(n) so dropping this fraction gives us O(log(n)) overall. And in the best case, time complexity will be O(1) as the target will be the first middle element selected on which we are partitioning.
    """
    low: int = 0
    high: int = arr.length() - 1

    while low <= high:
        mid: int = int(low + ((high - low) / 2))
        mid_value: T = arr.get(mid)

        if target < mid_value:
            high = mid - 1
        elif target > mid_value:
            low = mid + 1
        else:
            return mid
        # fi
    # elihw

    return -1
# fed
