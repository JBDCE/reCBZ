from unittest import TestCase

from subprocess import run
from os import remove
from os.path import getsize


class Test_characterization(TestCase):
    '''
    Basic file input and file output validation.
    Makes sure the output stays roughly the same
    allowing for a 1% deviation in file size.

    TODO For now this still requires pip install to run
    before a test will be performed on codechanges
    '''
    # TODO This could probably be wrapped up in permutation testing
    def test_cbz_to_cbz(self):
        output_filename = 'Testfile [reCBZ].cbz'
        expected_filesize = 233608
        run([
            'recbz',
            'tests/testfiles/Testfile.cbz',
            '--cbz',
            '--noprev',
        ])
        self.assertAlmostEqual(
            getsize(output_filename),
            expected_filesize,
            delta=expected_filesize * 0.01,
        )
        remove(output_filename)
        return

    def test_cbz_to_epub(self):
        output_filename = 'Testfile [reCBZ].epub'
        expected_filesize = 130517
        run([
            'recbz',
            'tests/testfiles/Testfile.cbz',
            '--epub',
            '--noprev',
        ])
        self.assertAlmostEqual(
            getsize(output_filename),
            expected_filesize,
            delta=expected_filesize * 0.01,
        )
        remove(output_filename)
        return

    def test_epub_to_epub(self):
        output_filename = 'Testfile [reCBZ].epub'
        expected_filesize = 130517
        run([
            'recbz',
            'tests/testfiles/Testfile.epub',
            '--epub',
            '--noprev',
        ])
        self.assertAlmostEqual(
            getsize(output_filename),
            expected_filesize,
            delta=expected_filesize * 0.01,
        )
        remove(output_filename)
        return

    def test_epub_to_cbz(self):
        output_filename = 'Testfile [reCBZ].cbz'
        expected_filesize = 233443
        run([
            'recbz',
            'tests/testfiles/Testfile.epub',
            '--cbz',
            '--noprev',
        ])
        self.assertAlmostEqual(
            getsize(output_filename),
            expected_filesize,
            delta=expected_filesize * 0.01,
        )
        remove(output_filename)
        return
