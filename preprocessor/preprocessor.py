import pandas as pd
import numpy as np
import json

from preprocessor.meta_categories import MetaCategories
from preprocessor.categories import Categories


class PreProcessor:
    def buildUserVector(self, slots):
        slot_values = []
        category_values = [[Categories.ARTS, 0],
                           [Categories.AUTOMOTIVE, 0],
                           [Categories.BEAUTY, 0],
                           [Categories.CDS, 0],
                           [Categories.CELLPHONES, 0],
                           [Categories.CLOTHING, 0],
                           [Categories.ELECTRONICS, 0],
                           [Categories.FASHION, 0],
                           [Categories.GROCERY, 0],
                           [Categories.HOME, 0],
                           [Categories.INDUSTRIAL, 0],
                           [Categories.INSTRUMENTS, 0],
                           [Categories.KINDLE, 0],
                           [Categories.LUXURY, 0],
                           [Categories.MAGAZINES, 0],
                           [Categories.MOVIES, 0],
                           [Categories.MUSIC, 0],
                           [Categories.PATIO, 0],
                           [Categories.PANTRY, 0],
                           [Categories.SOFTWARE, 0],
                           [Categories.SPORTS, 0],
                           [Categories.TOOLS, 0],
                           [Categories.TOYS, 0],
                           [Categories.GAMES, 0]]
        for key, slot_object in slots.items():
            for subkey, value in slot_object.items():
                if subkey == 'value' and key != 'targetPerson':
                    slot_values.append([key, int(value)])
        for value in slot_values:
            for meta_category in MetaCategories:
                if value[0] == meta_category.value[0]:
                    for category in meta_category.value[1:]:
                        for category_value in category_values:
                            if category_value[0].value == category.value:
                                category_value[1] += value[1]

        df_user_rating = pd.DataFrame(np.array(category_values),
                                      columns=['category', 'rating'])
        df_user_rating["rating"] = pd.to_numeric(df_user_rating["rating"])

        return df_user_rating
