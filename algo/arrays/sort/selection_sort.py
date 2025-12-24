from typing import TypeVar
from ds import Array

T = TypeVar("T")

def selection_sort(arr: Array[T]) -> None:
    """Sort an array using the selection sort algorithm.

    Time complexity in the worst case is O(n^2) where the arrays are in reverse order meaning every loop executes to completion. In the best case, time complexity is also O(n^2) since the outer loop executes to completion and the inner loop performs up to n iterations. In the best case, the array is sorted but complexity is also O(n^2) since we still have to do both loops and perform a full sweep to check that the array is sorted. Space complexity is O(1) since the implementation is iterative and sorting occurs in place.
    """
    # loop over all elements minus the last so there is at least one remaining element
    for i in range(arr.length() - 1):
        # the current known minimum is i
        minimum: int = i

        # loop over the remaining elements
        for j in range(i + 1, arr.length()):
            # if the current element is less than the known minimum we have a new minimum
            if arr.get(j) < arr.get(minimum):
                minimum = j
            # fi
        # rof

        # swap the current element with the minimum
        temp: T = arr.get(minimum)
        arr.set(minimum, arr.get(i))
        arr.set(i, temp)
    # rof
# fed

