import polars as pl
df = pl.read_csv("data/2024_fb_ads_president_scored_anon.csv")

num_cols = ['estimated_audience_size', 'estimated_impressions', 'estimated_spend']
cat_cols = [col for col in df.columns if col not in num_cols]

for col in num_cols:
    print(f"\n{col} (Null values in num_cols)")
    null_count = df.select(pl.col(col).null_count().alias(f"{col}_nulls"))
    print(null_count)

for col in cat_cols:
    print(f"\n{col} (Categorical Summary)")
    print(df.select([
        pl.col(col).n_unique().alias("unique_count")
    ]))

print("\nDescriptive Stats (Numeric Columns)")
stats = df.select([
    pl.col(col).count().alias(f"{col}_count") for col in num_cols
] + [
    pl.col(col).mean().alias(f"{col}_mean") for col in num_cols
] + [
    pl.col(col).std().alias(f"{col}_std") for col in num_cols
] + [
    pl.col(col).min().alias(f"{col}_min") for col in num_cols
] + [
    pl.col(col).max().alias(f"{col}_max") for col in num_cols
])
print(stats.transpose(include_header=True))

"""# Group by page_id
if "page_id" in df.columns:
    print("\nGrouped by page_id (Summary)")
    grouped = df.group_by("page_id").agg([
        pl.col(col).count().alias(f"{col}_count") for col in num_cols
    ] + [
        pl.col(col).mean().alias(f"{col}_mean") for col in num_cols
    ] + [
        pl.col(col).median().alias(f"{col}_median") for col in num_cols
    ])
    print(grouped.head(3))

# Group by ad_id
if "ad_id" in df.columns:
    print("\nGrouped by ad_id (Summary)")
    grouped = df.group_by("ad_id").agg([
        pl.col(col).count().alias(f"{col}_count") for col in num_cols
    ] + [
        pl.col(col).mean().alias(f"{col}_mean") for col in num_cols
    ] + [
        pl.col(col).median().alias(f"{col}_median") for col in num_cols
    ])
    print(grouped.head(3))

# Grouped by page_id and ad_id
if "ad_id" in df.columns:
    grouped_mean = df.group_by(["page_id", "ad_id"]).agg([
        pl.col(col).mean().alias(f"{col}_mean") for col in num_cols
    ])
    print(grouped_mean.head(3))
    grouped_count = df.group_by(["page_id", "ad_id"]).agg([
        pl.count().alias("row_count")
    ])
    print(grouped_count.head(3))
    grouped_median = df.group_by(["page_id", "ad_id"]).agg([
        pl.col(col).median().alias(f"{col}_median") for col in num_cols
    ])
    print(grouped_median.head(3))


##Executing code for 2nd dataset
## fb_posts dataset
df = pl.read_csv("data/2024_fb_posts_president_scored_anon.csv")

##check for str dtypes as it will not count as numerical column
for name, dtype in zip(df.columns, df.dtypes):
    print(f"{name}: {dtype}")

num_cols = ['Likes', 'Comments', 'Shares', 'Love', 'Wow', 'Haha', 'Sad', 'Angry', 'Care', 'Post Views', 'Total Views', 'Total Views For All Crossposts']
cat_cols = [col for col in df.columns if col not in num_cols]

for col in cat_cols:
    print(f"\n=== {col} (Categorical Summary) ===")
    print(df.select([
        pl.col(col).n_unique().alias("unique_count")
    ]))

print("\nDescriptive Stats (Numeric Columns)")
stats = df.select([
    pl.col(col).count().alias(f"{col}_len") for col in num_cols
] + [
    pl.col(col).mean().alias(f"{col}_mean") for col in num_cols
] + [
    pl.col(col).std().alias(f"{col}_std") for col in num_cols
] + [
    pl.col(col).min().alias(f"{col}_min") for col in num_cols
] + [
    pl.col(col).max().alias(f"{col}_max") for col in num_cols
])
print(stats.transpose(include_header=True))

# Group by Facebook_Id
if "Facebook_Id" in df.columns:
    print("\nGrouped by Facebook_Id (Summary)")
    grouped = df.group_by("Facebook_Id").agg([
        pl.col(col).count().alias(f"{col}_len") for col in num_cols
    ] + [
        pl.col(col).mean().alias(f"{col}_mean") for col in num_cols
    ] + [
        pl.col(col).median().alias(f"{col}_median") for col in num_cols
    ])
    print(grouped.head(3))

# Group by post_id
if "post_id" in df.columns:
    print("\nGrouped by post_id (Summary)")
    grouped = df.group_by("post_id").agg([
        pl.col(col).count().alias(f"{col}_len") for col in num_cols
    ] + [
        pl.col(col).mean().alias(f"{col}_mean") for col in num_cols
    ] + [
        pl.col(col).median().alias(f"{col}_median") for col in num_cols
    ])
    print(grouped.head(3))

# Grouped by Facebook_Id and post_id
if "post_id" in df.columns:
    print("\nGrouped by Facebook Id , post id (Summary)")
    grouped_mean = df.group_by(["Facebook_Id", "post_id"]).agg([
        pl.col(col).mean().alias(f"{col}_mean") for col in num_cols
    ])
    print(grouped_mean.head(3))
    grouped_count = df.group_by(["Facebook_Id", "post_id"]).agg([
        pl.len().alias("row_count")
    ])
    print(grouped_count.head(3))
    grouped_median = df.group_by(["Facebook_Id", "post_id"]).agg([
        pl.col(col).median().alias(f"{col}_median") for col in num_cols
    ])
    print(grouped_median.head(3))


##Executing code for 3rd dataset
## tw_posts dataset
df = pl.read_csv("data/2024_tw_posts_president_scored_anon.csv")

for name, dtype in zip(df.columns, df.dtypes):
    print(f"{name}: {dtype}")

num_cols = ['retweetCount', 'replyCount', 'likeCount', 'quoteCount', 'viewCount', 'bookmarkCount']
cat_cols = [col for col in df.columns if col not in num_cols]

for col in cat_cols:
    print(f"\n{col} (Categorical Summary)")
    print(df.select([
        pl.col(col).n_unique().alias("unique_count")
    ]))

print("\nDescriptive Stats (Numeric Columns)")
stats = df.select([
    pl.col(col).count().alias(f"{col}_len") for col in num_cols
] + [
    pl.col(col).mean().alias(f"{col}_mean") for col in num_cols
] + [
    pl.col(col).std().alias(f"{col}_std") for col in num_cols
] + [
    pl.col(col).min().alias(f"{col}_min") for col in num_cols
] + [
    pl.col(col).max().alias(f"{col}_max") for col in num_cols
])
print(stats.transpose(include_header=True))

# Group by id
if "id" in df.columns:
    print("\nGrouped by id (Summary)")
    grouped = df.group_by("id").agg([
        pl.col(col).count().alias(f"{col}_len") for col in num_cols
    ] + [
        pl.col(col).mean().alias(f"{col}_mean") for col in num_cols
    ] + [
        pl.col(col).median().alias(f"{col}_median") for col in num_cols
    ])
    print(grouped.head(3))

# Group by url
if "url" in df.columns:
    print("\nGrouped by url (Summary)")
    grouped = df.group_by("url").agg([
        pl.col(col).count().alias(f"{col}_len") for col in num_cols
    ] + [
        pl.col(col).mean().alias(f"{col}_mean") for col in num_cols
    ] + [
        pl.col(col).median().alias(f"{col}_median") for col in num_cols
    ])
    print(grouped.head(3))

# Grouped by id and url
if "url" in df.columns:
    print("\nGrouped by id Id , post id (Summary)")
    grouped_mean = df.group_by(["id", "url"]).agg([
        pl.col(col).mean().alias(f"{col}_mean") for col in num_cols
    ])
    print(grouped_mean.head(3))
    grouped_count = df.group_by(["id", "url"]).agg([
        pl.len().alias("row_count")
    ])
    print(grouped_count.head(3))
    grouped_median = df.group_by(["id", "url"]).agg([
        pl.col(col).median().alias(f"{col}_median") for col in num_cols
    ])
    print(grouped_median.head(3))"""