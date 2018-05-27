import self as self

from WorldCitiesDatabase import Region, City


class Country(object):
    """
    Country is an object that holds information about a given country.
    It holds all the regions and all the cities within itself.
    """

    name: str = None
    """ The name of the country """

    __regions: list[Region] = None
    """ The regions within the country """

    __cities: list[City] = None
    """ The cities within the country """

    def __init__(self, name: str):
        super(Country, self).__init__()

        self.__regions = list()
        self.__cities = list()

        self.name = name

    def add_region(self, region: Region) -> self:
        """
        Adds the region to the countries list of regions
        :param region: Region
        :return: self
        """
        self.__regions.append(region)
        return self

    def add_city(self, city: City) -> self:
        """
        Adds a city to the country
        :param city: City
        :return: self
        """
        self.__cities.append(city)
        return self

    def get_regions(self) -> list[Region]:
        """
        Returns a list of all the regions in the country
        :return: list[Region]
        """
        return self.__regions

    def get_cities(self) -> list[City]:
        """
        Returns a list of all the cities in the country
        :return: list[City}
        """
        return self.__cities
