from __future__ import annotations
from typing import TypeVar, Generic, List
from .array import Array

T = TypeVar("T")

class LinkedList(Generic[T]):
    """A class that implements a singlely linked list."""

    class LinkedListIndexError(IndexError):
        """Custom error class for linked list index out of bounds errors."""
        
        def __init__(self):
            """Instantiate the parent error class with a custom out of bounds message."""
            super.__init__("Linked list index out of bounds")
        # fed
    # ssalc

    class _Node:
        """A class that implements a node in the linked list."""

        value: T # The value of the node
        next: _Node | None # A pointer to the next node in the linked list

        def __init__(self, value: T, nxt: _Node | None = None):
            """Set the given value of the node and the node it points to in the linked list."""
            self.value = value
            self.next = nxt
        # fed
    # ssalc

    _length: int # The length of the linked list
    _head: LinkedList._Node | None # A pointer to the head of the linked list
    _tail: LinkedList._Node | None # A pointer to the tail of the linked list

    def __init__(self, values: Array[T] | None = None):
        """Initialises the linked list with the given elements if any and sets the length."""
        if values:
            self._length = values.length
            self._head = self._Node(values.get(0))
            
            current: LinkedList._Node = self._head

            for i in range(1, values.length):
                current.next = self._Node(values.get(i))

                current = current.next
            # rof

            self._tail = current
        else:
            self._head = None
            self._tail = None
            self._length = 0
        # fi
    # fed

    def _validate_less_than_eq_to_n(self, value: int) -> None:
        """Do nothing if the given value is between 0 and the linked list length inclusive or raise a LinkedListIndexError."""
        if value < 0 or value > self._length:
            raise self.inkedListIndexError
        # fi
    # fed

    def _validate_index(self, index: int) -> None:
        """Do nothing if the given index is within valid bounds for the linked list or raise a LinkedListIndexError."""
        if index == self._length:
            raise self.LinkedListIndexError
        # fi

        self._validate_less_than_eq_to_n(index)
    # fed
  
    def _traverse(self, index: int) -> LinkedList._Node:
        """Traverse the linked list to the given index and return the node.
        
        Time complexity is O(n) in the worst case where the given index is n-2 meaning we have to traverse roughly n times to get the node before the tail. Time complexity is O(n) in the average case where the given index is roughly in the middle meaning we have to traverse around n/2 times so overall O(n) complexity dropping the constant. And in the best case, time complexity is O(1) where the given index is 0 or the last index. These are the head and tail of the linked list respectively which we already have references to so no traversals would be required.
        """
        self._validate_index(index)

        if index == 0:
            return self._head
        # fi

        if index == self._length - 1:
            return self._tail
        # fi

        current: LinkedList._Node = self._head

        for i in range(index):
            current = current.next
        # rof

        return current
    # fed
    
    def insert(self, index: int, value: T) -> None:
        """Insert an item into the linked list at the given index or raise a LinkedListIndexError if out of bounds.
        
        Time complexity mirrors the time complexity of the `_traverse` method so worst and average case O(n) and best case O(1).
        """
        self._validate_less_than_eq_to_n(index)

        if index == 0:
            new_node: LinkedList._Node = self._Node(value, self._head)
            self._head = new_node

            if self._length == 0:
                self._tail = self._head
            # fi
        else:
            node_behind: LinkedList._Node = self._traverse(index - 1)
            new_node: LinkedList._Node = self._Node(value, node_behind.next)

            node_behind.next = new_node

            if index == self._length:
                self._tail = self._tail.next
            # fi
        # fi

        self._length += 1
    # fed
    
    def append(self, value: T) -> None:
        """Append an item at the end of the linked list.

        Time complexity is the worst case time complexity of the `insert` method so O(n).
        """
        self.insert(self._length, value)
    # fed

    def prepend(self, value: T) -> None:
        """Prepend an item at the beginning of the linked list.

        Time complexity is the best case time complexity of the `insert` method so O(1).
        """
        self.insert(0, value)
    # fed

    def delete(self, index: int) -> T:
        """Delete an item from the linked list at the given index and return its value or raise a LinkedListIndexError if out of bounds.
        
        Time complexity mirrors the time complexity of the `_traverse` method so worst and average case O(n) and best case O(1).
        """
        self._validate_index(index)

        if index == 0:
            value: T = self._head.value
            self._head = self._head.next

            if self._length == 1:
                self._tail = None
            # fi
        else:
            node_behind: LinkedList._Node = self._traverse(index - 1)
            node: LinkedList._Node = node_behind.next
            value: T = node.value
            node_behind.next = node.next

            if index == self._length - 1:
                self._tail = node_behind
            # fi
        # fi

        self._length -= 1

        return value
    # fed

    def delete_first(self) -> T:
        """Delete the head of the linked list and return its value or raise a LinkedListIndexError if the linked list is empty.
        
        Time complexity is the best case time complexity of the `delete` method so O(1).
        """
        return self.delete(0)
    # fed

    def delete_last(self) -> T:
        """Delete the tail of the linked list and return its value or raise a LinkedListIndexError if the linked list is empty.
        
        Time complexity is the worst case time complexity of the `delete` method so O(1).
        """
        return self.delete(self._length - 1)
    # fed

    def get(self, index: int) -> T:
        """Get an item from the linked list at the specified index or raise a LinkedListIndexError if out of bounds.
    
        Time complexity mirrors the time complexity of the `_traverse` method so worst and average case O(n) and best case O(1).
        """
        return self._traverse(index).value
    # fed

    def head(self) -> T:
        """Get the value at the head of the linked list or raise a LinkedListIndexError if the linked list is empty.
        
        Time complexity is O(1) given that we have a reference to the head of the linked list.
        """
        return self.get(0)
    # fed

    def tail(self) -> T:
        """Get the value at the tail of the linked list or raise a LinkedListIndexError if the linked list is empty.

        Time complexity is O(1) given that we have a reference to the tail of the linked list.
        """
        return self.get(self._length - 1)
    # fed

    def set(self, index: int, value: T) -> None:
        """Set the value of a node in the linked list at the specified index or throw an LinkedListIndexError if out of bounds.
        
        Time complexity mirrors the time complexity of the `_traverse` method so worst and average case O(n) and best case O(1).
        """
        self._traverse(index).value = value
    # fed

    def search(self, value: T) -> int:
        """Linearly search for an item in the linked list and return the index of the first occurence or -1 if it is not in the linked list.
        
        Time complexity mirrors the time complexity of the `_traverse` method so worst and average case O(n) and best case O(1) with the item being at the head.
        """
        current: LinkedList._Node | None = self._head

        for i in range(self._length):
            if value == current.value:
                return i
            # fi

            current = current.next
        # rof

        return -1
    # fed

    def length(self) -> int:
        """Get the length of the linked list."""
        return self._length
    # fed
# ssalc
