from WorldCitiesDatabase import Country, Region, City


class Database(object):
    """
    Database class for holding all the countries, regions and cities in the project
    """

    __countries: dict[str, Country] = None
    """ All the countries in the database"""

    __regions: list[Region] = None
    """ All the regions in the database """

    __cities: list[City] = None
    """ All the cities in the database """

    def __init__(self):
        self.__countries = dict()
        self.__regions = list()
        self.__cities = list()
