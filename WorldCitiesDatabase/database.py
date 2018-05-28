import random


class Database(object):
    """
    Database class for holding all the countries, regions and cities in the project
    """

    countries: dict = None
    """ All the countries in the database"""

    regions: dict = None
    """ All the regions in the database """

    cities: dict = None
    """ All the cities in the database """

    def __init__(self):
        self.countries = dict()
        self.regions = dict()
        self.cities = dict()

    def print_database_summary(self) -> None:
        """
        Prints a summary of the database
        :return: None
        """
        print("============================================================")
        print(f"Database summary:")
        print(f"Countries: {len(self.countries)}")
        print(f"Regions: {len(self.regions)}")
        print(f"Cities: {len(self.cities)}")
        print("============================================================")

    def get_two_random_cities(self) -> tuple:
        """
        Returns two random selected cities
        :return: tuple
        """
        return random.choices(list(self.cities.values()), k=2)
