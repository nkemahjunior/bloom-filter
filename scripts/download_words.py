"""
Downloads the NLTK words corpus and generates DNA sequences.
Saves both to the data/ directory.
Run this once before benchmarking.
"""

import os
import random
import nltk
from nltk.corpus import words


def download_english_words(path: str) -> list[str]:
    """Download NLTK words corpus and save to file."""
    nltk.download("words", quiet=True)
    english = words.words()
    with open(path, "w") as f:
        for word in english:
            f.write(word + "\n")
    print(f"Saved {len(english)} English words to {path}")
    return english


def generate_dna_sequences(n: int, length: int, seed: int = 42) -> list[str]:
    """Generate random DNA sequences of fixed length."""
    random.seed(seed)
    bases = ["A", "T", "C", "G"]
    return ["".join(random.choices(bases, k=length)) for _ in range(n)]


def save_dna_sequences(sequences: list[str], path: str) -> None:
    """Save DNA sequences to file."""
    with open(path, "w") as f:
        for seq in sequences:
            f.write(seq + "\n")
    print(f"Saved {len(sequences)} DNA sequences to {path}")


def main() -> None:
    os.makedirs("data", exist_ok=True)

    english = download_english_words("data/english_words.txt")

    dna_sequences = generate_dna_sequences(n=len(english), length=10)
    save_dna_sequences(dna_sequences, "data/dna_sequences.txt")


if __name__ == "__main__":
    main()
