# Sequence Analytics System  
*(Bioinformatics Data Governance for TP53 Gene Sequences)*

![Project Preview](reports/preview.png)
This project implements a complete data governance pipeline for genomic datasets.  
It validates DNA and mRNA sequences, evaluates data integrity, and stores automated quality metrics in a local SQLite database.

The goal is to ensure that bioinformatics datasets are accurate, complete, and reproducible through automated validation and reporting.

---

## Overview

This project implements a data governance and validation pipeline for genomic sequences, focusing on the **TP53 gene** , a well-studied tumor suppressor associated with several human cancers.  
It demonstrates how to validate, analyze, and manage biological sequence data using Python and cloud-based infrastructure.

---
### Why TP53?
TP53 is a critical tumor suppressor gene responsible for regulating cell cycle and apoptosis.  
Mutations in TP53 are among the most common genetic alterations found in human cancers, making it an ideal candidate for demonstrating sequence validation and quality governance in bioinformatics workflows.

---

## Objectives

- Validate real genomic sequence data obtained from NCBI (e.g., the **TP53** tumor suppressor gene).  
- Detect invalid or duplicate DNA sequences.  
- Calculate average GC content, sequence length, and overall data quality score.  
- Automate HTML report generation and cloud upload using Google Cloud Storage.  
- Maintain a historical log of all validation runs in SQLite for reproducibility.

---

## Tools and Skills

| Tool | Purpose |
|------|----------|
| Python (pandas, biopython) | Sequence validation and analysis |
| SQLite | Local database for versioned logging |
| Google Cloud Storage | Secure cloud storage and governance |
| HTML / JSON | Reporting and structured data logging |
| Git / GitHub | Version control and documentation |

---

## Repository Contents

| File | Description |
|------|--------------|
| `src/fasta_to_csv.py` | Converts FASTA sequences into structured CSV data |
| `src/validator_step1.py` | Performs initial data validation and missing value checks |
| `src/validator_step2.py` | Performs DNA sequence validation and scoring |
| `src/generate_report.py` | Generates the HTML report with metrics |
| `src/view_logs.py` | Displays previous validation runs and quality scores |
| `reports/data_quality_report.html` | Example output from the TP53 dataset analysis |
| `governance.db` | Local SQLite database for tracking validation runs |
| `.gitignore` | Ensures sensitive keys (e.g., `gcp_key.json`) are excluded from commits |

---

## Example Output

| Metric | Result |
|--------|---------|
| Total Records | 2 |
| Invalid Sequences | 0 |
| Duplicates | 0 |
| Missing Values | 0 |
| Data Quality Score | 100% |
| Average Sequence Length | 19,060 bp |
| Average GC Content | 49.38% |

---

## Author

Created by **Khushi Patel**

