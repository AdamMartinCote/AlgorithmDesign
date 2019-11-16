class Cut:
    i: int
    p_i: int

    def __init__(self, i, p_i):
        self.i = i
        self.p_i = p_i

    @property
    def r_i(self) -> float:
        return self.p_i / self.i

    def __repr__(self):
        return str(self.i)
