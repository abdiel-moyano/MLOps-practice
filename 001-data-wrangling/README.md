# Module 001: Data Wrangling & Pre-processing

## 🎯 Implementation Objective
The goal of this module is to operationalize the transformation of raw telemetry data into model-ready features. In an MLOps lifecycle, this stage is critical for ensuring that the data consumed by the model is clean, consistent, and mathematically valid.

## 🏗 Key Architectural Patterns

### 1. Vectorized Operations vs. Iterative Loops
To ensure high-throughput and low-latency in production pipelines, all transformations are implemented using **Vectorization** (via Pandas and NumPy). By delegating computations to C-level SIMD instructions, we eliminate the overhead of the Python interpreter's `for` loops.

### 2. Handling Data Decay (Imputation Strategy)
Real-world sensors often fail, leading to missing values (`NaN`). This module implements **Mean Imputation** to maintain pipeline stability. 
* **Architectural Note:** While this script calculates the mean dynamically for demonstration, in a production-grade "Training-Serving" architecture, this value is persisted as a **Metadata Artifact** to prevent *Training-Serving Skew*.

### 3. Feature Engineering
We implemented a logic-gate to transform raw temperature readings into a binary feature (`Is_Overheating`). This simplifies the decision boundary for the ML model, improving predictive performance.

## 🛠 Technical Stack
* **Python 3.12**
* **Pandas:** Structured data manipulation and DataFrame management.
* **NumPy:** High-performance numerical operations and "NumPy Bridge" implementation.

## 🚀 Environment Setup & Execution
To ensure reproducibility, follow these steps using a Virtual Environment:

```bash
# 1. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the pre-processing pipeline
python pre_processing.py
```

## 📊 Expected Output
The script generates a NumPy ndarray (2D Matrix). This matrix is the final input for the model's .predict() method, following the structure:

| Index | Feature Name | Description |
|-------|--------------|-------------|
| 0 | Temperature | Imputed value (Mean) |
| 1 | CPU_Usage | Raw telemetry value |
| 2 | Is_Overheating | Binary flag (0/1) |