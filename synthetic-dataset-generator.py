#import libraries
import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
num_samples = 1000

# Create touchpoint data
touchpoints = ['Ad', 'Email', 'Social', 'Search', 'Direct']
num_touchpoints = len(touchpoints)
touchpoint_data = np.random.choice(touchpoints, size=num_samples)

# Create conversion data
conversion_data = np.random.choice([0, 1], size=num_samples, p=[0.8, 0.2])

# Create timestamp data
start_date = pd.to_datetime('2022-01-01')
end_date = pd.to_datetime('2022-12-31')
timestamps = pd.date_range(start_date, end_date, periods=num_samples)

# Combine data into a DataFrame
dataset = pd.DataFrame({'Timestamp': timestamps, 'Touchpoint': touchpoint_data, 'Conversion': conversion_data})

# Print the first few rows of the generated dataset
print(dataset.head())

dataset.to_csv("att_data.csv",index=false)
