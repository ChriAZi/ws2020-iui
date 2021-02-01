from preprocessor.keywords import Keywords


class Filter:

    @staticmethod
    def filter_by_fav_category(data, fav_category, recommended_category):
        matches = []
        for row in data:
            if recommended_category.value in str(row['category']):
                for keyword in Keywords[fav_category].value:
                    if keyword in str(row['title']):
                        matches.append((row['asin'], row['title'], row['price'], row['AvgSenti']))
        return matches

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
    def create_speech(products):
        speech = ''
        for idx, product in enumerate(products[:3]):
            if idx == 0:
                speech = speech + 'The first product is ' + product[1] + ', which costs ' + product[2] + '.'
            elif idx == 1:
                speech = speech + ' My second idea for a present is ' + product[1] + ', which costs ' + product[2] + '.'
            elif idx == 2:
                speech = speech + ' And lastly, my final recommendation for you is ' + product[1] + ', which costs ' + \
                         product[2] + '.'
        return speech
