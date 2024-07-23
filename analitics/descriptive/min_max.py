import pandas as pd
from typing import Tuple, Any

from analitics.core.read_data import movies, tags, ratings


def min_of_fields(
        table_movies: pd.DataFrame,
        table_tags: pd.DataFrame,
        table_ratings: pd.DataFrame,

) -> Tuple[int, str, int, int | float]:
    min_m = table_movies.movieId.min()
    min_t = table_tags.tag.min()
    min_u = table_ratings.userId.min()
    min_r = table_ratings.rating.min()

    return min_m, min_t, min_u, min_r


def max_of_fields(
        table_movies: pd.DataFrame,
        table_tags: pd.DataFrame,
        table_ratings: pd.DataFrame,

) -> Tuple[int, str, int, int | float]:
    max_m = table_movies.movieId.max()
    max_t = table_tags.tag.max()
    max_u = table_ratings.userId.max()
    max_r = table_ratings.rating.max()

    return max_m, max_t, max_u, max_r


min_movies, min_tags, min_user, min_ratings = min_of_fields(movies, tags, ratings)
max_movies, max_tags, max_user, max_ratings = max_of_fields(movies, tags, ratings)
