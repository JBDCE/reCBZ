from unittest import TestCase


from reCBZ.util import human_sort


class Test_human_sort(TestCase):
    def test_numbers(self):
        data = [1, 3, 6, 8, 2, 5,]
        expected = ['1', '2', '3', '5', '6', '8', ]
        result = human_sort(data)
        self.assertEqual(result, expected)
        return
