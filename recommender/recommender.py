from preprocessor.categories import Categories


class Recommender:
    def get_recommendations(self, df_fav_categories):
    	#load lookup table -> this contains the recommended category for various combinations of favorite categories
    	df_lookUp = pd.read_csv('lookUp_table.csv');

    	#get favorite category
    	df_fav_categories['category'] = df_fav_categories['category'].apply(lambda x: x.value[0]);
    	df_fav_categories = df_fav_categories.sort_values(by=['category']);

    	#get the recommended category for the the favorite categories
    	recommended = df_lookUp.recommended.loc[(df_lookUp['category1'] == df_fav_categories.category.loc[0]) & (df_lookUp['category2'] == df_fav_categories.category.loc[1])].tolist()[0]

    	return recommended
