"""
How to uncover and investigate NaN values.

How to convert objects and string data types to numbers.

Creating donut and bar charts with plotly.

Create a rolling average to smooth out time-series data and show a trend.

How to use .value_counts(), .groupby(), .merge(), .sort_values() and .agg().



In addition, we learned many new things too. We looked at how to:

Create a Choropleth to display data on a map.

Create bar charts showing different segments of the data with plotly.

Create Sunburst charts with plotly.

Use Seaborn's .lmplot() and show best-fit lines across multiple categories using the row, hue, and lowess parameters.

Understand how a different picture emerges when looking at the same data in different ways (e.g., box plots vs a time series analysis).

See the distribution of our data and visualise descriptive statistics with the help of a histogram in Seaborn.
"""


import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

pd.options.display.float_format = '{:,.2f}'.format
df_data = pd.read_csv('nobel_prize_data.csv')

"""
# Explore the data
print(df_data.shape)
print(df_data.columns)
print(df_data.head())
print(df_data.sample())
"""
# Clean up
print(f"Any nun values? {df_data.isna().values.any()}\n"
      f"There are {df_data.isna().values.sum()} nun values\n"
      f"they are as follows : \n {df_data.isna().sum()}")
print(f"Any duplicate values? {df_data.duplicated(subset=['prize', 'full_name', 'year', 'motivation']).values.any()}\n"
      f"There are {df_data.duplicated(subset=['prize', 'full_name', 'year', 'motivation']).values.sum()}"
      f" duplicate values \n"
      f" they are as follows : \n {df_data.duplicated(subset=['prize', 'full_name', 'year', 'motivation']).sum()}\n ")

col_subset = ['year', 'category', 'laureate_type',
              'birth_date', 'full_name', 'organization_name']
print(df_data.loc[df_data.birth_date.isna()][col_subset])
col_subset_2 = ['year', 'category', 'laureate_type', 'full_name', 'organization_name']
print(df_data.loc[df_data.organization_name.isna()][col_subset_2])

# Type check
for col in df_data.columns:
    print(f"\nThe Column name is : {col}\nType of first itme in this col is : {type(df_data[col][0])}\n"
          f"The first item in this col is : {df_data[col][0]}\n")
print(df_data.info())
# Type conversion
df_data["birth_date"] = pd.to_datetime(df_data["birth_date"])

separated_values = df_data["prize_share"].astype(str).str.split('/', expand=True)
numerator = pd.to_numeric(separated_values[0])
denominator = pd.to_numeric(separated_values[1])
df_data['share_pct'] = (numerator / denominator) * 100
print(df_data["share_pct"])
print(df_data.info())
print(df_data["sex"].value_counts())
# Percent of woman vs man
biology = df_data.sex.value_counts()
fig = px.pie(labels=biology.index,
             values=biology.values,
             title="Percentage of Male vs. Female Winners",
             names=biology.index,
             hole=0.4, )

fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent')

# fig.show()

# first 3 woman to win the prize
# print(df_data[df_data["sex"] == "Female"].sort_values("year", ascending=True)[:3])

# The Repeat Winners
# option 1
is_winner2 = df_data.duplicated(subset=['full_name'], keep=False)
multiple_winners = df_data[is_winner2]

# option 2
is_winner = df_data[df_data.duplicated(subset="full_name", keep=False)]

print(is_winner["full_name"].unique())
print(is_winner["full_name"].value_counts())

# Number of Prizes per Category
prizes_per_category = df_data.category.value_counts()
print(df_data["category"].value_counts())
print(df_data["category"].nunique())
v_bar = px.bar(
    x=prizes_per_category.index,
    y=prizes_per_category.values,
    color=prizes_per_category.values,
    color_continuous_scale='Aggrnyl',
    title='Number of Prizes Awarded per Category')

v_bar.update_layout(xaxis_title='Nobel Prize Category',
                    coloraxis_showscale=False,
                    yaxis_title='Number of Prizes')
# v_bar.show()

# Economics Prize
print(df_data[df_data.category == 'Economics'].sort_values('year'))
print("############")
# Male and Female Winners by Category
print(df_data.groupby(["category", "sex"], as_index=True).agg({"prize": pd.Series.count}))

cat_men_women = df_data.groupby(['category', 'sex'],
                                as_index=False).agg({'prize': pd.Series.count})
cat_men_women.sort_values('prize', ascending=False, inplace=True)
v_bar_split = px.bar(x=cat_men_women.category,
                     y=cat_men_women.prize,
                     color=cat_men_women.sex,
                     title='Number of Prizes Awarded per Category split by Men and Women')

v_bar_split.update_layout(xaxis_title='Nobel Prize Category',
                          yaxis_title='Number of Prizes')
# v_bar_split.show()

print("GGGGGGGGGGGGGGG")
# Count the number of prizes awarded every year.
print(df_data.groupby("year", as_index=False).agg({"prize": pd.Series.count}))
prize_per_year = df_data.groupby(by='year').count().prize
print("###############")
print(prize_per_year)
moving_average = prize_per_year.rolling(window=5).mean()
plt.figure(figsize=(16, 8), dpi=200)
plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks=np.arange(1900, 2021, step=5),
           fontsize=14,
           rotation=45)

ax = plt.gca()  # get current axis
ax.set_xlim(1900, 2020)

