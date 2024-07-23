import pandas as pd
from collections import Counter


def calculate_tags_std(
        table_movies: pd.DataFrame,
        table_tags: pd.DataFrame,
):
    df_movies_and_tags = table_movies.merge(table_tags, on='movieId', how='left')
    tag_count = Counter(tag for tag in df_movies_and_tags['movieId'])
    tag_count_df = pd.DataFrame.from_dict(tag_count, orient='index', columns=['count'])
    std_tag_freq = tag_count_df["count"].std()
    return std_tag_freq
