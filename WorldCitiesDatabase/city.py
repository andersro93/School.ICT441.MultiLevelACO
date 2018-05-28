class City(object):
    """
    A city are a part of a region€
    """

    name: str = None
    """ The name of the city """

    __region = None
    """ The region this city belongs to """

    __country = None
    """ The country this city belongs to """

    __population: int = None
    """ The population of the city """

    __coordinates_long: float = None
    """ Longitude coordinates """

    __coordinates_lat: float = None
    """ Latitude coordinates """

    def __init__(self, name: str, region, country):
        self.name = name
        self.__region = region
        self.__country = country

    def set_population(self, population: int):
        """
        Sets the city's population to given amount
        :param population: int
        :return: self
        """
        self.__population = population
        return self

    def set_coordinates(self, longitude: float, latitude: float):
        """
        Sets the city's coordinates to the given coordinates
        :param longitude: float
        :param latitude: float
        :return: self
        """
        self.__coordinates_long = longitude
        self.__coordinates_lat = latitude
        return self

    def get_population(self) -> int:
        """
        Returns the population of the city
        :return: int
        """
        return self.__population

    def get_coordinates(self) -> tuple:
        """
        Returns the coordinates as a tuple where first value is longitude and second is latitude
        :return: tuple
        """
        return self.__coordinates_long, self.__coordinates_lat

    def get_region(self):
        """
        Returns the Region the city belongs to
        :return: Region
        """
        return self.__region

    def get_country(self):
        """
        Returns the Country the city belongs to
        :return: Country
        """
        return self.__country
