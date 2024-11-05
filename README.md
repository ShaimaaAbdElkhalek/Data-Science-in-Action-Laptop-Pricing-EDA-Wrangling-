# Laptop Pricing EDA
![Laptop Pricing EDA](https://github.com/ShaimaaAbdElkhalek/Data-Science-in-Action-Laptop-Pricing-EDA-Wrangling-/blob/main/data/download%20(1).jpeg?raw=true)

This repository contains a Jupyter Notebook for exploratory data analysis (EDA) on a dataset of laptop pricing. The analysis aims to understand the relationships between various laptop features and their prices, utilizing libraries such as Pandas, NumPy, Matplotlib, and Seaborn for data manipulation and visualization.

## Table of Contents
- [Dataset Overview](#dataset-overview)
- [Data Cleaning and Preparation](#data-cleaning-and-preparation)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Visualizations](#visualizations)
- [Final DataFrame](#final-dataframe)
- [Installation](#installation)


## Dataset Overview

The dataset used for this analysis is sourced from [IBM's Developer Skills Network](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_base.csv) and contains the following columns:

- `Manufacturer`: The brand of the laptop.
- `Category`: The category of the laptop.
- `Screen`: The type of screen.
- `GPU`: The graphics processing unit.
- `OS`: The operating system.
- `CPU_core`: The number of CPU cores.
- `Screen_Size_inch`: The screen size in inches.
- `CPU_frequency`: The CPU frequency in GHz.
- `RAM_GB`: The amount of RAM in GB.
- `Storage_GB_SSD`: The storage capacity in GB SSD.
- `Weight_kg`: The weight of the laptop in kg.
- `Price`: The price of the laptop.

## Data Cleaning and Preparation

The notebook includes the following steps for data cleaning and preparation:

1. **Loading the Dataset**: The dataset is loaded using Pandas, and headers are assigned for clarity.
2. **Handling Missing Values**: Missing values are identified and appropriately handled, including replacing placeholders and imputing missing data.
3. **Data Type Conversion**: Certain columns are converted to the correct data types (e.g., numeric, categorical).
4. **Data Standardization**: Screen size is converted from inches to centimeters, and weight is converted from kg to pounds.

## Exploratory Data Analysis

The EDA process includes:

- Descriptive statistical analysis of the dataset.
- Correlation analysis between numerical features and price.
- Visualization of relationships using regression plots for numerical variables.
- Box plots to analyze the impact of categorical features on laptop prices.

## Visualizations

The analysis generates several visualizations to better understand the data:

- **Regression Plots**: To explore relationships between CPU frequency, screen size, weight, and price.
- **Box Plots**: To compare prices across different categories, GPUs, operating systems, CPU cores, RAM, and storage types.
- **Count Plots**: To visualize the distribution of price categories after binning.

## Final DataFrame

The final version of the DataFrame includes all necessary adjustments for analysis, with categorical features transformed into indicator variables.
## Installation

pip install numpy pandas matplotlib seaborn scipy

