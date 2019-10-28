from src.roll import Roll


class BaseAlgo:
    def __init__(self, display_solution=False, display_time=False, display_distance=False):
        self.display_solution = display_solution

    def optimize_exemplaire(self, roll: Roll):
        # start timer
        cuts = self.execute(roll)
        # end timer
        # report result....

        if self.display_solution:
            print(list(map(lambda x: x.i, cuts)))

    def execute(self, roll: Roll):
        raise NotImplemented("class is abstract")
