import pandas as pd
from typing import Tuple

from analitics.core.read_data import ratings, tags, movies
from analitics.descriptive.calculations.standard_deviation import calculate_tags_std


def standard_deviation_of_field(
        table_ratings: pd.DataFrame,
        table_tags: pd.DataFrame,
        table_movies: pd.DataFrame,
) -> Tuple[float, float, float, float]:
    std_r = round(table_ratings.rating.std(), 2)
    std_t = round(calculate_tags_std(table_movies, table_tags), 2)
    std_m = round(table_movies.movieId.std(), 2)
    std_u = round(table_ratings.userId.std(), 2)

    return std_r, std_t, std_m, std_u


std_rating, std_tags, std_movies, std_user = standard_deviation_of_field(ratings, tags, movies)
