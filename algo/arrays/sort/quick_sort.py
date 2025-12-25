from ds import Array
from typing import TypeVar

T = TypeVar("T")

def quick_sort(arr: Array[T]) -> None:
    """Sort an array using the quick sort algorithm."""
    def _quick_sort_rec(arr: Array[T], low: int, high: int) -> None:
        """Sorts a portion of an array within the given high and low bounds using the Hoare partition scheme.
        
        Arguments
        ---------
        arr
            The base array that is being sorted.

        low
            The lower boundary/index of the portion that will be sorted.

        high
            The higher boundary/index of the portion that will be sorted.
        """
        if low >= high:
            return
        # fi

        pivot: int = arr.get(low)
        i: int = low - 1
        j: int = high + 1

        while True:
            i += 1

            while arr.get(i) < pivot:
                i += 1
            # elihw

            j -= 1

            while arr.get(j) > pivot:
                j -= 1
            # elihw

            if i >= j:
                break
            # fi

            temp: T = arr.get(i)
            arr.set(i, arr.get(j))
            arr.set(j, temp)
        # elihw

        _quick_sort_rec(arr, low, j)
        _quick_sort_rec(arr, j + 1, high)
    # fed

    _quick_sort_rec(arr, 0, arr.length() - 1)
# fed

