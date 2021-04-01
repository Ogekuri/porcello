#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""test_porcello.py: Unit test for download_test_sequence.

   :synopsis: Unit test for download_test_sequence.
   :platform: Unix, Windows


.. moduleauthor:: Francesco Rolando <ogekuri@gmail.com>

"""

import unittest
import argparse
import contextlib
import io
import sys
from porcello.download_test_sequence import cmd_line_parser_setup


_author_ = "Francesco Rolando"
_email_ = "ogekuri@gmail.com"
_copyright_ = "Copyright 2020, Francesco Rolando"


@contextlib.contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


def validate_args(parser, args):
    with captured_output():
        try:
            parser.parse_args(args)
            return True
        except SystemExit:
            return False


class CommandLineTest(unittest.TestCase):
    def setUp(self):
        self.parser = argparse.ArgumentParser()
        cmd_line_parser_setup(self.parser)

    def test_command_line(self):

        # OK CASES
        self.assertTrue(self.parser.parse_args(
            ['-a', "https://dtcsrv851.dl.net:5443",
             '-t',  "Test Seqeunce Name",
             '-p', "ExampleImagesDownload"]))

    def test_missing_required_fields(self):

        # KO CASES

        # missing '-a', "https://dtcsrv851.dl.net:5443"
        self.assertFalse(validate_args(self.parser,
                                       ['-t',  "Test Seqeunce Name",
                                        '-p', "ExampleImagesDownload"]))

        # missing '-t', "Test Seqeunce Name"
        self.assertFalse(validate_args(self.parser,
                                       ['-a', "https://dtcsrv851.dl.net:5443",
                                        '-p', "ExampleImagesDownload"]))

        # missing '-p', "ExampleImagesDownload"
        self.assertFalse(validate_args(self.parser,
                                       ['-a', "https://dtcsrv851.dl.net:5443",
                                        '-t',  "Test Seqeunce Name"]))


if __name__ == '__main__':
    unittest.main()
