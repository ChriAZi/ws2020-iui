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
        speech = 'I have found three possible gifts for you. '
        for idx, product in enumerate(products[:3]):
            if idx == 0:
                speech = speech + 'My first idea is ' + ' '.join(product[1].split()[:3]) + ', which costs ' + product[2] + ' Dollars.'
            elif idx == 1:
                speech = speech + ' The second product for a present is ' + ' '.join(product[1].split()[:3]) + ', which costs ' + product[2] + ' Dollars.'
            elif idx == 2:
                speech = speech + ' And lastly, my final recommendation for you is ' + ' '.join(product[1].split()[:3]) + ', which costs ' + \
                         product[2] + ' Dollars. I hope some of these ideas are helpful to you.'
        return speech
