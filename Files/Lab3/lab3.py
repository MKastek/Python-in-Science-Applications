import argparse
from forbes import Forbes


def init_parser():
    parser = argparse.ArgumentParser(description='Webscraping of Forbes ranking')
    parser.add_argument("site",help="link to webpage", type=str)
    return parser


parser = init_parser()
args = parser.parse_args()
forbes = Forbes(args.site)
forbes.print()
