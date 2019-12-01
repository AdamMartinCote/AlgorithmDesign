from unittest import TestCase

from tp3.src.exemplaire import Exemplaire

ref_base_val = [
    2, 2, 0, 5, 2, 5, 2, 3, 4, 2, 8, 3, 3, 7, 6, 3, 2, 9, 1, 7, 9, 6, 9, 1, 7, 9, 8, 3, 5, 8, 8, 5, 0, 9, 9, 2, 4, 4, 5,
    3, 6, 5, 5, 8, 5, 4, 7, 4, 2, 3, 1, 8, 1, 6, 0, 4, 6, 2, 0, 6, 9, 5, 2, 5, 4, 1, 2, 7, 7, 8, 9, 0, 4, 3, 6, 1, 8, 3,
    6, 3, 5, 7, 6, 5, 1, 9, 7, 5, 8, 2, 8, 0, 2, 6, 5, 6, 0, 3, 8, 7,
]

ref_mat_0_3 = -6
ref_mat_99_99 = 0
ref_mat_98_97 = -6


class TestExamplaire(TestCase):
    def test_exemplaire_created(self):
        exemplaire = Exemplaire("../exemplaires/MTG_10_10")
        self.assertIsNotNone(exemplaire)
        self.assertEqual(10, exemplaire.nCards)
        self.assertEqual(10, exemplaire.nDecks)
        self.assertEqual(ref_base_val, exemplaire.baseQuality)

        self.assertEqual(ref_mat_0_3, exemplaire.synergyMatrix[0][3])
        self.assertEqual(ref_mat_99_99, exemplaire.synergyMatrix[99][99])
        self.assertEqual(ref_mat_98_97, exemplaire.synergyMatrix[98][97])
