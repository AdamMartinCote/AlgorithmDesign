from src.cut import Cut


class Roll:
    """ Un exemplaire du problème
    """
    def __init__(self, filepath: str):
        with open(filepath) as file:
            line_1 = file.readline()
            line_2 = file.readline()
            line_3 = file.readline()
            try:
                self.size = int(line_1)
                self.cuts = []
                for cut_size, cut_worth in zip(line_2.split(),
                                               line_3.split()):
                    # print(f"cut: {cut_size}:{cut_worth}")
                    i = int(cut_size)
                    p_i = int(cut_worth)
                    self.cuts.append(Cut(i, p_i))
                pass
            except ValueError:
                raise ValueError("file format error")
            finally:
                file.close()

    def __getitem__(self, key) -> int:
        # d = {cut.i: cut.p_i for cut in self.cuts}
        # return d[key]

        return self.cuts[key - 1].p_i if key else 0
