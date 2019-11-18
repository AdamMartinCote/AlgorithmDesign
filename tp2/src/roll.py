from typing import List

from src.cut import Cut


class Roll:
    """ Un exemplaire du problème
    """
    cuts: List[Cut]
    size: int

    def __init__(self, filepath: str):
        with open(filepath) as file:
            line_1 = file.readline()
            line_2 = file.readline()
            line_3 = file.readline()
            try:
                self.size = int(line_1)
                self.cuts = [None]
                for cut_size, cut_worth in zip(line_2.split(),
                                               line_3.split()):
                    i = int(cut_size)
                    p_i = int(cut_worth)
                    self.cuts.append(Cut(i, p_i))
                pass
            except ValueError:
                raise ValueError("file format error")
            finally:
                file.close()
