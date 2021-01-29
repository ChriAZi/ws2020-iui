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
    [user_vector, max_price] = PreProcessor.buildUserVector(request['request']['intent']['slots'])

    # Get Recommendations
    Recommender = Recommender()
    [fav_category, recommended_category] = Recommender.get_recommendations(user_vector)

    # Load Products
    csv_data = csv.DictReader(open('data/final_dataset_metadata.csv'))

    # Filter Products
    Filter = Filter()
    products = Filter.filter_by_fav_category(csv_data, fav_category, recommended_category)
    products = Filter.filter_by_pricing(products, max_price)
    print(products)
    # products(asin, title, price) -> sentiment analysis -> top three products(title, pricing)
    # return top three products: "I have found three possible gifts for you. [for product in products speak(title, price)]
