# Bloom Filter - Concepts of Data Science 2025-2026

## Team Members
- Junior Nkemah Kaving
- Rexford Holland

## Project Overview
Implementation of a Bloom filter - a space-efficient probabilistic data structure
that supports fast insert and search operations with a controllable false positive rate.

## Repository Structure

```
bloom-filter/
├── src/
│   └── bloom_filter.py        - BloomFilter implementation
├── notebooks/
│   └── demo.ipynb             - demonstration, testing, and experiments
├── scripts/
│   ├── benchmark.py           - performance benchmarking script for HPC
│   ├── download_words.py      - downloads and generates test data
│   └── job_script.sh          - HPC job submission script
├── tests/
│   └── test_bloom_filter.py   - formal correctness tests
├── results/                   - benchmark outputs and plots
├── data/                      - test data (generated locally, not tracked by git)
├── pyproject.toml             - package configuration
├── requirements.txt           - project dependencies
└── README.md
```


## Setup

### 1. Clone the repository
```bash
git clone https://github.com/nkemahjunior/bloom-filter.git
cd bloom-filter
```

### 2. Install dependencies
```bash
pip install -e .
pip install -r requirements.txt
```

### 3. Generate test data
```bash
python scripts/download_words.py
```

## Running the Tests
```bash
pytest tests/
```

## Running the Notebook
Open `notebooks/demo.ipynb` in Jupyter or VS Code.

## Running the Benchmark
Locally:
```bash
python scripts/benchmark.py
```

On HPC:
```bash
sbatch scripts/job_script.sh
```

## Conclusions
- `insert` and `search` both run in **O(k)** time where k is the number of hash
  functions. Average time per operation stays flat as n grows, confirmed by benchmarks.
- The false positive rate grows as more items are inserted and rises sharply once
  insertions exceed the filter's designed capacity.
- The Bloom filter achieves significant memory compression compared to a Python `set`,
  with compression improving as the number of stored items grows.
- Hash uniformity is good for English words. DNA sequences show some clustering due
  to the limited 4-character alphabet, meaning hash functions distribute less evenly.
- Optimal filter size depends on the target false positive rate — tighter rates
  require larger bit arrays but still remain far more compact than storing items directly.