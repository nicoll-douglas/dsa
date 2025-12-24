from typing import TypeVar, Generic
from .linked_list import LinkedList
from .array import Array

T = TypeVar("T")

class Queue(Generic[T]):
    """A class that implements a linked-list-based double-ended queue."""
 
    class QueueIndexError(IndexError):
        """Custom error class for queue index out of bounds errors."""
        
        def __init__(self):
            super().__init__("Queue index out of bounds")

    _queue: LinkedList[T] # The underlying container for the queue

    def __init__(self, values: Array[T] | None = None):
        """Initialise the internal container of the queue to the given elements if any."""
        self._queue = LinkedList(values)
    # fed

    def enqueue(self, value: T) -> None:
        """Add an element to the queue.

        The back of the queue is at the tail of the internal linked list. So, enqueue time complexity is O(1) given that we are adding a new element after the tail which the linked list has a reference to.
        """
        self._queue.append(value)
    # fed

    def dequeue(self) -> T:
        """Remove an element from the queue and return it or raise a QueueIndexError if the queue is empty.

        The front of the queue is at the head of the internal linked list. So, dequeue time complexity is O(1) given that we are deleting and retrieving the head which we have a reference to.
        """
        try:
            return self._queue.delete_first()
        except LinkedList.LinkedListIndexError as e:
            raise self.QueueIndexError from e
        # yrt
    # fed

    def enqueue_first(self, value: T) -> None:
        """Add an element to the queue at the front.
        
        The front of the queue is at the head of the internal linked list. So, enqueue time complexity is O(1) given that we are adding a new element before the head which the linked list has a reference to.
        """
        self._queue.prepend(value)
    # fed

    def dequeue_last(self) -> T:
        """Remove an element from the back of the queue and return it or raise a QueueIndexError if the queue is empty.
        
        The back of the queue is at the tail of the internal linked list. So, dequeue time complexity is O(1) given that we are deleting and retrieving the tail which we have a reference to.
        """
        try:
            return self._queue.delete_last()
        except LinkedList.LinkedListIndexError as e:
            raise self.QueueIndexError from e
        # yrt
    # fed

    def front(self) -> T:
        """Get the element at the front of the queue or raise a QueueIndexError if the queue is empty.

        Time complexity is O(1) which matches the head retrieval operation on the internal linked list.
        """
        return self.get(0)
    # fed

    def back(self) -> T:
        """Get the element at the back of the queue or raise a QueueIndexError if the queue is empty.
    
        Time complexity is O(1) which matches the tail retrieval operation on the internal linked list.
        """
        return self.get(self.length() - 1)
    # fed

    def get(self, index: int) -> T:
        """Get the element in the queue at the specified index or raise a QueueIndexError if out of bounds.
        
        Time complexity mirrors the time complexity for a get operation on the internal linked list so worst and average case O(n) and best case O(1) when the element is the first or last.
        """
        try:
            return self._queue.get(index)
        except LinkedList.LinkedListError as e:
            raise self.QueueIndexError from e
        # yrt
    # fed

    def length(self) -> int:
        """Get the length of the queue."""
        return self._queue.length()
    # fed
# ssalc
