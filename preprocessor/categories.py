from enum import Enum


class Categories(Enum):
    ARTS = ('Arts_Crafts_and_Sewing',
            ['Keyword', 'Keyword2'])
    AUTOMOTIVE = ('Automotive',
                  ['Keyword1', 'Keyword2'])
    CDS = ('CDs_and_Vinyl', ['Keyword1', 'Keyword2'])
    CELLPHONES = ('Cell_Phones_and_Accessories',
                  ['Keyword1', 'Keyword2'])
    CLOTHING = ('Clothing_Shoes_and_Jewelry',
                ['Keyword1', 'Keyword2'])
    ELECTRONICS = ('Electronics',
                   ['Keyword1', 'Keyword2'])
    GROCERY = ('Grocery_and_Gourmet_Food',
               ['Keyword1', 'Keyword2'])
    HOME = ('Home_and_Kitchen',
            ['Keyword1', 'Keyword2'])
    INDUSTRIAL = ('Industrial_and_Scientific',
                  ['Keyword1', 'Keyword2'])
    INSTRUMENTS = ('Musical_Instruments',
                   ['Keyword1', 'Keyword2'])
    KINDLE = ('Kindle_Store',
              ['Keyword1', 'Keyword2'])
    LUXURY = ('Luxury_Beauty',
              ['Keyword1', 'Keyword2'])
    MOVIES = ('Movies_and_TV',
              ['Keyword1', 'Keyword2'])
    PATIO = ('Patio_Lawn_and_Garden',
             ['Keyword1', 'Keyword2'])
    PANTRY = ('Prime_Pantry',
              ['Keyword1', 'Keyword2'])
    SPORTS = ('Sports_and_Outdoors',
              ['Sport'])
    TOOLS = ('Tools_and_Home_Improvement',
             ['Keyword1', 'Keyword2'])
    TOYS = ('Toys_and_Games',
            ['Keyword1', 'Keyword2'])
    GAMES = ('Video_Games',
             ['Keyword1', 'Keyword2'])
