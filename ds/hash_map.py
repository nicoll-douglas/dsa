from __future__ import annotations
from typing import Generic, TypeVar, TypeAlias, Callable
from .linked_list import LinkedList
from .array import Array

K = TypeVar("K")
V = TypeVar("V")

class HashMap(Generic[K, V]):
    class Entry:
        key: K
        value: V

        def __init__(self, key: K, value: V):
            self.key = key
            self.value = value
        # fed
    # ssalc

    _Bucket: TypeAlias = LinkedList[Entry]
    _BucketArray: TypeAlias = Array[_Bucket]

    _INITIAL_BUCKETS: int = 16
    _MAX_LOAD: float = 0.7

    _bucket_array: _BucketArray
    _size: int

    def __init__(self):
        self._initialise_new_bucket_array()
    # fed

    def _initialise_new_bucket_array(self, length: int | None = None) -> None:
        bucket_array: _BucketArray = Array()

        for i in range(HashMap._INITIAL_BUCKETS if length is None else length):
            bucket_array.push(LinkedList())
        # rof

        self._bucket_array = bucket_array
        self._size = 0
    # fed
    
    def _get_bucket_index(self, key: K) -> int:
        return hash(key) % self._bucket_array.length()
    # fed

    def _get_bucket(self, key: K) -> _Bucket:
        return self._bucket_array.get(self._get_bucket_index(key))
    # fed
    
    def _calculate_load_factor(self) -> float:
        return self._size / self._bucket_array.length()
    # fed

    def _load_factor_exceeded(self) -> bool:
        return self._calculate_load_factor() > HashMap._MAX_LOAD
    # fi

    def _resize(self) -> None:
        old_bucket_array: _BucketArray = self._bucket_array
        new_bucket_array_length: int = old_bucket_array.length() * 2

        self._initialise_new_bucket_array(new_bucket_array_length)
        
        for i in range(old_bucket_array.length()):
            bucket: _Bucket = old_bucket_array.get(i)

            bucket.for_each(lambda entry: self.set(entry.key, entry.value))
        # rof
    # fed
            
    def set(self, key: K, value: V) -> None:
        bucket: _Bucket = self._get_bucket(key)
        replaced: bool = False

        def _mapper(entry: Entry) -> Entry:
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
        bucket: _Bucket = self._get_bucket(key)
        entry: Entry | None = bucket.find(lambda entry: entry.key == key)
        
        return default_value if entry is None else entry.value
    # fed

    def delete(self, key: K) -> V | None:
        bucket: _Bucket = self._get_bucket(key)
        deleted_val: V | None = None
        deleted: bool = False

        def _match(entry: Entry):
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
        for i in range(self._bucket_array.length()):
            bucket: _Bucket = self._bucket_array.get(i)

            bucket.for_each(lambda entry: callback(entry.key, entry.value))
        # rof
    # fed

    def size(self):
        return self._size
    # fed
# ssalc


