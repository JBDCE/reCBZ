from unittest import TestCase


from reCBZ.util import human_sort, trim_whitespace

from PIL import Image


class Test_human_sort(TestCase):
    def test_numbers(self):
        data = [1, 3, 6, 8, 2, 5,]
        expected = ['1', '2', '3', '5', '6', '8', ]
        result = human_sort(data)
        self.assertEqual(result, expected)
        return


class Test_trim_whitespace(TestCase):
    def test_testimage(self):
        input_image = Image.open('tests/testfiles/whitespace_trim_test.png')
        expected_image_size = (530, 517)
        output_image = trim_whitespace(
            input_image=input_image,
            padding=5
        )
        self.assertEqual(output_image.size, expected_image_size)
        return
