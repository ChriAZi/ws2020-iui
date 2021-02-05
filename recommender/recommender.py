import pandas as pd
from preprocessor.categories import Categories


class Recommender:
    @staticmethod
    def get_recommendations(df_fav_categories):
        df_look_up = pd.read_csv('data/look_up_table.csv')

        # get favorite category
        df_fav_categories['category'] = df_fav_categories['category'].apply(lambda x: x.value)
        df_fav_categories = df_fav_categories.sort_values(by=['category'])
        df_fav_categories = df_fav_categories.reset_index()
        # get the recommended category for the the favorite categories
        recommended = df_look_up.recommended.loc[(df_look_up['category1'] == df_fav_categories.category.loc[0])
                                                 & (df_look_up['category2'] ==
                                                    df_fav_categories.category.loc[1])].tolist()[0]

        return Categories(recommended)
