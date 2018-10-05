
# coding: utf-8

# # Statistical Methods in Pandas - Lab

# ## Introduction
# 
# In this lesson you'll get some hands on experience using some of the key summary statistics methods in Pandas.

# ## Objectives:
# You will be able to:
# 
# * Understand and use the df.describe() and df.info() summary statistics methods
# * Use built-in Pandas methods for calculating summary statistics (.mean(), .std(), .count(), .sum(), .mean(), .median(), .std(), .var() and .quantile())
# * Apply a function to every element in a Series or DataFrame using s.apply() and df.applymap()
# 
# 
# ## Getting Started
# 
# For this lab, we'll be working with a dataset containing information on various lego datasets.  You will find this dataset in the file `lego_sets.csv`.  
# 
# In the cell below:
# 
# * Import pandas and set the standard alias of `pd`
# * Load in the `lego_sets.csv`dataset using the `read_csv()` function
# * Display the head of the DataFrame to get a feel for what we'll be working with

# In[1]:


import pandas as pd
df = pd.read_csv('lego_sets.csv')
df.head()


# In[3]:


df.shape


# ## Getting DataFrame-Level Statistics
# 
# We'll begin by getting some overall summary statistics on the dataset.  There are two ways we'll get this information-- `.info()` and `.describe()`.
# 
# ### Using `.info()`
# 
# The `.info()` method provides us metadata on the DataFrame itself.  This allows to answer questions such as:
# 
# * What data type does each column contain?
# * How many rows are in my dataset? 
# * How many total non-missing values does each column contain?
# * How much memory does the DataFrame take up?
# 
# In the cell below, call our DataFrame's `.info()` method. 

# In[2]:


df.info()


# #### Interpreting the Results
# 
# Read the output above, and then answer the following questions:
# 
# How many total rows are in this DataFrame?  How many columns contain numeric data? How many contain categorical data?  Identify at least 3 columns that contain missing values. 
# 
# Write your answer below this line:
# ________________________________________________________________________________________________________________________________
# 
# There are 12261 rows, as evidenced by the Range Index listed in the output.  Of the 14 columns in this dataset, 7 contain numeric data stored as `float64`, and the other 7 contain strings, which pandas lists as `object`.  The column `num_reviews`, `review_difficulty`, and `val_star_rating` all contain missing values.  We can tell this because the number of entries for each of those columns is less than the total number of entries described by the Range Index. 
# 
# 
# 
# ## Using `.describe()`
# 
# Whereas `.info()` provides statistics about the DataFrame itself, `.describe()` returns output containing basic summary statistics about the data contained with the DataFrame.  
# 
# In the cell below, call the DataFrame's `.describe()` method. 

# In[4]:


df.describe()


# #### Interpreting the Results
# 
# The output contains descriptive statistics corresponding to the columns.  Use these to answer the following questions:
# 
# How much is the standard deviation for piece count?  How many pieces are in the largest lego set?  How many in the smallest lego set? What is the median `val_star_rating`?
# 
# ________________________________________________________________________________________________________________________________
# 
# The standard deviation is 825 pieces.  The largest lego set contains 7,541 pieces, while the smallest contains only 1.  The median value for `val_star_rating` is 4.3.
# 
# ## Getting Summary Statistics
# 
# Pandas also allows us to easily compute individual summary statistics using built-in methods.  Next, we'll get some practice using these methods. 
# 
# In the cell below, compute the median value of the `star_rating` column.

# In[ ]:


df['star_rating'].median()


# Next, get a count of the total number of values in `play_star_rating`.

# In[ ]:


df['play_star_rating'].count()


# Now, compute the standard deviation of the `list_price` column.

# In[ ]:


df['list_price'].std()


# If we bought every single lego set in this dataset, how many pieces would we have?  Use the `.sum()` method on the correct column to compute this. 

# In[ ]:


df['piece_count'].sum()


# Now, let's try getting the value for the 90% quantile.  Do this in the cell below.

# In[ ]:


df.quantile(0.9)


# ## Getting Summary Statistics on Categorical Data
# 
# For obvious reasons, most of the methods we've used so far only work with numerical data--there's no way to calculate the standard deviation of a column containing string values. However, there are some things that we can discover about columns containing categorical data. 
# 
# In the cell below, get the `.unique()` values contained within the `review_difficulty` column. 

# In[ ]:


df['review_difficulty'].unique()


# Now, let's get the `value_counts` for this column, to see how common each is. 

# In[ ]:


df['review_difficulty'].value_counts()


# As you can see, these provide us quick and easy ways to get information on columns containing categorical information.  
# 
# 
# ## Using `.applymap()`
# 
# When working with pandas DataFrames, we can quickly compute functions on the data contained by using the `applymap()` function and passing in a lambda function. 
# 
# For instance, we can use `applymap()` to return a version of the DataFrame where every value has been converted to a string.
# 
# In the cell below:
# 
# * Call our DataFrame's `.applymap()` function and pass in `lambda x: str(x)`
# * Call our new `string_df` object's `.info()` method to confirm that everything has been cast to a string

# In[ ]:


string_df = df.applymap(lambda x: str(x))
string_df.info()


# Note that everything--even the `NaN` values, have been cast to a string in the example above. 
# 
# Note that for pandas Series objects (such as a single column in a DataFrame), we can do the same thing using the `apply()` method.  
# 
# This is just one example of how we can quickly compute custom functions on our DataFrame--this will become especially useful when we learn how to **_normalize_** our datasets in a later section!
# 
# # Conclusion
# 
# In this lab, we learned how to:
# 
# * Understand and use the df.describe() and df.info() summary statistics methods
# * Use built-in Pandas methods for calculating summary statistics (.mean(), .std(), .count(), .sum(), .mean(), .median(), .std(), .var() and .quantile())
# * Apply a function to every element in a Series or DataFrame using s.apply() and df.applymap()
