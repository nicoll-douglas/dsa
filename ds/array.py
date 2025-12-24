from typing import Generic, List, TypeVar

T = TypeVar("T")

class Array(Generic[T]):
    """A class that implements an array with automatic resizing."""

    _array: List[T] # The underlying container for the array
    length: int # The length of the array

    def __init__(self, elements: List[T] = []):
        """Initialise the internal container with the given elements and sets the initial length of the array."""
        self._array = elements
        self.length = len(elements)
    # fed

    def _validate_less_than_eq_to_n(self, value: int) -> None:
        """Do nothing if the given value is between 0 and the array length inclusive or raise an IndexError."""
        if value < 0 or value > self.length:
            raise IndexError
        # fi
    # fed

    def _validate_index(self, index: int) -> None:
        """Do nothing if the given in index is within valid bounds for the array or raise an IndexError."""
        if index == self.length:
            raise IndexError
        # fi

        self._validate_less_than_eq_to_n(index)
    # fed

    def get(self, index: int) -> T:
        """Get an element from the array at the specified index and return it or raise an IndexError if out of bounds.

        Time complexity is O(1) since array memory is contiguous. So, the memory address is computed instantly using the base array address and index.
        """
        self._validate_index(index)
            
        return self._array[index]
    # fed

    def set(self, index: int, value: T) -> None:
        """Set an element in the array with the specified value at the specified index or raise an IndexError if index is out of bounds."""
        self._validate_index(index)

        self._array[index] = value
    # fed

    def search(self, target: T) -> int:
        """Search the array for a target linearly and return the index of the first occurence or -1 if not in the array.

        Time complexity is O(n) in the worst case as the target would be at the end of the array and you have to traverse n elements to find it. Time complexity is O(n) in the average case as you have to traverse about n/2 elements to find it so dropping the constant would give us O(n) overall. And in the best case, time complexity is O(1) since we only have to traverse 1 element to find the target.
        """
        for i in range(self.length):
            if self._array[i] == target:
                return i
            # fi
        # rof

        return -1
    # fed

    def delete(self, index: int) -> T:
        """Delete an element from the array, resize it, and return the deleted element or raise an IndexError if index is out of bounds.

        Time complexity is O(n) in the worst case as the target deletion index would be 0, so we would have to shift down n-1 elements. In the average case the deletion index would be around the middle so we would have to shift about n/2 elements so O(n) overall dropping the constant. And in the best case, O(1) as we would delete the last element so no elements would have to be shifted.
        """
        self._validate_index(index)

        deleted: T = self._array[index]

        for i in range(index, self.length - 1):
            self.set(i, self.get(i + 1))
        # rof

        del self._array[self.length - 1]

        self.length -= 1
        
        return deleted
    # fed

    def insert(self, index: int, value: T) -> None:
        """Insert the given element into the array at the given index, automatically resizing the array or raise an IndexError if the index is out of bounds.

        Time complexity is O(n) in the worst case as the target insertion index would be 0, so we would have to shift up n-1 elements. In the average case the insertion index would be around the middle so we would have to shift about n/2 elements so O(n) overall dropping the constant. And in the best case, O(1) as we would insert the last element so no elements would have to be shifted.
        """
        self._validate_less_than_eq_to_n(index)
        self._array += [None]
        self.length += 1

        for i in range(index, self.length - 2):
            self.set(i + 1, this.get(i))
        # rof

        self.set(index, value)
    # fed

    def unshift(self, value: T) -> None:
        """Insert an array element at the beginning of the array.

        Time complexity is O(n) since it is the worst case for the `insert` method.
        """
        self.insert(0, value)
    # fed

    def push(self, value: T) -> None:
        """Insert an array element at the end of the array.
        
        Time complexity is O(1) since it is the best case for the `insert` method.
        """
        self.insert(this.length, value)
    # fed

    def shift(self) -> T:
        """Delete the first element from the array and return it.
        
        Time complexity is O(n) since it is the worse case for the `delete` method.
        """
        return self.delete(0)
    # fed

    def pop(self) -> T:
        """Delete the last element from the array and return it.

        Time complexity is O(1) since it is the best case for `delete` method.
        """
        return self.delete(this.size - 1)
    # fed
 # ssalc
