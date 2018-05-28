from WorldCitiesDatabase import City


class Algorithm(object):
    """
    Base class for all algorithms
    """

    def find_shortest_path_between(self, origin: City, destination: City, visiting_cities: int):
        """
        Finds the shortest path between city x and city y and travels within the given amount of cities
        :param origin: City
        :param destination: City
        :param visiting_cities: int
        :return:
        """
        raise NotImplementedError(f"The algorithm needs to override this method")

