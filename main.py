import csv
from flask import Flask
from flask_ask import Ask, statement, question, request

from filter.filter import Filter
from preprocessor.preprocessor import PreProcessor
from recommender.recommender import Recommender

app = Flask(__name__)
ask = Ask(app, '/')


@ask.launch
def start_skill():
    startup_message = "Hi and welcome to 'Secret Santa'. I can help you find a birthday or christmas present \
    for a family member. Just say 'Alexa, help me find a present!'."
    return question(startup_message)


@ask.intent('GiftRecommendationIntent')
def handle_slot_values():
    recommended_products = get_present_recommendations(request)
    speech_output = Filter.create_speech(recommended_products)
    return statement(speech_output)


def get_present_recommendations(skill_request):
    # Get Slot Values from Alexa Request
    [fav_categories, max_price] = PreProcessor.build_user_vector(skill_request.intent.slots)

    # Get Recommendations
    recommended_category = Recommender.get_recommendations(fav_categories)

    # Load Data from CSV
    csv_data = csv.DictReader(open('data/final_dataset_metadata_sentiment.csv'))

    # Filter Products
    products = Filter.filter_by_fav_category(csv_data, fav_categories.category.loc[0], recommended_category)
    products = Filter.filter_by_pricing(products, max_price)
    products = Filter.sort_by_sentiment(products)
    return products


if __name__ == '__main__':
    app.run(debug=True)
