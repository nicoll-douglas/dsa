from __future__ import annotations
from typing import Generic, TypeVar, TypeAlias, Callable
from .linked_list import LinkedList
from .array import Array

K = TypeVar("K")
V = TypeVar("V")

class HashMap(Generic[K, V]):
    """A class that implements a hash map with separate chaining and automatic resizing."""

    class Entry:
        """A class that implements an entry in the hash map."""

        key: K # The key of the entry
        value: V # The value of the entry

        def __init__(self, key: K, value: V):
            """Assign the given key and value to the entry."""
            self.key = key
            self.value = value
        # fed
    # ssalc

    _Bucket: TypeAlias = LinkedList[HashMap.Entry]
    _BucketArray: TypeAlias = Array[HashMap._Bucket]

    _INITIAL_BUCKETS: int = 16 # The initial number of buckets
    _MAX_LOAD: float = 0.7 # The maximum load factor

    _bucket_array: HashMap._BucketArray # The array of buckets that holds entries
    _size: int # The size of the hash map

    def __init__(self):
        """Initialise the bucket array with the initial number of buckets."""
        self._initialise_new_bucket_array()
    # fed

    def _initialise_new_bucket_array(self, length: int | None = None) -> None:
        """Create and assign a new bucket array with the given length or the initial number of buckets if none given."""
        bucket_array: HashMap._BucketArray = Array()

        for i in range(HashMap._INITIAL_BUCKETS if length is None else length):
            bucket_array.push(LinkedList())
        # rof

        self._bucket_array = bucket_array
        self._size = 0
    # fed
    
    def _get_bucket_index(self, key: K) -> int:
        """Get the index of the associated bucket for the given key via hashing."""
        return hash(key) % self._bucket_array.length()
    # fed

    def _get_bucket(self, key: K)  -> HashMap._Bucket:
        """Get a reference to the bucket associated with the given key."""
        return self._bucket_array.get(self._get_bucket_index(key))
    # fed
    
    def _calculate_load_factor(self) -> float:
        """Calculate the current load factor of the hash map."""
        return self._size / self._bucket_array.length()
    # fed

    def _load_factor_exceeded(self) -> bool:
        """Return a flag indicating whether the load factor of the hash map has been exceeded."""
        return self._calculate_load_factor() > HashMap._MAX_LOAD
    # fi

    def _resize(self) -> None:
        """Double the size of the bucket array and re-hash all keys.
        
        Time complexity is O(n) since for each entry we have to re-insert it into a newly created bucket array. Space complexity is O(n) since we clone the old bucket array before replacing it with a new one.
        """
        old_bucket_array: HashMap._BucketArray = self._bucket_array
        new_bucket_array_length: int = old_bucket_array.length() * 2

        self._initialise_new_bucket_array(new_bucket_array_length)
        
        for i in range(old_bucket_array.length()):
            bucket: HashMap._Bucket = old_bucket_array.get(i)

            bucket.for_each(lambda entry: self.set(entry.key, entry.value))
        # rof
    # fed
            
    def set(self, key: K, value: V) -> None:
        """Insert a key-value pair into the hash map and resize the hash map if the load factor has been exceeded.

        Time complexity in the best case is O(1) since when we insert we always insert at the end of the bucket (linked list) or if we are updating then the bucket is of length 1. In the average case, the average length of a chain in a bucket is equal to the number of elements divided by the number of buckets which is any number less than or equal to the load factor (0.7) so time taken to insert or update is proportional to the load factor giving us O(1). Worst case, all keys in the hash map hash to the same bucket and so if we update the second to last item in the bucket's chain, we have to traverse roughly n elements giving us O(n).
        """
        bucket: HashMap._Bucket = self._get_bucket(key)
        replaced: bool = False

        def _mapper(entry: HashMap.Entry) -> Entry:
            nonlocal replaced
            
            if entry.key == key:
                entry.value = value
                replaced = True
            # fi
            
            return entry
        # fed

        bucket.map(_mapper) # O(n) worst, O(1) best/average

        if replaced:
            return
        # fi

        bucket.append(self.Entry(key, value)) # O(1)

        self._size += 1

        if self._load_factor_exceeded():
            self._resize()
        # fi
    # fed

    def get(self, key: K, default_value: V | None = None) -> V | None:
        """Get a value associated with a key in the hash map or return the default if the key doesn't exist.

        Time complexity mirrors the time complexity of the `set` method so O(1) best/average case and O(n) worst case.
        """
        bucket: HashMap._Bucket = self._get_bucket(key)
        entry: HashMap.Entry | None = bucket.find(lambda entry: entry.key == key)
        
        return default_value if entry is None else entry.value
    # fed

    def delete(self, key: K) -> V | None:
        """Delete a key-value pair from the hash map based on the given key.

        Time complexity mirros the time complexity of the `set` method so O(1) best/average case and O(n) worst case.
        """
        bucket: HashMap._Bucket = self._get_bucket(key)
        deleted_val: V | None = None
        deleted: bool = False

        def _match(entry: HashMap.Entry):
            nonlocal deleted
            nonlocal deleted_val

            if entry.key == key:
                deleted_val = entry.value
                deleted = True

                return False
            # fi

            return True
        # fed

        bucket.filter(_match) # O(n) worst, O(1) best/average

        if deleted:
            self._size -= 1
        # fi

        return deleted_val
    # fed

    def contains(self, key: K) -> bool:
        return self.get(key) is not None
    # fed

    def for_each(self, callback: Callable[[K, V], None]) -> None:
        """Run a callback function for each entry in the hash map passing the key and value of the entry.

        Insertion order is not preserved so order of iteration may appear to be random.
        """
        for i in range(self._bucket_array.length()):
            bucket: HashMap._Bucket = self._bucket_array.get(i)

            bucket.for_each(lambda entry: callback(entry.key, entry.value))
        # rof
    # fed

    def size(self):
        """Get the number of key-value pairs in the hash map."""
        return self._size
    # fed
# ssalc


