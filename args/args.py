import argparse

parser = argparse.ArgumentParser(description='argparse sample.')

parser.add_argument('-e','--error', action='store_true', default=False, help='show error (default: show no error)')
parser.add_argument('-d','--data', type=int, help='data number')
parser.add_argument('-s','--str', type=str, help='data name')

args = parser.parse_args()

print args

print vars(args)['data']
