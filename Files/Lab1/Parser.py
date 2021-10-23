import argparse


parser = argparse.ArgumentParser(description="To jest opis")

#python lab1.py -h
#-file argument opcjonalny

parser.add_argument('file',help = 'name of file')
parser.add_argument('-n','--number',help = 'some number',type=int,default = 44)
parser.add_argument('-bpar','--bpar', help='some flag',action='store_true')

args = parser.parse_args()
print(args.file)
print(f'File name: {args.file=}')

print(f'{args.number = }')
print(f'{args.bpar = }')





