"""
Bloom Filter implementation for Concepts of Data Science 2025-2026.

A Bloom filter is a space-efficient probabilistic data structure that supports
fast insert and membership queries with a controllable false positive rate.
False positives are possible, but false negatives are not.
"""

import hashlib


class BloomFilter:
    """
    A space-efficient probabilistic data structure for set membership queries.

    Uses multiple hash functions derived from SHA-256 with different seeds
    to map items to positions in a bit array.

    Attributes:
        size (int): Number of bits in the bit array.
        num_hashes (int): Number of hash functions applied per item.
        bit_array (list[int]): The underlying bit array, initialised to zeros.
    """

    def __init__(self, size: int, num_hashes: int) -> None:
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [0] * size

    def _hash(self, item: str, seed: int) -> int:
        data = f"{seed}:{item}".encode("utf-8")
        digest = hashlib.sha256(data).hexdigest()
        return int(digest, 16) % self.size

    def get_positions(self, item: str) -> list[int]:
        return [self._hash(item, seed) for seed in range(self.num_hashes)]

    def insert(self, item: str) -> None:
        for position in self.get_positions(item):
            self.bit_array[position] = 1

    def search(self, item: str) -> bool:
        for position in self.get_positions(item):
            if self.bit_array[position] == 0:
                return False
        return True
