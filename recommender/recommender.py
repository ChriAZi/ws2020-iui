import os

from preprocessor.categories import Categories

from repository.repository import Repository


class Recommender:
    @staticmethod
    def get_recommendations(df_fav_categories):
        # load lookup table -> this contains the recommended category for various combinations of favorite categories
        df_look_up = Repository.get_csv_from_s3(os.getenv("BUCKET_NAME"), os.getenv("LOOKUP_CSV"))

        # get favorite category
        df_fav_categories['category'] = df_fav_categories['category'].apply(lambda x: x.value)
        df_fav_categories = df_fav_categories.sort_values(by=['category'])

        # get the recommended category for the the favorite categories
        recommended = df_look_up.recommended.loc[(df_look_up['category1'] == df_fav_categories.category.loc[0])
                                                 & (df_look_up['category2'] ==
                                                    df_fav_categories.category.loc[1])].tolist()[0]

        return Categories(recommended)
