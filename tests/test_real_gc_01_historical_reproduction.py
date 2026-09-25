import unittest


class GCT01HistoricalReproductionTests(unittest.TestCase):
    def test_march_2019_headline_identity(self):
        self.assertAlmostEqual(61.0, 68.8 - 7.8)

    def test_revised_headline_identity(self):
        self.assertAlmostEqual(43.8, 51.0 - 7.2)

    def test_cross_vintage_mixing_changes_residual(self):
        invalid_mixed_residual = 68.8 - 7.2
        self.assertAlmostEqual(61.6, invalid_mixed_residual)
        self.assertNotAlmostEqual(61.0, invalid_mixed_residual)
        self.assertNotAlmostEqual(43.8, invalid_mixed_residual)


if __name__ == "__main__":
    unittest.main()
