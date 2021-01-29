class Filter:

    def filter_by_fav_category(self, data, fav_category, recommended_category):
        matches = []
        for row in data:
            if recommended_category.value[0] in row['category']:
                for keyword in fav_category.value[1]:
                    if keyword in row['title']:
                        matches.append((row['asin'], row['title'], row['price']))
        return matches

    def filter_by_pricing(self, products, max_price):
        filtered_products = []
        for product in products:
            if product[2] and product[2] <= max_price:
                filtered_products.append(product)
        return filtered_products

    # def filter_by_sentiment(self):
    #   filtered_data = None
    #  return filtered_data
