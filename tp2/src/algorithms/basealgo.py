from src.roll import Roll


class BaseAlgo:
    def __init__(self):
        pass

    def optimize_exemplaire(self, roll: Roll, display_solution=False, display_time=False, display_distance=False):
        # start timer
        # raise NotImplemented(f"{self.__class__.__name__} should implement optimize_exemplaire")
        cuts = self.run_algo(roll)
        # end timer
        # report result....

        if display_solution:
            print(list(map(lambda x: x.i, cuts)))

    def run_algo(self, roll: Roll):
        raise NotImplemented("class is abstract")
