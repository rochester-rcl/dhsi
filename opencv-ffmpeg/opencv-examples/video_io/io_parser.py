# A canned parser for io - just input and output paths

import argparse


class IOParser(object):
    def __init__(self):
        self.input_file = None
        self.output_file = None
        self.init_parser()

    def init_parser(self):
        parser = argparse.ArgumentParser(description="Test that the reader works")
        parser.add_argument('-i', '--input_file', help="input video file path", required=True, type=str)
        parser.add_argument('-o', '--output_file', help="output video file path", required=False, type=str)

        args = vars(parser.parse_args())
        self.input_file = args['input_file']
        self.output_file = args['output_file']

