from SimulatedLIBS import simulation
import matplotlib.pyplot as plt

Te = [1, 2, 3, 4, 5, 6]
Ne = [10**9, 10**10, 10**11, 10**12, 10**13, 10**14]

libs = simulation.SimulatedLIBS(Te=Te[4], Ne=Ne[5], elements=['Ar','Ti'],percentages=[99.9,0.1],
                                resolution=1000,low_w=200,upper_w=1000,max_ion_charge=3)
libs.plot('red')
libs = simulation.SimulatedLIBS(Te=Te[5], Ne=Ne[5], elements=['Ar','Ti'],percentages=[99.9,0.1],
                                resolution=1000,low_w=200,upper_w=1000,max_ion_charge=3)
libs.plot('blue')

plt.show()

