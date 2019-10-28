from tp2.src.cut import Cut


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
                    self.cuts.append(Cut(size=cut_size,
                                         worth=cut_worth))

            except ValueError:
                raise ValueError("file format error")
            finally:
                file.close()
