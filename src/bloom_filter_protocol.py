"""
Protocol defining the interface for the BloomFilter implementation.
Any class that implements these methods and attributes is considered
a valid BloomFilter.
"""

from typing import Protocol


class BloomFilterProtocol(Protocol):
    """
    Structural interface for a Bloom filter.

    Attributes:
        size: Number of bits in the array.
        num_hashes: Number of hash functions used.
        bit_array: The underlying bit array of 0s and 1s.
    """

    size: int
    num_hashes: int
    bit_array: list[int]

    def insert(self, item: str) -> None:
        """
        Insert an item into the Bloom filter.

        Args:
            item: The item to insert.
        """
        ...

    def search(self, item: str) -> bool:
        """
        Check if an item is in the Bloom filter.

        Args:
            item: The item to search for.

        Returns:
            True if item is probably in the set.
            False if item is definitely not in the set.
        """
        ...

    def get_positions(self, item: str) -> list[int]:
        """
        Return all hash positions for a given item.

        Args:
            item: The item to hash.

        Returns:
            List of positions in the bit array.
        """
        ...
