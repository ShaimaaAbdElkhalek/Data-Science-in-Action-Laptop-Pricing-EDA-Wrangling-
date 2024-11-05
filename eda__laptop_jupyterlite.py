# -*- coding: utf-8 -*-
"""EDA _Laptop.jupyterlite.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mbJsZWxLyITIt2X2HmcnxCdgnN2i5l7t
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
# %matplotlib inline

headers=["Manufacturer", "Category", "Screen", "GPU", "OS", "CPU_core", "Screen_Size_inch", "CPU_frequency", "RAM_GB", "Storage_GB_SSD", "Weight_kg" ,"Price"]
filepath = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_base.csv"
df = pd.read_csv(filepath, names=headers)

df.head()

df.replace("?", np.nan, inplace=True)

df.dtypes

df.describe(include='all')

df.info()

sns.regplot(x='CPU_frequency' ,y ='Price',data=df)
plt.title('CPU Frequency vs Price')
df['CPU_frequency'].corr(df['Price'])

to_obj=['OS','RAM_GB', 'GPU', 'OS', 'Storage_GB_SSD']
for i in to_obj:
  df[i]=df[i].astype(object)

df['Screen_Size_inch']=pd.to_numeric(df['Screen_Size_inch'], errors='coerce')
df['Weight_kg']=pd.to_numeric(df['Weight_kg'] ,errors='coerce')

sns.regplot(x='Screen_Size_inch' ,y ='Price',data=df)
plt.title('Screen Size_inch vs price')

sns.regplot(x='Weight_kg', y='Price' , data=df)
plt.title('Weight kg vs price')

numeric_cols = ['CPU_frequency', 'Screen_Size_inch', 'Weight_kg']
df[numeric_cols].corrwith(df['Price'])

"""Interpretation: "CPU_frequency" has a 36% positive correlation with the price of the laptops. The other two parameters have weak correlation with price.

### Categorical features
Generate Box plots for the different feature that hold categorical values. These features would be "Category", "GPU", "OS", "CPU_core", "RAM_GB", "Storage_GB_SSD"
"""

sns.boxplot(x='Category',y="Price", data=df)

sns.boxplot(x='GPU',y="Price", data=df)

sns.boxplot(x="OS",y="Price",data=df)

sns.boxplot(x='CPU_core',y="Price", data=df)

sns.boxplot(x='RAM_GB',y="Price", data=df)

df.GPU.value_counts()

sns.boxplot(x='Storage_GB_SSD',y="Price", data=df)

"""#  Descriptive Statistical Analysis

"""

df.describe(include='all')

"""#GroupBy and Pivot Tables

Group the parameters "GPU", "CPU_core" and "Price" to make a pivot table and visualize this connection using the pcolor plot.

"""

df_test=df[[  "GPU", "CPU_core" , "Price"  ]]
df_grp=df_test.groupby(["GPU", "CPU_core"]  , as_index=False  ).mean()
df_grp

df_pivot=df_grp.pivot(index='GPU' , columns= 'CPU_core')
df_pivot

"""# Data Wrangling


 - Handle missing data in different ways
 - Correct the data type of different data values as per requirement
 - Standardize and normalize the appropriate data attributes
 - Visualize the data as grouped bar graph using Binning
 - Cnverting a categorical data into numerical indicator variables

### Data Standardization
The value of Screen_size usually has a standard unit of inches. Similarly, weight of the laptop is needed to be in pounds. Use the below mentioned units of conversion and write a code to modify the columns of the dataframe accordingly. Update their names as well.

```{math}
1 inch = 2.54 cm
1 kg   = 2.205 pounds
```
"""

df['Screen_Size_cm']=df['Screen_Size_inch']/2.54
df.drop(['Screen_Size_inch' ],axis=1,inplace=True)

df.head()

df['Screen_Size_cm']=df['Screen_Size_cm'].astype('float')
df['Weight_kg']=df['Weight_kg'].astype('float')

to_num=['Screen_Size_cm','Weight_kg' ]
for i in to_num:
  df[i]=pd.to_numeric(df[i], errors='coerce')

"""Note that we can update the `Screen_Size_cm` column such that all values are rounded to nearest 2 decimal places by using `numpy.round()`

"""

df[['Screen_Size_cm']] = np.round(df[['Screen_Size_cm']],2)
df.head()

df.isnull().sum()

timpute=['Screen_Size_cm','Weight_kg']
for col in timpute:
  df[col]=df[col].fillna(df[col].mean())

timpute=['Screen_Size_cm','Weight_kg']
for col in timpute:
  df[col]=df[col].fillna(df[col].mode())

"""### Data Normalization

"""

df['CPU_frequency']=df['CPU_frequency']/df['CPU_frequency'].max()
df['CPU_frequency'].min(), df['CPU_frequency'].max()

"""### Binning

"""

df['Price'].dtype

Price_binned=np.linspace(min(df['Price']) , max(df['Price']) ,4)
g_names=["Low", "Medium" , "High"]
Price_binned
df['Price_binned']=pd.cut(df['Price'],Price_binned, labels=g_names  ,include_lowest=True)
df[['Price', 'Price_binned']].head(30)

df['Price_binned'].value_counts()

"""plot the bar graph of these bins.

"""

import seaborn as sns
sns.countplot(x='Price_binned', data=df)

"""

### Indicator variables
Convert the "Screen" attribute of the dataset into 2 indicator variables, "Screen-IPS_panel" and "Screen-Full_HD". Then drop the "Screen" attribute from the dataset.
"""

# Write your code below and press Shift+Enter to execute
df['Screen'].value_counts()

dummy_variables=pd.get_dummies(df['Screen'])
dummy_variables.head()

dummy_variables.rename(columns={'Full HD	':'Screen-Full_HD' ,'IPS Panel':'Screen-IPS_panel' },inplace=True)
df=pd.concat([df,dummy_variables],axis=1)

df.drop('Screen', axis=1,inplace=True)
df.head()

"""This version of the dataset, now finalized, is the one you'll be using in all subsequent modules.

Print the content of dataframe.head() to verify the changes that were made to the dataset.
"""

print(df.head())