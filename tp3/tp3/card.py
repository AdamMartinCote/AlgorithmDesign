class Card:
    idx: int
    base_value: int

    def __init__(self, idx, base_value):
        self.idx = idx
        self.base_value = base_value

    def __str__(self):
        return str(self.idx)
