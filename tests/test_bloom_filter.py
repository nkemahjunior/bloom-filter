"""
Tests for the BloomFilter implementation.
"""

from src.bloom_filter import BloomFilter


class TestBloomFilterCorrectness:
    """Correctness tests for insert and search operations."""

    def setup_method(self):
        self.bf = BloomFilter(size=1000, num_hashes=3)

    def test_inserted_word_is_found(self):
        self.bf.insert("apple")
        assert self.bf.search("apple") is True

    def test_multiple_inserted_words_are_found(self):
        words = ["apple", "banana", "cat", "dog", "elephant"]
        for word in words:
            self.bf.insert(word)
        for word in words:
            assert self.bf.search(word) is True

    def test_never_produces_false_negatives(self):
        words = ["apple", "banana", "cat"]
        for word in words:
            self.bf.insert(word)
        for word in words:
            assert self.bf.search(word) is True

    def test_empty_filter_returns_false(self):
        assert self.bf.search("apple") is False


class TestBloomFilterHashFunctions:
    """Tests for hash function behaviour."""

    def setup_method(self):
        self.bf = BloomFilter(size=1000, num_hashes=3)

    def test_get_positions_returns_list(self):
        assert isinstance(self.bf.get_positions("apple"), list)

    def test_get_positions_correct_length(self):
        assert len(self.bf.get_positions("apple")) == self.bf.num_hashes

    def test_get_positions_within_bounds(self):
        assert all(
            0 <= pos < self.bf.size for pos in self.bf.get_positions("apple"))

    def test_get_positions_deterministic(self):
        assert self.bf.get_positions("apple") == self.bf.get_positions("apple")

    def test_different_items_give_different_positions(self):
        assert self.bf.get_positions(
            "apple") != self.bf.get_positions("banana")


# Edge case tests for empty strings, single chars, and hash seeds
class TestBloomFilterEdgeCases:
    """Edge case tests for unusual inputs."""

    def test_empty_string_can_be_inserted_and_found(self):
        bf = BloomFilter(size=1000, num_hashes=3)
        bf.insert("")
        assert bf.search("") is True

    def test_single_character_items(self):
        bf = BloomFilter(size=1000, num_hashes=3)
        for char in "abcdefghij":
            bf.insert(char)
        for char in "abcdefghij":
            assert bf.search(char) is True

    def test_num_hashes_one(self):
        bf = BloomFilter(size=1000, num_hashes=1)
        bf.insert("apple")
        assert bf.search("apple") is True

    def test_positions_differ_per_seed(self):
        bf = BloomFilter(size=10000, num_hashes=5)
        positions = bf.get_positions("apple")
        assert len(positions) == len(set(positions)
                                     ), "hash seeds must produce distinct positions"

    def test_large_num_hashes(self):
        bf = BloomFilter(size=10000, num_hashes=10)
        bf.insert("hello")
        assert bf.search("hello") is True
