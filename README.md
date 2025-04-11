# NeuroEventTools

## Overview
This repository contains Python scripts developed to handle and preprocess neuroimaging datasets. It demonstrates robust methods for parsing, organizing, and managing complex datasets, including nested structures and mixed data types.

## Features
- **Data Parsing:** Extracting and organizing data from raw neuroimaging files into pandas DataFrame.
- **Error Handling:** Implementing techniques to manage diverse data formats and ensure reliable execution.
- **Pythonic Methods:** Using Python libraries such as NumPy, pandas, and custom-built classes for efficient data processing.
- **Output:** The methods generate a DataFrame for clear visualization of events, timings, and overall dataset organization.

## Code description
- The class **Neve** is used to handle the neural event dataset.
- THe 'NeuroEvent()' method converts the neural event dataset to a pandas DataFrame for further analysis.
- The 'describe_data' method provide basic stats for the dataset, specifically the Onset(s) column.
