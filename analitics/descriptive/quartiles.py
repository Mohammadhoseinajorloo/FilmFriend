import pandas as pd

from analitics.descriptive.calculations.quartiles import calculate_quartile_tag
from analitics.core.read_data import movies, tags, ratings


class Quartiles:
    def __init__(self, table: pd.DataFrame):
        self.describe = table.describe()

    def quartile_25(self, column: str):
        return round(self.describe[column]["25%"], 2)

    def quartile_50(self, column: str):
        return round(self.describe[column]["50%"], 2)

    def quartile_75(self, column: str):
        return round(self.describe[column]["75%"], 2)


tags_table = calculate_quartile_tag(tags)
quartile_movies = Quartiles(movies)
quartile_ratings = Quartiles(ratings)
quartile_tags = Quartiles(tags_table)
