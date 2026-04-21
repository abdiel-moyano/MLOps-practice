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
* **Pandas:** Used for structured data manipulation and DataFrame management.
* **NumPy:** Used for high-performance numerical operations and the final "NumPy Bridge" (converting DataFrames to Matrices).

## 🚀 How to Run
Ensure you have the requirements installed:
```bash
pip install pandas numpy
```

Run the pre-processing script:

```bash
python pre_processing.py
```

## 📊 Expected Output
The script produces a processed NumPy ndarray (2D Matrix) representing the feature set:

Column 0: Temperature (Imputed)

Column 1: CPU Usage

Column 2: Is_Overheating (Calculated)