ax.scatter(x=prize_per_year.index,
           y=prize_per_year.values,
           c='dodgerblue',
           alpha=0.7,
           s=100, )

ax.plot(prize_per_year.index,
        moving_average.values,
        c='crimson',
        linewidth=3, )

# plt.show()
yearly_avg_share = df_data.groupby(by='year').agg({'share_pct': pd.Series.mean})
share_moving_average = yearly_avg_share.rolling(window=5).mean()
plt.figure(figsize=(16, 8), dpi=200)
plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks=np.arange(1900, 2021, step=5),
           fontsize=14,
           rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()  # create second y-axis
ax1.set_xlim(1900, 2020)

ax1.scatter(x=prize_per_year.index,
            y=prize_per_year.values,
            c='dodgerblue',
            alpha=0.7,
            s=100, )

ax1.plot(prize_per_year.index,
         moving_average.values,
         c='crimson',
         linewidth=3, )

# Adding prize share plot on second axis
ax2.plot(prize_per_year.index,
         share_moving_average.values,
         c='grey',
         linewidth=3, )

# plt.show()
plt.figure(figsize=(16, 8), dpi=200)
plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks=np.arange(1900, 2021, step=5),
           fontsize=14,
           rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_xlim(1900, 2020)

# Can invert axis
ax2.invert_yaxis()

ax1.scatter(x=prize_per_year.index,
            y=prize_per_year.values,
            c='dodgerblue',
            alpha=0.7,
            s=100, )

ax1.plot(prize_per_year.index,
         moving_average.values,
         c='crimson',
         linewidth=3, )

ax2.plot(prize_per_year.index,
         share_moving_average.values,
         c='grey',
         linewidth=3, )

# plt.show()

top_countries = df_data.groupby('birth_country_current', as_index=False).agg({'prize': pd.Series.count})
top_countries.sort_values(by='prize', inplace=True)
top20_countries = top_countries[-20:]
print(top20_countries)
h_bar = px.bar(x=top20_countries.prize,
               y=top20_countries.birth_country_current,
               orientation='h',
               color=top20_countries.prize,
               color_continuous_scale='Viridis',
               title='Top 20 Countries by Number of Prizes')

h_bar.update_layout(xaxis_title='Number of Prizes',
                    yaxis_title='Country',
                    coloraxis_showscale=False)
# h_bar.show()

df_countries = df_data.groupby(['birth_country_current', 'ISO'],
                               as_index=False).agg({'prize': pd.Series.count})
df_countries.sort_values('prize', ascending=False)
print(df_countries.sort_values('prize', ascending=False))
world_map = px.choropleth(df_countries,
                          locations='ISO',
                          color='prize',
                          hover_name='birth_country_current',
                          color_continuous_scale=px.colors.sequential.matter)

world_map.update_layout(coloraxis_showscale=True, )

# world_map.show()

#  The category breakdown by country

cat_country = df_data.groupby(['birth_country_current', 'category'], as_index=False).agg({'prize': pd.Series.count})
cat_country.sort_values(by='prize', ascending=False, inplace=True)
print("GGGGGGGGG")
print(cat_country)
print("WWWWWWWWW")
print(top20_countries)
print("RRRRRR")
merged_df = pd.merge(cat_country, top20_countries, on="birth_country_current")
merged_df.rename(columns={"prize_x": "cat_prize", "prize_y": "total_prize"}, inplace=True)
print(merged_df)
merged_df.sort_values(by='total_prize', inplace=True)
print(merged_df)
cat_cntry_bar = px.bar(x=merged_df.cat_prize,
                       y=merged_df.birth_country_current,
                       color=merged_df.category,
                       orientation='h',
                       title='Top 20 Countries by Number of Prizes and Category')

cat_cntry_bar.update_layout(xaxis_title='Number of Prizes',
                            yaxis_title='Country')
# cat_cntry_bar.show()

# Country Prizes over Time
prize_by_year = df_data.groupby(['birth_country_current', 'year'], as_index=False).agg({"prize": pd.Series.count})
print("222222222")
print(prize_by_year)
prize_by_year = prize_by_year.sort_values('year', ascending=True)
print(333333)
print(prize_by_year)
print(4444444)
cumulative_prizes = prize_by_year.groupby(by=['birth_country_current',
                                              'year']).sum().groupby(level=[0]).cumsum()
print(cumulative_prizes)
print("huhweqfqw")
cumulative_prizes.reset_index(inplace=True)
print(cumulative_prizes)
l_chart = px.line(cumulative_prizes,
                  x='year',
                  y='prize',
                  color='birth_country_current',
                  hover_name='birth_country_current')

l_chart.update_layout(xaxis_title='Year',
                      yaxis_title='Number of Prizes')

# l_chart.show()
"""
print(111111)
print(prize_by_year.groupby(by=['birth_country_current',
                                              'year']).head())
print(222222222)
print(prize_by_year.groupby(by=['birth_country_current',
                                              'year']).sum())

print(3333333333333333)
print(prize_by_year.groupby(by=['birth_country_current',
                                              'year']).sum().groupby(level=[0]).head())

print(4444444444444444444)
print(prize_by_year.groupby(by=['birth_country_current',
                                              'year']).sum().groupby(level=[0]).cumsum())
"""
# The Top Research Organisations
top20_orgs = df_data[df_data["laureate_type"] == "Organization"]
print(top20_orgs["organization_name"].value_counts())
