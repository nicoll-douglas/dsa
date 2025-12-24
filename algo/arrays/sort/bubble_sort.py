from ds import Array
from typing import TypeVar

T = TypeVar("T")

def bubble_sort(arr: Array[T]) -> None:
    """Sort a given array using the bubble sort algorithm.
    
    The time complexity in the worst case is O(n^2) since every element must bubble through all others leading to maximum comparisons and swaps. In the average case, time complexity is O(n^2) since the number of swaps and comparisons will be some fraction of O(n^2) leading to O(n^2) complexity overall dropping the constant. Time complexity in the best case is O(n) as we would only do one pass of the inner loop to see that no swaps occurred meaning that we would break out (the array was already sorted). Space complexity is O(1) since it's iterative and swapping occurs in place.
    """

    # loop enough times that on the final iteration, only 2 items are left to compare at the end
    for i in range(arr.length() - 1):
        swapped: bool = False

        # loop over the unsorted items (at the end we get [x, y] which are the first two elements that we are comparing)
        for j in range(arr.length() - i - 1):
            current: T = arr.get(j)
            nxt: T = arr.get(j + 1)

            # if the current is bigger that the next, swap it upwards
            if current > nxt:
                arr.set(j, nxt)
                arr.set(j + 1, current)

                swapped = True
            # fi
        # rof
    
        # if no swaps occurred the array is sorted so exit
        if not swapped:
            break
        # fi
    # rof
# fed

