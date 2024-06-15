# -*- coding: utf-8 -*-
"""ass4

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1N9CetaHttt9hXH6ayR7CjqqohL05sU5W
"""

import pandas as pd
import numpy as np

temp = pd.read_csv("/content/iris.csv")
print(temp.index)

print(temp.columns)
print(temp.shape)
temp.info()

print(temp.head())

print(temp.tail())

# to know unique values
temp.nunique()

# to know unique values
temp.nunique()

temp.isna().sum()

temp.isnull().sum()

print(temp.describe())

import pandas as pd

# Example data (replace with your actual DataFrame)
data = {
    'sepal.length': [5.1, 4.9, 4.7, 4.6, 5.0],
    'sepal.width': [3.5, 3.0, 3.2, 3.1, 3.6],
    'petal.length': [1.4, 1.4, 1.3, 1.5, 1.4],
    'petal.width': [0.2, 0.2, 0.2, 0.2, 0.2],
    'species': ['Setosa', 'Setosa', 'Setosa', 'Setosa', 'Setosa']
}

# Create DataFrame
df = pd.DataFrame(data)

# Extract numeric columns
numeric_cols = df.select_dtypes(include='number')

# Calculate mean, median, and mode
mean_values = numeric_cols.mean()
median_values = numeric_cols.median()
mode_values = numeric_cols.mode().iloc[0]  # Get the first row of the mode DataFrame

# Print the results
print("Mean values:")
print(mean_values)
print("\nMedian values:")
print(median_values)
print("\nMode values:")
print(mode_values)

import pandas as pd
import numpy as np

# Example data (replace with your actual DataFrame)
data = {
    'sepal.length': [5.1, 4.9, 4.7, 4.6, 5.0],
    'sepal.width': [3.5, 3.0, 3.2, 3.1, 3.6],
    'petal.length': [1.4, 1.4, 1.3, 1.5, 1.4],
    'petal.width': [0.2, 0.2, 0.2, 0.2, 0.2],
    'species': ['Setosa', 'Setosa', 'Setosa', 'Setosa', 'Setosa']
}

# Create DataFrame
temp = pd.DataFrame(data)

# Variance
variance = temp['sepal.length'].var()
print("Variance:", variance)

# Standard deviation
std_deviation = temp['sepal.length'].std()
print("Standard Deviation:", std_deviation)

# Mean Absolute Deviation (MAD)
mad = np.mean(np.abs(temp['sepal.length'] - temp['sepal.length'].mean()))
print("Mean Absolute Deviation (MAD):", mad)

# Range
range_value = max(temp['sepal.length']) - min(temp['sepal.length'])
print("Range:", range_value)

# Interquartile Range (IQR)
Q1 = np.percentile(temp['sepal.length'], 25)
Q3 = np.percentile(temp['sepal.length'], 75)
IQR = Q3 - Q1
print("Interquartile Range (IQR):", IQR)

#Measure of frequency destribution
unique, counts = np.unique(temp['sepal.length'], return_counts=True)
print(unique, counts)

matrix = np.corrcoef(temp['sepal.length'], temp['sepal.width'])
print(matrix)
print('\n\n')
print(temp[['sepal.length', 'sepal.width']].corr())

import pandas as pd

# Example data (replace with your actual DataFrame)
data = {
    'sepal.length': [5.1, 4.9, 4.7, 4.6, 5.0],
    'sepal.width': [3.5, 3.0, 3.2, 3.1, 3.6],
    'petal.length': [1.4, 1.4, 1.3, 1.5, 1.4],
    'petal.width': [0.2, 0.2, 0.2, 0.2, 0.2],
    'species': ['Setosa', 'Setosa', 'Setosa', 'Setosa', 'Setosa']
}

# Create DataFrame
temp = pd.DataFrame(data)

# Drop non-numeric columns if necessary
numeric_temp = temp.select_dtypes(include='number')

# Calculate correlation matrix
matrix = numeric_temp.corr()

# Print correlation matrix
print(matrix)

import seaborn as sns
sns.pairplot(temp)

import pandas as pd
import seaborn as sns

# Example data (replace with your actual DataFrame)
data = {
    'sepal.length': [5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0],
    'sepal.width': [3.5, 3.0, 3.2, 3.1, 3.6, 3.9, 3.4, 3.4],
    'petal.length': [1.4, 1.4, 1.3, 1.5, 1.4, 1.7, 1.4, 1.5],
    'petal.width': [0.2, 0.2, 0.2, 0.2, 0.2, 0.4, 0.3, 0.2],
    'species': ['Setosa', 'Setosa', 'Setosa', 'Setosa', 'Setosa', 'Setosa', 'Setosa', 'Setosa']
}

