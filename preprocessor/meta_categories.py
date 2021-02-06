from enum import Enum
from .categories import Categories


class MetaCategories(Enum):
    COOKING = ('cooking',
               Categories.PANTRY,
               Categories.HOME,
               Categories.GROCERY)
    CREATIVE = ('creative',
                Categories.INSTRUMENTS,
                Categories.ARTS,
                Categories.TOOLS)
    FASHION = ('fashion',
               Categories.CLOTHING,
               Categories.LUXURY)
    GAMES = ('games',
             Categories.GAMES,
             Categories.TOYS)
    READING = ('reading',
               Categories.KINDLE)
    TECHNOLOGY = ('technology',
                  Categories.ELECTRONICS,
                  Categories.CELLPHONES,
                  Categories.TOOLS)
    MUSIC_AND_MOVIES = ('musicAndMovies',
                        Categories.CDS,
                        Categories.MOVIES)
    TINKERING = ('tinkering',
                 Categories.AUTOMOTIVE,
                 Categories.PATIO,
                 Categories.TOOLS)
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
                    Categories.TOYS)
    INDOOR = ('indoor',
              Categories.ARTS,
              Categories.CDS,
              Categories.CELLPHONES,
              Categories.CLOTHING,
              Categories.ELECTRONICS,
              Categories.GROCERY,
              Categories.HOME,
              Categories.INDUSTRIAL,
              Categories.INSTRUMENTS,
              Categories.KINDLE,
              Categories.LUXURY,
              Categories.MOVIES,
              Categories.PANTRY,
              Categories.TOOLS,
              Categories.TOYS,
              Categories.GAMES)
    OUTDOOR = ('outdoor',
               Categories.SPORTS,
               Categories.AUTOMOTIVE,
               Categories.PATIO)
