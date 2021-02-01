import csv
import json

from filter.filter import Filter
from recommender.recommender import Recommender
from preprocessor.preprocessor import PreProcessor

if __name__ == '__main__':
    # Get Slot Values
    with open('sample_alexa_request.json') as json_file:
        request = json.load(json_file)
    PreProcessor = PreProcessor()
    [fav_categories, max_price] = PreProcessor.build_user_vector(request['request']['intent']['slots'])

    # Get Recommendations
    Recommender = Recommender()

    recommended_category = Recommender.get_recommendations(fav_categories)

    # Load Products
    csv_data = csv.DictReader(open('data/final_dataset_metadata_sentiment.csv'))

    # Filter Products

    Filter = Filter()
    products = Filter.filter_by_fav_category(csv_data, fav_categories.category.loc[0], recommended_category)
    products = Filter.filter_by_pricing(products, max_price)
    products = Filter.sort_by_sentiment(products)
    product_list = Filter.create_speech(products)
    print(product_list)

    # products(asin, title, price) -> sentiment analysis -> top three products(title, pricing)
    # return top three products: "I have found three possible gifts for you. [for product in products speak(title, price)]
