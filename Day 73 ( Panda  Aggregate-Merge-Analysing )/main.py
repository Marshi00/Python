"""
use HTML Markdown in Notebooks, such as section headings # and how to embed images with the <img> tag.

combine the groupby() and count() functions to aggregate data

use the .value_counts() function

slice DataFrames using the square bracket notation e.g., df[:-2] or df[:10]

use the .agg() function to run an operation on a particular column

rename() columns of DataFrames

create a line chart with two separate axes to visualise data that have different scales.

create a scatter plot in Matplotlib

work with tables in a relational database by using primary and foreign keys

.merge() DataFrames along a particular column

create a bar chart with Matplotlib
"""
# Import Statements
import pandas
import matplotlib.pyplot as plt

# Read the .csv file and store it in a Pandas dataframe & change header name
import pandas as pd

data_frame_colors = pandas.read_csv(filepath_or_buffer='data/colors.csv')

# Check how many rows and how many columns there are. What are the dimensions of the dataframe
# print(data_frame_colors.shape)
# print(data_frame_colors.head())


# Count the number of entries in each column.
# print(data_frame_colors.count())

# the total number of unique colours
# print(data_frame_colors.groupby("rgb").count())
# print(data_frame_colors.nunique(axis="rows"))
# print(data_frame_colors['name'].nunique())


# Find the number of transparent colours
# print(data_frame_colors.groupby("is_trans").count())
# print(data_frame_colors["is_trans"].value_counts())

# sets data sets
data_frame_sets = pandas.read_csv(filepath_or_buffer='data/sets.csv')
# print(data_frame_sets.head())
# In which year were the first LEGO sets released and what were these sets called?

# 1
# print(data_frame_sets["year"].idxmin())
# print(data_frame_sets[['name', 'year']].loc[data_frame_sets["year"].idxmin()])

# 2
# print(data_frame_sets.sort_values("year").head())


# here we are filtering our DataFrame on a condition
# How many different products did the LEGO company sell in their first year of operation?
# print(data_frame_sets[data_frame_sets["year"] == 1949])

# What are the top 5 LEGO sets with the most number of parts?
# print(data_frame_sets.sort_values(by="num_parts", ascending=False).head())
data_frame_sets_by_year = data_frame_sets.groupby("year").count()
# print(data_frame_sets_by_year.head())
"""
plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel("YEAR", fontsize=14)
plt.ylabel("Set Numbers", fontsize=14)
plt.ylim(0, 1000)
plt.plot(data_frame_sets_by_year.index[:-2], data_frame_sets_by_year["set_num"][:-2])
plt.show()
"""
# group the data by year and then count the number of unique theme_ids for that year
themes_by_year = data_frame_sets.groupby("year").agg({"theme_id": pandas.Series.nunique})
# print(themes_by_year)
themes_by_year.rename(columns={"theme_id": "nr_unique_themes"}, inplace=True)
# print(themes_by_year)

# Create a line plot of the number of themes released year-on-year.
# Only include the full calendar years in the dataset (1949 to 2019)
"""
ax1 = plt.gca() # get current axes
ax2 = ax1.twinx()
plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
ax1.plot(data_frame_sets_by_year.index[:-2], data_frame_sets_by_year["set_num"][:-2], color="g")
ax2.plot(themes_by_year.index[:-2], themes_by_year["nr_unique_themes"][:-2], color="b")
ax1.set_xlabel("YEAR", fontsize=14)
ax1.set_ylabel("Set Numbers", fontsize=14, color="green")
ax2.set_ylabel("Unique Themes", fontsize=14, color="blue")
plt.show()
"""

# Create a Pandas Series called parts_per_set that has the year as the index and
# contains the average number of parts per LEGO set in that year
average_parts_year = data_frame_sets.groupby("year").agg({"num_parts": pandas.Series.mean})
# print(average_parts_year)
average_parts_year.rename(columns={"num_parts": "average_num_parts"}, inplace=True)
# print(average_parts_year)
"""
plt.scatter(average_parts_year.index[:-2], average_parts_year["average_num_parts"][:-2])
plt.show()
"""

# To count the number of sets per Theme
set_theme_count = data_frame_sets["theme_id"].value_counts()
# print(set_theme_count.head())

#  Exploring the themes.csv
data_frame_themes = pandas.read_csv(filepath_or_buffer='data/themes.csv')
# print(data_frame_themes.head())
# print(data_frame_themes[data_frame_themes["name"] == "Star Wars"])

# convert this Pandas Series into a Pandas DataFrame.
set_theme_count = pandas.DataFrame({"id": set_theme_count.index,
                                    "set_count": set_theme_count.values})
# print(set_theme_count)
merge_data_frame = pandas.merge(set_theme_count, data_frame_themes, on="id")
print(merge_data_frame)
plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
plt.bar(merge_data_frame["name"][:10], merge_data_frame["set_count"][:10])
plt.show()