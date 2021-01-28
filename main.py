from preprocessor.preprocessor import PreProcessor
import json

if __name__ == '__main__':
    PreProcessor = PreProcessor()
    with open('sample_alexa_request.json') as json_file:
        request = json.load(json_file)
    category_values = PreProcessor.buildUserVector(request['request']['intent']['slots'])
    # value vector -> recommender -> best category + recommended category
    # best category +  recommended category -> matching -> list of products (price, asin, title)
    # list of products (price, asin, title) -> price (age) filtering -> list of products (price, asin, title)
    # new category -> nlp -> list of products(product, sentiment, price)
    # list of products -> filtering -> list of products
    print(category_values)
