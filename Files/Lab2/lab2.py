import argparse
import os
from IsingModel import IsingModel
import numpy as np

parser = argparse.ArgumentParser(description='Ising Model')
parser.add_argument("N",help="Dimension of grid", type=int)
parser.add_argument("J",help="Integral", type=float)
parser.add_argument("Betha",help="Betha", type=float)
parser.add_argument("B",help="Magnetic field value", type=float)
parser.add_argument("steps",help="steps", type=int)
parser.add_argument("-d", help="Density of \"up\" spins",type=float ,default=0.5)
parser.add_argument("-f", help="Image file",type=str ,default="Step")
args = parser.parse_args()

for root, dirs, files in os.walk('./output'):
    for f in files:
        os.unlink(os.path.join(root, f))

model = IsingModel(args.N, args.J, args.Betha, args.B, args.steps, np.around(args.d, 2), args.f)
print(model.M)
model.monte_carlo()
print(model.M)

