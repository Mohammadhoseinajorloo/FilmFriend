from flask import render_template

from analitics.descriptive.totals import record_users, record_ratings, record_movies, record_tags
from analitics.descriptive.nuniques import unique_tag, unique_movie, unique_rating, unique_user
from analitics.descriptive.means import mean_users, mean_movies, mean_ratings, mean_tags
from analitics.descriptive.standard_deviation import std_user, std_tags, std_movies, std_rating
from analitics.descriptive.quartiles import quartile_ratings, quartile_movies, quartile_tags
from analitics.descriptive.min_max import (
    min_movies, min_tags, min_user, min_ratings,
    max_movies, max_tags, max_user, max_ratings
)


def home():
    return render_template("home.html")


def dashboard():
    return render_template(
        "dashboard.html",
        all_user=record_users,
        all_ratings=record_ratings,
        all_movies=record_movies,
        all_tags=record_tags,
        # __________________________
        unique_user=unique_user,
        unique_movie=unique_movie,
        unique_tag=unique_tag,
        unique_ratings=unique_rating,
        # ________________________________
        mean_users=mean_users,
        mean_movies=mean_movies,
        mean_ratings=mean_ratings,
        mean_tags=mean_tags,
        # ________________________________
        std_user=std_user,
        std_movies=std_movies,
        std_rating=std_rating,
        std_tags=std_tags,
        # ________________________________
        min_movies=min_movies,
        min_tags=min_tags,
        min_user=min_user,
        min_ratings=min_ratings,
        # ________________________________
        max_movies=max_movies,
        max_tags=max_tags,
        max_user=max_user,
        max_ratings=max_ratings,
        # _________________________________
        quartile_ratings=quartile_ratings,
        quartile_movies=quartile_movies,
        quartile_tags=quartile_tags,

    )