# Create DataFrame
temp = pd.DataFrame(data)

# Exclude non-numeric columns and calculate correlation matrix
numeric_temp = temp.select_dtypes(include='number')
corr_setosa = numeric_temp.corr()

# Print correlation matrix for 'Setosa' species subset
print("Correlation matrix for 'Setosa' species subset:")
print(corr_setosa)

# Create pairplot for 'Setosa' species subset using Seaborn
sns.pairplot(temp[temp['species'] == 'Setosa'], vars=numeric_temp.columns)

import matplotlib.pyplot as plt
bxplt = sns.boxplot(temp['sepal.width'])
plt.show()

Q1 = np.percentile(temp['sepal.width'], 25.) # 25th percentile of the data of the given feature
Q3 = np.percentile(temp['sepal.width'], 75.) # 75th percentile of the data of the given feature
IQR = Q3-Q1 #Interquartile Range
#outlier_step = IQR * 1.5 #That's we were talking about above
#outliers = feature_data[~((feature_data >= Q1 - outlier_step) & (feature_data <= Q3 + outlier_step))].index.tolist()
ll = Q1 - (1.5*IQR)
ul = Q3 + (1.5*IQR)
upper_outliers = temp[temp['sepal.width'] > ul].index.tolist()
lower_outliers = temp[temp['sepal.width'] < ll].index.tolist()
bad_indices = list(set(upper_outliers + lower_outliers))
drop = True
#if not drop:
    #print('For the feature {}, No of Outliers is {}'.format(temp['sepal.width'], len(bad_indices)))
if drop:
    temp.drop(bad_indices, inplace = True, errors = 'ignore')
    print('Outliers from {} feature removed'.format(temp['sepal.width']))

bxplt = sns.boxplot(temp['sepal.width'])
plt.show()

# Example using pandas get_dummies for one-hot encoding
encoded_temp = pd.get_dummies(temp, columns=['species'])
print(encoded_temp.head())

# Example: Calculating petal area for flower dataset
temp['petal_area'] = temp['petal.length'] * temp['petal.width']
print(temp.head())

from sklearn.preprocessing import StandardScaler

# Example: Standard scaling of numerical features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(temp[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']])
temp[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']] = scaled_features
print(temp.head())

import pandas as pd

# Example data (replace with your actual DataFrame)
data = {
    'sepal.length': [5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0],
    'sepal.width': [3.5, 3.0, 3.2, 3.1, 3.6, 3.9, 3.4, 3.4],
    'petal.length': [1.4, 1.4, 1.3, 1.5, 1.4, 1.7, 1.4, 1.5],
    'petal.width': [0.2, 0.2, 0.2, 0.2, 0.2, 0.4, 0.3, 0.2],
    'species': ['Setosa', 'Setosa', 'Setosa', 'Setosa', 'Setosa', 'Setosa', 'Setosa', 'Setosa']
}

# Create DataFrame
temp = pd.DataFrame(data)

# Define bins and labels for sepal length categories
bins = [0, 5, 6]  # Define the bin edges
labels = ['Short', 'Medium']  # Provide labels for the intervals defined by bins

# Bin 'sepal.length' into categories
temp['sepal_length_category'] = pd.cut(temp['sepal.length'], bins=bins, labels=labels)

# Display the updated DataFrame
print(temp.head())

# Example: Interaction between sepal length and petal width
temp['sepal_length_petal_width'] = temp['sepal.length'] * temp['petal.width']
print(temp.head())

import pandas as pd
import numpy as np

# Example data (replace with your actual DataFrame)
data = {
    'sepal.length': ['5.1', '4.9', '4.7', 'Setosa', '5.0', '5.4', '4.6', '5.0']
}

# Create DataFrame
temp = pd.DataFrame(data)

# Convert 'sepal.length' to numeric, coercing errors to NaN
temp['sepal.length'] = pd.to_numeric(temp['sepal.length'], errors='coerce')

# Drop NaN values if any
temp.dropna(inplace=True)

# Calculate mean, median, and mode
mean_value = temp['sepal.length'].mean()
median_value = temp['sepal.length'].median()
mode_value = temp['sepal.length'].mode()

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")

