from typing import TypeVar, Generic
from .array import Array

T = TypeVar("T")

class Stack(Generic[T]):
    """A class that implements a stack with automatic resizing and a dynamic array."""

    class StackIndexError(IndexError):
        """Custom error class for stack index errors."""

        def __init__(self):
            """Instantiates the parent class with a custom out of bounds error message"""
            super.__init__("Stack index out of bounds")
        # fed
    # ssalc

    _stack: Array[T] # The underlying container for the stack

    def __init__(self, elements: Array[T] | None = None):
        """Put the given elements into the stack if any or initialise an empty stack."""
        self._stack = elements if elements else Array()
    # fed

    def _top(self) -> int:
        """Get the index of the element at the top of the stack."""
        return self._stack.length() - 1
    # fed

    def push(self, value: T) -> None:
        """Push an item onto the top of the stack.
        
        Time complexity mirrors the time complexity for a push operation on the internal array so O(1).
        """
        self._stack.push(value)
    # fed

    def pop(self) -> T:
        """Remove and return the item at the top of the stack or raise a StackIndexError if the stack is empty.
        
        Time complexity mirrors the time complexity for a pop operation on the internal array so O(1).
        """
        try:
            return self._stack.pop()
        except Array.ArrayIndexError as e:
            raise self.StackIndexError from e
        # yrt
    # fed

    def peek(self) -> T:
        """Return the item at the top of the stack or raise a StackIndexError if the stack is empty.
        
        Time complexity mirrors the time complexity of the `get` method so O(1).
        """
        return self.get(self._top())
    # fed

    def get(self, index: int) -> T:
        """Get the item in the stack at the given index or raise a StackIndexError if out of bounds.

        Time complexity mirrors the time complexity for a get operation on the internal array so O(1).
        """
        try:
            return self._stack.get(index)
        except Array.ArrayIndexError as e:
            raise self.StackIndexError from e
        # yrt
    # fed

    def size(self) -> int:
        """Get the size of the stack."""
        return self._stack.length()
    # fed
# ssalc
