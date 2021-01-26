from enum import Enum
from .categories import Categories


class MetaCategories(Enum):
    COOKING = ('cooking',
               Categories.PANTRY,
               Categories.HOME,
               Categories.GROCERY)
    CREATIVE = ('creative',
                Categories.INSTRUMENTS,
                Categories.ARTS)
    FASHION = ('fashion',
               Categories.CLOTHING,
               Categories.FASHION,
               Categories.BEAUTY,
               Categories.LUXURY)
    GAMES = ('games',
             Categories.GAMES,
             Categories.TOYS)
    READING = ('reading',
               Categories.KINDLE,
               Categories.MAGAZINES)
    TECHNOLOGY = ('technology',
                  Categories.ELECTRONICS,
                  Categories.CELLPHONES,
                  Categories.SOFTWARE)
    MUSIC_AND_MOVIES = ('musicAndMovies',
                        Categories.MUSIC,
                        Categories.CDS,
                        Categories.MOVIES)
    TINKERING = ('tinkering',
                 Categories.AUTOMOTIVE,
                 Categories.PATIO,
                 Categories.TOOLS,
                 Categories.INDUSTRIAL)
    SPORTS = ('sports',
              Categories.SPORTS)
    HIGH_ACTIVITY = ('highActivity',
                     Categories.HOME,
                     Categories.INSTRUMENTS,
                     Categories.ARTS,
                     Categories.PATIO,
                     Categories.TOOLS,
                     Categories.SPORTS)
    LOW_ACTIVITY = ('lowActivity',
                    Categories.MOVIES,
                    Categories.KINDLE,
                    Categories.CDS,
                    Categories.GAMES,
                    Categories.MAGAZINES,
                    Categories.TOYS,
                    Categories.MUSIC)
    INDOOR = ('indoor',
              Categories.ARTS,
              Categories.BEAUTY,
              Categories.CDS,
              Categories.CELLPHONES,
              Categories.CLOTHING,
              Categories.ELECTRONICS,
              Categories.FASHION,
              Categories.GROCERY,
              Categories.HOME,
              Categories.INDUSTRIAL,
              Categories.INSTRUMENTS,
              Categories.KINDLE,
              Categories.LUXURY,
              Categories.MAGAZINES,
              Categories.MOVIES,
              Categories.MUSIC,
              Categories.PANTRY,
              Categories.SOFTWARE,
              Categories.TOOLS,
              Categories.TOYS,
              Categories.GAMES)
    OUTDOOR = ('outdoor',
               Categories.SPORTS,
               Categories.AUTOMOTIVE,
               Categories.PATIO)
