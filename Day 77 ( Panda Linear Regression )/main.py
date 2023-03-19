"""
Use nested loops to remove unwanted characters from multiple columns

Filter Pandas DataFrames based on multiple conditions using both .loc[] and .query()

Create bubble charts using the Seaborn Library

Style Seaborn charts using the pre-built styles and by modifying Matplotlib parameters

Use floor division (i.e., integer division) to convert years to decades

Use Seaborn to superimpose a linear regressions over our data

Make a judgement if our regression is good or bad based on how well the model fits our data and the r-squared metric

Run regressions with scikit-learn and calculate the coefficients.

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
# Read Data set
df_cost_revenue = pd.read_csv("cost_revenue_dirty.csv")

# How many rows and columns does df_apps have? What are the column names?
# What does the data look like?
# Look at a random sample of 5 different rows with

# print(df_cost_revenue.shape)
# print(df_cost_revenue.columns)
# print(df_cost_revenue.head())
# print(df_cost_revenue.sample(5))
df_cost_revenue_cols = df_cost_revenue.columns

# Clean up
# print(f"any nun values ? {df_cost_revenue.isna().values.any()}")
# print(f"any duplicate values? {df_cost_revenue.duplicated(subset=['Movie_Title', 'Release_Date']).values.any()} ")
# print(f"how many duplicate values? {df_cost_revenue.duplicated(subset=['Movie_Title', 'Release_Date']).values.sum()}")
df_cost_revenue.drop_duplicates(subset=['Movie_Title', 'Release_Date'], inplace=True)
# print(f"any duplicate values? {df_cost_revenue.duplicated(subset=['Movie_Title', 'Release_Date']).values.any()} ")

# Type check
"""
print(df_cost_revenue_cols)
for item in df_cost_revenue_cols:
    print(f" the column name is {item} \ntype of first item in this column is {type(df_cost_revenue[item][0])}\n"
          f" the first item in this column is {df_cost_revenue[item][0]}\n\n")

"""

# Convert  to numeric format
chars_to_remove = [',', '$']
columns_to_clean = ['USD_Production_Budget',
                    'USD_Worldwide_Gross',
                    'USD_Domestic_Gross']

for col in columns_to_clean:
    for char in chars_to_remove:
        # Replace each character with an empty string
        df_cost_revenue[col] = df_cost_revenue[col].astype(str).str.replace(char, "")
    # Convert column to a numeric data type
    df_cost_revenue[col] = pd.to_numeric(df_cost_revenue[col])

# print(df_cost_revenue["Release_Date"])
df_cost_revenue["Release_Date"] = pd.to_datetime(df_cost_revenue["Release_Date"])
# print(df_cost_revenue.info())
# print(df_cost_revenue["Release_Date"])

# What is the average production budget of the films in the data set?
print(df_cost_revenue.describe())
print(df_cost_revenue["USD_Production_Budget"].mean())

# What is the average worldwide gross revenue of films?
print(df_cost_revenue["USD_Worldwide_Gross"].mean())

# What were the minimums for worldwide and domestic revenue?
print(df_cost_revenue["USD_Worldwide_Gross"].min())
print(df_cost_revenue["USD_Domestic_Gross"].min())

# Are the bottom 25% of films actually profitable or do they lose money?

# What are the highest production budget and highest worldwide gross revenue of any film?
print(df_cost_revenue["USD_Worldwide_Gross"].max())
print(df_cost_revenue["USD_Production_Budget"].max())

# How much revenue did the lowest and highest budget films make?
df_cost_revenue["total_revenue"] = df_cost_revenue['USD_Worldwide_Gross'] + df_cost_revenue['USD_Domestic_Gross']
print(df_cost_revenue["total_revenue"].loc[df_cost_revenue["USD_Production_Budget"].idxmax()])
print(df_cost_revenue["total_revenue"].loc[df_cost_revenue["USD_Production_Budget"].idxmin()])

# How many films grossed $0 domestically (i.e., in the United States)?
# What were the highest budget films that grossed nothing?
# print(df_cost_revenue[df_cost_revenue["USD_Domestic_Gross"] == 0].count()["USD_Domestic_Gross"])
# print(df_cost_revenue[df_cost_revenue["total_revenue"] == 0].sort_values("USD_Production_Budget", ascending=False))

# How many films grossed $0 worldwide?
# What are the highest budget films that had no revenue internationally (i.e., the biggest flops)?
# print(df_cost_revenue[df_cost_revenue["total_revenue"] == 0].count()["total_revenue"])

# Filter on Multiple Conditions
x = df_cost_revenue.loc[(df_cost_revenue["USD_Domestic_Gross"] == 0) & (df_cost_revenue["USD_Worldwide_Gross"] != 0)]
print(x)
international_releases = df_cost_revenue.query('USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0')
print(f'Number of international releases: {len(international_releases)}')
print(international_releases)

# Identify which films were not released yet as of the time of data collection (May 1st, 2018).

scrape_date = pd.Timestamp("2018-05-01")
unreleased_movies = df_cost_revenue[df_cost_revenue["Release_Date"] > scrape_date]
print(unreleased_movies)
data_clean = df_cost_revenue.drop(unreleased_movies.index)

#  what is the true percentage of films where the costs exceed the worldwide gross revenue?
money_losing = data_clean.loc[data_clean.USD_Production_Budget > data_clean.USD_Worldwide_Gross]
print((len(money_losing) / len(data_clean)) * 100)
# option 2
money_losing = data_clean.query('USD_Production_Budget > USD_Worldwide_Gross')
print((money_losing.shape[0] / data_clean.shape[0]) * 100)

print((money_losing.count()["USD_Production_Budget"] / data_clean.count()["USD_Production_Budget"]) * 100)

# Seaborn plots
plt.figure(figsize=(8, 4), dpi=200)
"""
# set styling on a single chart
with sns.axes_style('whitegrid'):
    ax = sns.scatterplot(data=data_clean,
                         x='USD_Production_Budget',
                         y='USD_Worldwide_Gross',
                         hue='USD_Worldwide_Gross',
                         size='USD_Worldwide_Gross')

    ax.set(ylim=(0, 3000000000),
           xlim=(0, 450000000),
           ylabel='Revenue in $ billions',
           xlabel='Budget in $100 millions')

