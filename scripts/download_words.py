"""
Downloads the NLTK words corpus and generates DNA sequences.
Saves both to the data/ directory.
Run this once before benchmarking.
"""

import os
import random
import nltk
from nltk.corpus import words

nltk.download("words")


os.makedirs("data", exist_ok=True)

# save english words
english = words.words()
with open("data/english_words.txt", "w") as f:
    for word in english:
        f.write(word + "\n")

print(f"Saved {len(english)} English words to data/english_words.txt")

# generate and save DNA sequences
bases = ["A", "T", "C", "G"]
dna_sequences = ["".join(random.choices(bases, k=10)) for _ in range(len(english))]

with open("data/dna_sequences.txt", "w") as f:
    for seq in dna_sequences:
        f.write(seq + "\n")

print(f"Saved {len(dna_sequences)} DNA sequences to data/dna_sequences.txt")
