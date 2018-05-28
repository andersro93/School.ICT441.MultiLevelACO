class Ant(object):

    def __init__(self):
        super(Ant, self).__init__()

        self.current_city = None
        self.visited_cities = []
        self.starting_city = None
        self.destination_city = None
        self.score = None
