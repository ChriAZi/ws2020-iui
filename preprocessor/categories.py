from enum import Enum


class Categories(Enum):
    ARTS = ('Arts_Crafts_and_Sewing',
            ['Sewing', 'potter', 'tinkering', 'DIV', 'Design', 'creative', 'Knitting', 'painting', 'crochet', 'draw'])
    AUTOMOTIVE = ('Automotive',
                  ['car', 'vehicle', 'automotive', 'driving', 'motor', 'motorcycle', 'SUV', 'garage', 'truck', 'ride'])
    CDS = ('CDs_and_Vinyl',
           ['CD', 'Vinyl', 'Audio', 'Music', 'Sound', 'jukebox', 'recorder', 'radio', 'album', 'disc'])
    CELLPHONES = ('Cell_Phones_and_Accessories',
                  ['Phone', 'Cell Phone', 'Case', 'Charger', 'PopSockets', 'Headphones', 'Headset', 'Bluetooth',
                   'mobil phone', 'mobile'])
    CLOTHING = ('Clothing_Shoes_and_Jewelry',
                ['Jewelry', 'Clothing', 'Shoes', 'fashion', 'style', 'bag', 'clobber', 'accessories', 'watch', 'outfit',
                 'look'])
    ELECTRONICS = ('Electronics',
                   ['Electronics', 'Technology', 'engineering', 'technique', 'Tablet', 'laptop', 'screen',
                    'electronic device', 'electronic equipment', 'apparatus'])
    GROCERY = ('Grocery_and_Gourmet_Food',
               ['Grocery', 'Gourmet', 'Food', 'meal', 'eat', 'drink', 'epicure', 'gastronome', 'gourmand', 'restaurant',
                'pub', 'brasserie'])
    HOME = ('Home_and_Kitchen',
            ['Home', 'Kitchen', 'cooking', 'baking', 'appliances', 'decoration', 'living', 'house', 'utensils',
             'domestic'])
    INDUSTRIAL = ('Industrial_and_Scientific',
                  ['industrial', 'scientific', 'academic', 'scholarly', 'science', 'mechanical', 'technical',
                   'analytical', 'manufacturing', 'tech'])
    INSTRUMENTS = ('Musical_Instruments',
                   ['Musical', 'Instruments', 'singing', 'playing an instrument', 'guitar', 'piano', 'make music',
                    'play music', 'karaoke', 'performing'])
    KINDLE = ('Kindle_Store',
              ['Kindle Store', 'Books', 'read', 'reading', 'fantasy', 'novel', 'story', 'Kindle', 'lecture', 'ebook',
               'electronic book'])
    LUXURY = ('Luxury_Beauty',
              ['luxury', 'beauty', 'opulence', 'luxurious', 'elegance', 'make-up', 'nails', 'glamour', 'pedicure',
               'manicure'])
    MOVIES = ('Movies_and_TV',
              ['Movies', 'TV', 'cinema', 'DVD', 'blu-ray', 'film', 'video', 'actor', 'television', 'watching'])
    PATIO = ('Patio_Lawn_and_Garden',
             ['patio', 'lawn', 'garden', 'patch', 'flower', 'bed', 'plants', 'backyard', 'yard', 'court'])
    PANTRY = ('Prime_Pantry',
              ['Prime Pantry', 'household', 'essentials', 'use', 'groceries', 'food', 'care package', 'useful',
               'household article', 'victual'])
    SPORTS = ('Sports_and_Outdoors',
              ['Sport', 'outdoor', 'outside', 'activity', 'hiking', 'walk', 'running', 'skiing', 'athletic', 'afoot'])
    TOOLS = ('Tools_and_Home_Improvement',
             ['Tools', 'Home Improvement', 'handcrafted', 'drill', 'screw', 'bolt', 'hammer', 'improvement', 'construct',
              'assemble', 'montage'])
    TOYS = ('Toys_and_Games',
            ['Toy', 'Game', 'play', 'board game', 'cards', 'games night', 'table game', 'plaything', 'frolic', 'playing'])
    GAMES = ('Video_Games',
             ['Video Games', 'gaming', 'computer games', 'electronic games', 'arcade', 'console', 'gambling', 'game',
              'paddle', 'joy stick'])
