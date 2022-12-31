import unittest
from .piecewiserange import PiecewiseRange


class PiecewiseRangeTests(unittest.TestCase):

    """Tests for PiecewiseRange."""

    def test_three_ranges(self):
        self.assertEqual(
            list(PiecewiseRange('1-3,4-6,8-10')),
            [1, 2, 3, 4, 5, 6, 8, 9, 10],
        )

    def test_single_digit_range_and_ranges(self):
        self.assertEqual(
            list(PiecewiseRange('1-2,4,8-10')),
            [1, 2, 4, 8, 9, 10],
        )

    def test_with_spaces(self):
        self.assertEqual(
            list(PiecewiseRange('0-0, 4-8, 20-21, 43-45')),
            [0, 4, 5, 6, 7, 8, 20, 21, 43, 44, 45],
        )

    def test_looping_multiple_times(self):
        numbers = PiecewiseRange('1-3,5-8')
        self.assertEqual(list(numbers), [1, 2, 3, 5, 6, 7, 8])
        self.assertEqual(list(numbers), [1, 2, 3, 5, 6, 7, 8])

    # To test bonus 1, comment out the next line
    # @unittest.expectedFailure
    def test_len(self):
        self.assertEqual(len(PiecewiseRange('1-4, 8, 11-14')), 9)

    # To test bonus 2, comment out the next line
    # @unittest.expectedFailure
    def test_indexable(self):
        self.assertEqual(PiecewiseRange('1-2, 6-8, 12-14')[5], 12)
        self.assertEqual(PiecewiseRange('1-2, 6, 12-14')[2], 6)
        self.assertEqual(PiecewiseRange('1-2, 6-8, 12-14')[-2], 13)
        with self.assertRaises(IndexError):
            PiecewiseRange('1-2, 6-8, 12-14')[8]
        with self.assertRaises(IndexError):
            PiecewiseRange('1-2, 6-8, 12-14')[-9]

    # To test bonus 3, comment out the next line
    # @unittest.expectedFailure
    def test_equality(self):
        self.assertEqual(repr(PiecewiseRange('1-3')), "PiecewiseRange('1-3')")
        self.assertEqual(
            PiecewiseRange('1-2, 6-8, 12-14'),
            PiecewiseRange('1-2, 6-8, 12-14'),
        )
        self.assertEqual(
            PiecewiseRange('1-2,\t\r6-8,\n 12-14'),
            PiecewiseRange('1-2,  \t6-8, 12-14\t'),
        )
        self.assertEqual(
            repr(PiecewiseRange('1,2,3')),
            repr(PiecewiseRange('1-3')),
        )
        self.assertEqual(
            PiecewiseRange('1-2,6,7,8-10, 12, 13, 14'),
            PiecewiseRange('1-2,  6-10, 12-14'),
        )
        self.assertNotEqual(
            PiecewiseRange('1-2,6,7,8-10, 12, 13, 15'),
            PiecewiseRange('1-2,  6-10, 12-14'),
        )
        self.assertFalse(
            PiecewiseRange('1-3') == PiecewiseRange('1-2,4')
        )
        self.assertFalse(
            PiecewiseRange('1-3') != PiecewiseRange('1-2,3')
        )
        self.assertEqual(
            PiecewiseRange('1-999999999,1000000000'),
            PiecewiseRange('1-1000000000'),
        )


class AllowUnexpectedSuccessRunner(unittest.TextTestRunner):
    """Custom test runner to avoid FAILED message on unexpected successes."""
    class resultclass(unittest.TextTestResult):
        def wasSuccessful(self):
            return not (self.failures or self.errors)


if __name__ == "__main__":
    from platform import python_version
    import sys
    if sys.version_info < (3, 6):
        sys.exit("Running {}.  Python 3.6 required.".format(python_version()))
    unittest.main(verbosity=2, testRunner=AllowUnexpectedSuccessRunner)
