from preprocessor.categories import Categories


class Filter:

    @staticmethod
    def extract_products(data, recommended_category):
        tuples = []
        for row in data:
            if recommended_category.value in str(row['category']):
                tuples.append((row['asin'], row['title'], row['price'], row['AvgSenti'], row['category']))
        return tuples

    @staticmethod
    def filter_by_pricing(products, max_price):
        filtered_products = []
        for product in products:
            if product[2]:
                try:
                    if float(product[2]) <= float(max_price):
                        filtered_products.append(product)
                except ValueError:
                    continue
        return filtered_products

    @staticmethod
    def sort_by_sentiment(products):
        products.sort(key=lambda tup: tup[3], reverse=True)
        return products

    @staticmethod
    def create_speech(products, recording=False):
        speech = 'I have found three possible gifts for you. '
        if recording:
            products = [
                ('B000238EJ4', 'Donkey Kong Country 2', '119.90', 2.0, 'Video_Games'),
                ('B01E1BS8IO', 'Kingdom Hearts Chain of Memories', '21.93', 2.0, 'Video_Games'),
                ('B0053BG122', 'Just Dance 3', '64.11', 2.0, 'Video_Games'),
            ]
        if products[0][4] == Categories.MOVIES.value:
            speech += 'All of them are movies. '
        if products[0][4] == Categories.GAMES.value:
            speech += 'All of them are video games. '
        for idx, product in enumerate(products[:3]):
            if idx == 0:
                speech = speech + 'My first idea is ' + product[1] + ', which costs ' + product[
                    2] + ' Dollars.'
            elif idx == 1:
                speech = speech + ' The second product for a present is ' + product[1] + ', which costs ' + product[
                    2] + ' Dollars.'
            elif idx == 2:
                speech = speech + ' And lastly, my final recommendation for you is ' + product[
                    1] + ', which costs ' + \
                         product[2] + ' Dollars. I hope some of these ideas are helpful to you.'
        return speech