#plt.show()
"""
"""
with sns.axes_style("darkgrid"):
    ax = sns.scatterplot(data=data_clean,
                         x='Release_Date',
                         y='USD_Production_Budget',
                         hue='USD_Worldwide_Gross',
                         size='USD_Worldwide_Gross', )

    ax.set(ylim=(0, 450000000),
           xlim=(data_clean.Release_Date.min(), data_clean.Release_Date.max()),
           xlabel='Year',
           ylabel='Budget in $100 millions')

plt.show()
"""
dt_index = pd.DatetimeIndex(data_clean["Release_Date"])
years = dt_index.year
decades = (years // 10) * 10
data_clean['Decade'] = decades
df_old_films = data_clean[data_clean['Decade'] <= 1960]
df_new_films = data_clean[data_clean['Decade'] > 1960]

print(df_new_films.shape[0])
print(len(df_old_films))

plt.figure(figsize=(8, 4), dpi=200)
"""
with sns.axes_style("whitegrid"):
    sns.regplot(data=df_old_films,
                x='USD_Production_Budget',
                y='USD_Worldwide_Gross',
                scatter_kws={'alpha': 0.4},
                line_kws={'color': 'black'})

plt.show()
"""

plt.figure(figsize=(8, 4), dpi=200)
with sns.axes_style('darkgrid'):
    ax = sns.regplot(data=df_new_films,
                     x='USD_Production_Budget',
                     y='USD_Worldwide_Gross',
                     color='#2f4b7c',
                     scatter_kws={'alpha': 0.3},
                     line_kws={'color': '#ff7c43'})

    ax.set(ylim=(0, 3000000000),
           xlim=(0, 450000000),
           ylabel='Revenue in $ billions',
           xlabel='Budget in $100 millions')

# plt.show()

regression = LinearRegression()
# Explanatory Variable(s) or Feature(s)
X = pd.DataFrame(df_new_films, columns=['USD_Production_Budget'])
# Response Variable or Target
y = pd.DataFrame(df_new_films, columns=['USD_Worldwide_Gross'])
# Find the best-fit line
regression.fit(X, y)
