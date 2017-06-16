# A canned parser for io - just input and output paths

import argparse


class IOParser(object):
    def __init__(self, **kwargs):
        self.input_file = None
        self.output_file = None
        try:
            self.extended_args = kwargs['add_args']
        except KeyError:
            self.extended_args = None

        self.init_parser()

    def init_parser(self):
        parser = argparse.ArgumentParser(description="Test that the reader works")
        parser.add_argument('-i', '--input_file', help="input video file path", required=True, type=str)
        parser.add_argument('-o', '--output_file', help="output video file path", required=False, type=str)

        if self.extended_args:
            for arg in self.extended_args:
                parser.add_argument(arg['short'], arg['verbose'], help=arg['help'], required=arg['required'], type=arg['type'])

        args = vars(parser.parse_args())
        for arg in args.items():
            setattr(self, arg[0], arg[1])



