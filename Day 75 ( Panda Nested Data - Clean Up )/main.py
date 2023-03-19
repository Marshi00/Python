"""
Pull a random sample from a DataFrame using .sample()

How to find duplicate entries with .duplicated() and .drop_duplicates()

How to convert string and object data types into numbers with .to_numeric()

How to use plotly to generate beautiful pie, donut, and bar charts as well as box and scatter plots
"""
# Import Statements
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Show numeric output in decimal format e.g., 2.15
pd.options.display.float_format = '{:,.2f}'.format

# Read Data set
df_apps = pd.read_csv('apps.csv')

# How many rows and columns does df_apps have? What are the column names?
# What does the data look like?
# Look at a random sample of 5 different rows with
# print(df_apps.shape)
# print(df_apps.columns)
# print(df_apps.sample())

# drop the cols that are not needed
df_apps.drop(["Last_Updated", "Android_Ver"], axis=1, inplace=True)
# print(df_apps.head())

# Remove nun values
# print(f'Missing values for data set?: {df_apps.isna().values.any()}')
# print(f'Missing values for data set?: {df_apps.isna().values.sum()}')
# df_apps.dropna(inplace=True)
df_apps_clean = df_apps.dropna()
# print(df_apps_clean.shape)
# print(f'Missing values for Tesla?: {df_apps.isna().values.any()}')
# print(f'Missing values for Tesla?: {df_apps.isna().values.sum()}')

# Remove duplicates
# print(f'duplicates values for data set?: {df_apps_clean.duplicated().values.any()}')
# print(f'duplicates values for data set?: {df_apps_clean.duplicated().values.sum()}')
df_apps_clean = df_apps_clean.drop_duplicates(subset=["App", "Type", "Price"])
# print(df_apps_clean.shape)
# print(f'duplicates values for data set?: {df_apps_clean.duplicated().values.any()}')
# print(f'duplicates values for data set?: {df_apps_clean.duplicated().values.sum()}')

#  highest rated
highest_rated = df_apps_clean.sort_values(by='Rating', ascending=False)
# print(highest_rated.head())

# the largest Android apps in the Google Play Store
highest_size = df_apps_clean.sort_values(by='Size_MBs', ascending=False)
# print(highest_rated.head())

# Which apps have the highest number of reviews? Are there any paid apps among the top 50
highest_reviews = df_apps_clean.sort_values(by='Reviews', ascending=False)
# print(highest_reviews.head(50))

# counting
ratings = df_apps_clean["Content_Rating"].value_counts()
# print(ratings)
"""
# Pie chat
fig = px.pie(labels=ratings.index,
             values=ratings.values,
             title="Content Rating",
             names=ratings.index,
             hole=0.6,
             )
fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent')

fig.show()
"""

# Check the datatype of the Installs column.
# print(type(df_apps_clean["Installs"].loc[21]))
# print(df_apps_clean["Installs"].describe())
# print(df_apps_clean["Installs"].info())


# Count the number of apps at each level of installations.
# print(df_apps_clean.groupby("Installs").count()["App"])

# Convert the number of installations (the Installs column) to a numeric data type.
# Hint: this is a 2-step process. You'll have to make sure you remove non-numeric characters first.
df_apps_clean["Installs"] = df_apps_clean["Installs"].astype(str).str.replace(",", "")
# print(df_apps_clean.groupby("Installs").count()["App"])
# print(df_apps_clean["Installs"].describe())
df_apps_clean["Installs"] = pd.to_numeric(df_apps_clean["Installs"])
df_apps_clean["Installs"] = pd.to_numeric(df_apps_clean["Installs"])
# print(df_apps_clean["Installs"].describe())

# Convert the price column to numeric data.
# print(df_apps_clean["Price"].describe())
# print(df_apps_clean.groupby("Price").count()["App"])
df_apps_clean["Price"] = df_apps_clean["Price"].astype(str).str.replace("$", "")
# print(df_apps_clean.groupby("Price").count()["App"])
df_apps_clean["Price"] = pd.to_numeric(df_apps_clean["Price"])
# print(df_apps_clean.groupby("Price").count()["App"])
# print(df_apps_clean["Price"].describe())

# Then investigate the top 20 most expensive apps in the dataset.
highest_price = df_apps_clean.sort_values(by='Price', ascending=False)
# print(highest_price.head(20))

# Remove all apps that cost more than $250 from the df_apps_clean DataFrame.
df_apps_clean = df_apps_clean[df_apps_clean['Price'] < 250]
# print(df_apps_clean.sort_values('Price', ascending=False).head(5))

