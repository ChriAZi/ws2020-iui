import csv
import json
import boto3
from pandas import pandas as pd

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

    aws_id = 'AKIAYRUJDE3EEPC7BVVI'
    aws_secret = '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'
    client = boto3.client('s3', aws_access_key_id=aws_id,
                          aws_secret_access_key=aws_secret)

    bucket_name = 'iui-csv-files'

    object_key = 'data/final_dataset_metadata_sentiment.csv'
    csv_obj = client.get_object(Bucket=bucket_name, Key=object_key)
    df = pd.read_csv(csv_obj['Body'])
    df = df.drop(columns=['Unnamed: 0'])
    csv_data = df.to_dict(orient='records')

    # Filter Products

    Filter = Filter()
    products = Filter.filter_by_fav_category(csv_data, fav_categories.category.loc[0], recommended_category)
    products = Filter.filter_by_pricing(products, max_price)
    products = Filter.sort_by_sentiment(products)
    product_list = Filter.create_speech(products)
    print(product_list)
