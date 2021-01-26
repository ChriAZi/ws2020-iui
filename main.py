from preprocessor.preprocessor import PreProcessor
import json

if __name__ == '__main__':
    PreProcessor = PreProcessor()
    with open('sample_alexa_request.json') as json_file:
        request = json.load(json_file)
    category_values = PreProcessor.buildUserVector(request['request']['intent']['slots'])
    print(category_values)
