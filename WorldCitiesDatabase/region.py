import self as self


class Region(object):
    """
    Regions are a part of a country and holds all the cities within itself
    """

    name: str = None
    """ The name of the region"""

    __country = None
    """ The country the region is a part of """

    __cities: list = None
    """ The cities within the region """

    def __init__(self, name: str, country):
        self.name = name
        self.__country = country
        self.__cities = list()

    def get_country(self):
        """
        Returns the country of the region
        :return: Country
        """
        return self.__country

    def add_city(self, city) -> self:
        """
        Adds the given city to the region
        :param city: City
        :return: self
        """
        self.__cities.append(city)
        return self

    def get_cities(self) -> list:
        """
        Returns a list of all the cities in the region
        :return: list[City]
        """
        return self.__cities
