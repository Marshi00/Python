"""
used .groupby() to explore the number of posts and entries per programming language

converted strings to Datetime objects with to_datetime() for easier plotting

reshaped our DataFrame by converting categories to columns using .pivot()

used .count() and isna().values.any() to look for NaN values in our DataFrame, which we then
 replaced using .fillna()

created (multiple) line charts using .plot() with a for-loop

styled our charts by changing the size, the labels, and the upper and lower bounds of our axis.

added a legend to tell apart which line is which by colour

smoothed out our time-series observations with .rolling().mean() and plotted them to better
 identify trends over time.
"""


# Import Statements
import pandas
import matplotlib.pyplot as plt

# Data Exploration
# Read the .csv file and store it in a Pandas dataframe & change header name
data_frame = pandas.read_csv(filepath_or_buffer='QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
pandas.options.display.float_format = '{:,.2f}'.format

# Examine the first 5 rows and the last 5 rows of the dataframe
# print(data_frame.head())

# Check how many rows and how many columns there are. What are the dimensions of the dataframe
# print(data_frame.shape)

# Count the number of entries in each column.
# print(data_frame.count())

# Count how many months of data exist per programming language
# print(data_frame.groupby("TAG").count())

# Calculate the total number of post per language
# print(data_frame.groupby("TAG").sum()["POSTS"])

"""
# print(data_frame.groupby("TAG").count()["POSTS"].idxmax())
# data_frame.groupby("TAG").count().loc["c"]
# print(data_frame.groupby("TAG").count())
"""

# Selecting an Individual Cell
# print(data_frame["DATE"])

# converting string to datetime objects
data_frame["DATE"] = pandas.to_datetime(data_frame["DATE"])
# print(data_frame["DATE"])

# Reshaping data frame
reshaped_data_frame = data_frame.pivot(index="DATE", columns="TAG", values="POSTS")
# print(reshaped_data_frame.shape)
# print(reshaped_data_frame.columns)

# Count the number of entries per column
# print(reshaped_data_frame.count())

#  substitute the number 0 for each NaN value
reshaped_data_frame.fillna(0, inplace=True)
# print(reshaped_data_frame)

# check if there are any NaN values left in the entire DataFrame
# print(reshaped_data_frame.isna().values.any())



#
# The window is number of observations that are averaged
roll_data_frame = reshaped_data_frame.rolling(window=6).mean()
#  resize our chart & fonts
plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
# add labels. Also, we're never going to get less than 0 posts, so let's set a lower limit of 0 for the y-axis
plt.xlabel("DATE", fontsize=14)
plt.ylabel("POSTS", fontsize=14)
plt.ylim(0, 35000)
# line chart for the popularity of a programming language

# plt.plot(reshaped_data_frame.index, reshaped_data_frame['python'])
# plt.plot(reshaped_data_frame.index, reshaped_data_frame['java'])

# plot all the programming languages on the same chart add a label for each line based on the column name
# (and make the lines thicker at the same time using linewidth
for column in roll_data_frame.columns:
    plt.plot(roll_data_frame.index, roll_data_frame[column],
             label=column, linewidth=3)

plt.legend(fontsize=16)
plt.show()
# reshaped_data_frame[column].name