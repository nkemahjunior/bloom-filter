"""
Benchmarking script for the BloomFilter implementation.
Measures insert and search performance for increasing number of words.
To be run on the HPC infrastructure.
"""

import csv
import time
import matplotlib.pyplot as plt
from src.bloom_filter import BloomFilter


def load_words(path: str) -> list[str]:
    """Load words from a file, one word per line."""
    with open(path) as f:
        return [line.strip() for line in f.readlines()]


def benchmark_insert(bf: BloomFilter, words: list[str]) -> float:
    """Return time taken to insert all words into the filter."""
    start = time.perf_counter()
    for word in words:
        bf.insert(word)
    return time.perf_counter() - start


def benchmark_search(bf: BloomFilter, words: list[str]) -> float:
    """Return time taken to search all words in the filter."""
    start = time.perf_counter()
    for word in words:
        bf.search(word)
    return time.perf_counter() - start


def run_benchmark_for_dataset(
    all_words: list[str], sizes: list[int], label: str
) -> tuple[list[float], list[float]]:
    """Run insert and search benchmarks for a dataset."""
    insert_times = []
    search_times = []

    for n in sizes:
        words = all_words[:n]
        bf = BloomFilter(size=n * 10, num_hashes=3)

        insert_time = benchmark_insert(bf, words)
        search_time = benchmark_search(bf, words)

        insert_times.append(insert_time)
        search_times.append(search_time)

        print(
            f"[{label}] {n} words: insert={insert_time:.4f}s, "
            f"search={search_time:.4f}s"
        )

    return insert_times, search_times


def save_results(
    sizes: list[int],
    english_insert: list[float],
    english_search: list[float],
    dna_insert: list[float],
    dna_search: list[float],
) -> None:
    """Save benchmark results to a text file."""
    with open("results/benchmark_results.txt", "w") as f:
        f.write("English Words:\n")
        for i, n in enumerate(sizes):
            f.write(
                f"  {n} words: insert={english_insert[i]:.4f}s, "
                f"search={english_search[i]:.4f}s\n"
            )
        f.write("\nDNA Sequences:\n")
        for i, n in enumerate(sizes):
            f.write(
                f"  {n} words: insert={dna_insert[i]:.4f}s, "
                f"search={dna_search[i]:.4f}s\n"
            )


def plot_results(
    sizes: list[int],
    english_insert: list[float],
    english_search: list[float],
    dna_insert: list[float],
    dna_search: list[float],
) -> None:
    """Plot benchmark results."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    axes[0].plot(sizes, english_insert, marker="o", label="English")
    axes[0].plot(sizes, dna_insert, marker="o", label="DNA")
    axes[0].set_title("Insert Performance")
    axes[0].set_xlabel("Number of words")
    axes[0].set_ylabel("Time (seconds)")
    axes[0].legend()

    axes[1].plot(sizes, english_search, marker="o", label="English")
    axes[1].plot(sizes, dna_search, marker="o", label="DNA")
    axes[1].set_title("Search Performance")
    axes[1].set_xlabel("Number of words")
    axes[1].set_ylabel("Time (seconds)")
    axes[1].legend()

    plt.tight_layout()
    plt.savefig("results/benchmark_plot.png")


def run_benchmarks() -> None:
    sizes = [1000, 10000, 50000, 100000, 200000]

    english_words = load_words("data/english_words.txt")
    dna_sequences = load_words("data/dna_sequences.txt")

    english_insert, english_search = run_benchmark_for_dataset(
        english_words, sizes, "English"
    )
    dna_insert, dna_search = run_benchmark_for_dataset(
        dna_sequences, sizes, "DNA"
    )

    save_results(sizes, english_insert, english_search, dna_insert, dna_search)
    save_results_csv(sizes, english_insert, english_search,
                     dna_insert, dna_search)

    plot_results(sizes, english_insert, english_search, dna_insert, dna_search)


def save_results_csv(
    sizes: list[int],
    english_insert: list[float],
    english_search: list[float],
    dna_insert: list[float],
    dna_search: list[float],
) -> None:
    """Save benchmark results to a CSV file for further analysis."""
    with open("results/benchmark_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "n_words",
            "english_insert_s", "english_search_s",
            "dna_insert_s", "dna_search_s"
        ])
        for i, n in enumerate(sizes):
            writer.writerow([
                n,
                english_insert[i], english_search[i],
                dna_insert[i], dna_search[i]
            ])


if __name__ == "__main__":
    run_benchmarks()
