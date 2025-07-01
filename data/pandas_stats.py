import pandas as pd
import os

file_path = 'data/2024_fb_ads_president_scored_anon.csv'
df = pd.read_csv(file_path)

numeric_cols = ['estimated_audience_size', 'estimated_impressions', 'estimated_spend']

print("\nMissing Value Count Per Column for Numerical cols:")
print(df[numeric_cols].isnull().sum())

print("\nDescriptive Statistics for Numeric Columns")
print(df[numeric_cols].describe())
    #Descriptive Stats for categorical columns
print("\nUnique Value Counts (Categorical Columns)")
for col in df.columns:
    if df[col].dtype == 'object' or df[col].dtype.name == 'category':
        print(f"\nColumn: {col}")
        print(df[col].value_counts(dropna=False).head(10))

"""   #Grouped by page_id
output_file_for_pageid = "grouped_by_page.csv"
print("\nGrouped Statistics by 'page_id'")
grouped_by_page = df.groupby('page_id')[numeric_cols].describe().head(3)
print(grouped_by_page)
    # Save to CSV as I am not able to see the whole output for evaluation lateer
grouped_by_page.to_csv(output_file_for_pageid)
print(f"\nGrouped statistics saved to: {os.path.abspath(output_file_for_pageid)}")

    #Grouped by ad_id
top3_df = df.head(3)
output_file_for_adid = "grouped_by_ad.csv"
print("\nGrouped Statistics by 'ad_id'")
grouped_by_ad = top3_df.groupby('ad_id')[numeric_cols].describe()
print(grouped_by_ad)
    # Save to CSV as I am not able to see the whole output for evaluation lateer
grouped_by_ad.to_csv(output_file_for_adid)
print(f"\nGrouped statistics saved to: {os.path.abspath(output_file_for_adid)}")

    # Grouped Statistics by 'page_id' and 'ad_id'
if 'ad_id' in df.columns:
    first3_df = df.head(3)
    output_file_for_pagead = "grouped_by_pagead.csv"
    print("\nGrouped Statistics by 'page_id' and 'ad_id'")
    grouped_by_page_ad = first3_df.groupby(['page_id', 'ad_id']).describe()
    print(grouped_by_page_ad)

    grouped_by_page_ad.to_csv(output_file_for_pagead)
    print(f"\nGrouped statistics saved to: {os.path.abspath(output_file_for_pagead)}")


##2nd dataset
##Doing same for fb_posts dataset
file_path = 'data/2024_fb_posts_president_scored_anon.csv'
df = pd.read_csv(file_path)
numeric_cols = ['Total Interactions', 'Likes', 'Comments', 'Shares', 'Love', 'Wow', 'Haha', 'Sad', 'Angry', 'Care', 'Post Views', 'Total Views', 'Total Views', 'Total Views For All Crossposts']

print("\nDescriptive Statistics for Numeric Columns")
print(df[numeric_cols].describe())
    #Descriptive Stats for categorical columns
print("\nUnique Value Counts (Categorical Columns)")
for col in df.columns:
    if df[col].dtype == 'object' or df[col].dtype.name == 'category':
        print(f"\nColumn: {col}")
        print(df[col].value_counts(dropna=False).head(5))


    #Grouped by Facebook_Id
output_file_for_fbid = "grouped_by_fbid.csv"
print("\nGrouped Statistics by 'Facebook_Id'")
grouped_by_fbid = df.groupby('Facebook_Id')[numeric_cols].describe().head(3)
print(grouped_by_fbid)

grouped_by_fbid.to_csv(output_file_for_fbid)
print(f"\nGrouped statistics saved to: {os.path.abspath(output_file_for_fbid)}")


    #Grouped by post_id
top3_df = df.head(3)
output_file_for_postid = "grouped_by_post.csv"
print("\nGrouped Statistics by 'post_id'")
grouped_by_post = top3_df.groupby('post_id')[numeric_cols].describe()
print(grouped_by_post)

grouped_by_post.to_csv(output_file_for_postid)
print(f"\nGrouped statistics saved to: {os.path.abspath(output_file_for_postid)}")


    # Grouped Statistics by # FB and Post
if 'post_id' in df.columns:
    first3_df = df.head(3)
    output_file_for_fbpost = "grouped_by_fbpost.csv"
    print("\nGrouped Statistics by 'Facebook_Id' and 'post_id'")
    grouped_by_fbpost = first3_df.groupby(['Facebook_Id', 'post_id']).describe()
    print(grouped_by_fbpost)

    grouped_by_fbpost.to_csv(output_file_for_fbpost)
    print(f"\nGrouped statistics saved to: {os.path.abspath(output_file_for_fbpost)}")


##3rd dataset
##Doing same for tw_posts dataset
file_path = 'data/2024_tw_posts_president_scored_anon.csv'
df = pd.read_csv(file_path)
numeric_cols = ['retweetCount', 'replyCount', 'likeCount', 'quoteCount', 'viewCount', 'bookmarkCount']

print("\nDescriptive Statistics for Numeric Columns")
print(df[numeric_cols].describe())
    #Descriptive Stats for categorical columns
print("\nUnique Value Counts (Categorical Columns)")
for col in df.columns:
    if df[col].dtype == 'object' or df[col].dtype.name == 'category':
        print(f"\nColumn: {col}")
        print(df[col].value_counts(dropna=False).head(5))


    #Grouped by twitter Id
top3_df = df.head(3)
output_file_for_id = "grouped_by_id.csv"
print("\nGrouped Statistics by 'id'")
grouped_by_id = df.groupby('id')[numeric_cols].describe()
print(grouped_by_id)

grouped_by_id.to_csv(output_file_for_id)
print(f"\nGrouped statistics saved to: {os.path.abspath(output_file_for_id)}")


    #Grouped by url
top3_df = df.head(3)
output_file_for_url = "grouped_by_url.csv"
print("\nGrouped Statistics by 'url'")
grouped_by_url = top3_df.groupby('url')[numeric_cols].describe()
print(grouped_by_url)

grouped_by_url.to_csv(output_file_for_url)
print(f"\nGrouped statistics saved to: {os.path.abspath(output_file_for_url)}")


    # Grouped Statistics by # id and url
if 'url' in df.columns:
    first3_df = df.head(3)
    output_file_for_idurl = "grouped_by_idurl.csv"
    print("\nGrouped Statistics by 'id' and 'url'")
    grouped_by_idurl = first3_df.groupby(['id', 'url']).describe()
    print(grouped_by_idurl)

    grouped_by_idurl.to_csv(output_file_for_idurl)
    print(f"\nGrouped statistics saved to: {os.path.abspath(output_file_for_idurl)}")"""