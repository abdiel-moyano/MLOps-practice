import pandas as pd
import numpy as np

# 1. Data simulation
data = {
    'ResourceID': ['VM-01', 'VM-02', 'VM-01', 'VM-03', 'VM-02'],
    'Timestamp': ['2023-01-01 10:00', '2023-01-01 10:05', '2023-01-01 10:00', '2023-01-01 10:10', '2023-01-01 10:15'],
    'Temperature': [72.5, np.nan, 72.5, 85.2, 78.0],
    'CPU_Usage': [45, 89, 45, 92, 10]
}
df = pd.DataFrame(data)

# --- DATA PRE-PROCESSING PIPELINE ---

# 1. Convert 'Timestamp' strings to Pandas datetime objects
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# 2. Drop duplicate records to ensure data integrity (Idempotency)
df = df.drop_duplicates()

# 3. Handle missing values in 'Temperature' using Mean Imputation
# Note: In a production environment, this mean should be a persisted artifact.
df['Temperature'] = df['Temperature'].fillna(df['Temperature'].mean())

# 4. Feature Engineering: Create 'Is_Overheating' flag (Vectorized operation)
# Returns 1 if Temp > 80, else 0.
df['Is_Overheating'] = (df['Temperature'] > 80).astype(int)

# 5. The NumPy Bridge: Convert specific features into a matrix (ndarray) for model consumption
X = df[['Temperature', 'CPU_Usage']].values

print(X)