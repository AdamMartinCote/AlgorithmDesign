from typing import List


class Exemplaire:
    nCards: int
    nDecks: int
    baseQuality: List[int]
    synergyMatrix: List[List[int]]  # Use k,v ??

    def __init__(self, filepath: str):
        with open(filepath) as file:
            line_1 = file.readline()
            line_2 = file.readline()
            line_3 = file.readline()
            try:
                self.nCards = int(line_1)
                self.nDecks = int(line_2)
                self.baseQuality = list(map(int, line_3.split()))

                self.synergyMatrix = []
                for line in file:
                    self.synergyMatrix.append(list(map(int, line.split())))
            except ValueError:
                raise ValueError("file format error")
            finally:
                file.close()