# Add a column called 'Revenue_Estimate' to the DataFrame.
# This column should hold the price of the app times the number of installs.
# What are the top 10 highest-grossing paid apps according to this estimate?
# Out of the top 10, how many are games?
df_apps_clean['Revenue_Estimate'] = df_apps_clean.Installs.mul(df_apps_clean.Price)
# print(df_apps_clean.sort_values('Revenue_Estimate', ascending=False)[:10])
# print(df_apps_clean.shape)

# find the number of different categories

# print(df_apps_clean["Category"].nunique())

# find the number of apps in each category
top10_category = df_apps_clean.Category.value_counts()[:10]
# print(df_apps_clean["Category"].value_counts()[:10])
bar = px.bar(x=top10_category.index,  # index = category name
             y=top10_category.values)

# bar.show()

# how often apps are downloaded in each category
category_installs = df_apps_clean.groupby("Category").agg({"Installs": pd.Series.sum})
category_installs.sort_values("Installs", ascending=True, inplace=True)

# horizontal bar chart
h_bar = px.bar(x=category_installs.Installs,
               y=category_installs.index,
               orientation='h',
               title='Category Popularity')

h_bar.update_layout(xaxis_title='Number of Downloads', yaxis_title='Category')
# h_bar.show()

# Create a DataFrame that has the number of apps in one column and the number of installs in another
""" 
# Option 1 
cat_number  = df_apps_clean.groupby("Category").agg({"Installs": pd.Series.count})
cat_merged_df = pd.merge(cat_number, category_installs, on='Category', how="inner")
print(f'The dimensions of the DataFrame are: {cat_merged_df.shape}')
# print(cat_merged_df)
cat_merged_df.rename(columns={"Installs_x": "App", "Installs_y": "Installs"}, inplace=True)
print(cat_merged_df)
cat_merged_df.sort_values('Installs', ascending=False)
"""
# option 2
cat_merged_df = df_apps_clean.groupby('Category').agg({'App': "count", 'Installs': "sum"})\
    .sort_values("Installs", ascending=False)

# print(cat_merged_df)
scatter = px.scatter(cat_merged_df,  # data
                     x='App',  # column name
                     y='Installs',
                     title='Category Concentration',
                     size='App',
                     hover_name=cat_merged_df.index,
                     color='Installs')

scatter.update_layout(xaxis_title="Number of Apps (Lower=More Concentrated)",
                      yaxis_title="Installs",
                      yaxis=dict(type='log'))

# scatter.show()
#print(df_apps_clean["Genres"].value_counts())
#print(df_apps_clean["Genres"].nunique())


# Extracting Nested Column Data using .stack()
# Split the strings on the semi-colon and then .stack them.
stack = df_apps_clean.Genres.str.split(';', expand=True).stack()
# print(stack)
# print(f'We now have a single column with shape: {stack.shape}')
num_genres = stack.value_counts()
# print(f'Number of genres: {len(num_genres)}')

bar_2 = px.bar(x=num_genres.index[:15],  # index = category name
             y=num_genres.values[:15],  # count
             title='Top Genres',
             hover_name=num_genres.index[:15],
             color=num_genres.values[:15],
             color_continuous_scale='Agsunset')

bar_2.update_layout(xaxis_title='Genre',
                  yaxis_title='Number of Apps',
                  coloraxis_showscale=False)

# bar_2.show()

# he split is between free and paid apps
# print(df_apps_clean["Type"].value_counts())
df_free_vs_paid = df_apps_clean.groupby(["Category", "Type"], as_index=False).agg({'App': pd.Series.count})
# print(df_free_vs_paid.head())

g_bar = px.bar(df_free_vs_paid,
               x='Category',
               y='App',
               title='Free vs Paid Apps by Category',
               color='Type',
               barmode='group')

g_bar.update_layout(xaxis_title='Category',
                    yaxis_title='Number of Apps',
                    xaxis={'categoryorder': 'total descending'},
                    yaxis=dict(type='log'))

# g_bar.show()

df_paid_apps = df_apps_clean[df_apps_clean['Type'] == 'Paid']
box = px.box(df_paid_apps,
             x='Category',
             y='Revenue_Estimate',
             title='How Much Can Paid Apps Earn?')

box.update_layout(xaxis_title='Category',
                  yaxis_title='Paid App Ballpark Revenue',
                  xaxis={'categoryorder': 'min ascending'},
                  yaxis=dict(type='log'))

# box.show()
print(df_paid_apps.Price.median())
new_df =df_paid_apps.groupby("Category", as_index=False).agg({'Price': pd.Series.median})
print(new_df)
box = px.box(df_paid_apps,
             x='Category',
             y="Price",
             title='Price per Category')

box.update_layout(xaxis_title='Category',
                  yaxis_title='Paid App Price',
                  xaxis={'categoryorder': 'max descending'},
                  yaxis=dict(type='log'))

box.show()