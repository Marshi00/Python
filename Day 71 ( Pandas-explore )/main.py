"""
Use .head(), .tail(), .shape and .columns to explore your DataFrame and find out the number of rows
 and columns as well as the column names.

Look for NaN (not a number) values with .findna() and consider using .dropna() to clean up your DataFrame.

You can access entire columns of a DataFrame using the square bracket notation: df['column name'] or
 df[['column name 1', 'column name 2', 'column name 3']]

You can access individual cells in a DataFrame by chaining square brackets df['column name'][index] or
 using df['column name'].loc[index]

The largest and smallest values, as well as their positions, can be found with methods like
 .max(), .min(), .idxmax() and .idxmin()

You can sort the DataFrame with .sort_values() and add new columns with .insert()

To create an Excel Style Pivot Table by grouping entries that belong to a particular category use
 the .groupby() method

"""

import pandas

data_frame = pandas.read_csv('salaries_by_college_major.csv')
pandas.options.display.float_format = '{:,.2f}'.format
# pandas.set_option('display.max_rows', None, 'display.max_columns', None)

# To see the number of rows and columns

# print(data_frame.shape)

# This will show us the first 5 rows of our dataframe.

# print(data_frame.head())

# We can access the column names directly with the columns attribute

# print(data_frame.columns)

# figure out if there are any missing or junk data in our dataframe. That way we can avoid problems later on.
# In this case, we're going to look for NaN (Not A Number) values in our dataframe. NAN values are blank cells or
# cells that contain strings instead of numbers

# print(data_frame.isna())
# print(data_frame.tail())


# Remove all rows wit NULL values from the DataFrame.

clean_data_frame = data_frame.dropna()
# print(clean_data_frame.tail())

# access a particular column from a data frame
# print(clean_data_frame['Starting Median Salary'])

# highest Value
# print(clean_data_frame['Starting Median Salary'].max())

# index of highest value
# print(clean_data_frame['Starting Median Salary'].idxmax())

# see the name of  corresponds to that particular row
# print(clean_data_frame['Undergraduate Major'].loc[43])
# print(clean_data_frame['Undergraduate Major'][43])

# retrieve an entire row
# print(clean_data_frame.loc[43])

# lowest Value
# print(clean_data_frame['Starting Median Salary'].min())

# index of the lowest value
# print(clean_data_frame['Starting Median Salary'].idxmin())
# print(clean_data_frame.loc[49])

# The Highest Mid-Career Salary
# print(clean_data_frame['Mid-Career Median Salary'].max())
# print(f"Index for the max mid career salary: {clean_data_frame['Mid-Career Median Salary'].idxmax()}")
# print(clean_data_frame['Undergraduate Major'][8])

# The Lowest Starting and Mid-Career Salary
# print(clean_data_frame['Starting Median Salary'].min())
# print(clean_data_frame['Undergraduate Major'].loc[clean_data_frame['Starting Median Salary'].idxmin()])

# the lowest mid-career salary
# print(clean_data_frame.loc[clean_data_frame['Mid-Career Median Salary'].idxmin()])

# making column from difference on high and mid-salary & insert 2 data frame
salary_spread_column = clean_data_frame['Mid-Career 90th Percentile Salary'] \
    .subtract(clean_data_frame['Mid-Career 10th Percentile Salary'])
clean_data_frame.insert(1, "Salary Spread", salary_spread_column)
# print(clean_data_frame.to_string())

# Sorting by the Lowest Spread
low_risk = clean_data_frame.sort_values('Salary Spread')

# print(low_risk[['Undergraduate Major', 'Salary Spread']].head())

# Sorting by the highest Spread
high_risk = clean_data_frame.sort_values(by='Salary Spread', ascending=False)
high_risk[['Undergraduate Major', 'Salary Spread']].head()
# print(high_risk[['Undergraduate Major', 'Salary Spread']].head())

# degrees with the highest potential
highest_potential = clean_data_frame.sort_values(by='Mid-Career 90th Percentile Salary', ascending=False)
# print(highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head())

# count how many majors we have in each category
# print(clean_data_frame.groupby('Group').count())

# the average salary by group
print(clean_data_frame.groupby('Group').mean()[["Starting Median Salary", "Mid-Career 90th Percentile Salary"]])