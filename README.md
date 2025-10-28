Bioinformatics Data Governance and Quality System
=================================================

This project implements a complete data governance pipeline for genomic datasets.  
It validates DNA sequences, evaluates data integrity, and stores automated analysis reports securely in Google Cloud.

The goal is to ensure that bioinformatics datasets are accurate, complete, and ready for downstream research or analysis.

Overview
--------

The project reads and validates DNA or mRNA sequence data (FASTA format), performs quality checks, and calculates GC content and sequence length statistics.  
It then generates an HTML summary report and uploads it to a secure Google Cloud Storage bucket for traceability and governance.

Objectives
----------

• Validate real genomic sequence data obtained from NCBI (for example, the TP53 tumor suppressor gene).  
• Detect invalid or duplicate DNA sequences.  
• Calculate average GC content, sequence length, and overall data quality score.  
• Automate HTML report generation and cloud upload through Google Cloud Storage.

Tools and Skills
----------------

| Tool | Purpose |
|------|----------|
| Python (pandas, biopython) | Sequence validation and analysis |
| Google Cloud Storage | Secure cloud storage and governance |
| HTML / JSON | Reporting and structured data logging |
| Git / GitHub | Version control and documentation |

Repository Contents
-------------------

| File | Description |
|------|--------------|
| src/fasta_to_csv.py | Converts FASTA sequences into structured CSV data |
| src/validate_sequences.py | Performs DNA sequence validation and scoring |
| src/generate_report.py | Generates the HTML report with metrics |
| src/view_logs.py | Displays previous validation runs and scores |
| reports/data_quality_report.html | Example output from TP53 dataset analysis |
| gcp_key.json | Google Cloud service credentials (excluded from public repo) |

Example Output
--------------

| Metric | Result |
|--------|---------|
| Total Records | 2 |
| Invalid Sequences | 0 |
| Duplicates | 0 |
| Missing Values | 0 |
| Data Quality Score | 100% |
| Average Sequence Length | 19,060 bp |
| Average GC Content | 49.38% |

Key Insights
------------

• The TP53 gene data showed 100 percent validity and no missing or duplicate records.  
• GC content and sequence length metrics aligned with published characteristics of TP53 genomic regions.  
• The system demonstrates real-world data governance workflows applied to bioinformatics research.

Author
------

Created by Khushi Patel  
Bioinformatics Data Governance Project – 2025

