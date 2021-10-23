import numpy as np
from PIL import Image, ImageDraw


class IsingModel:

    def __init__(self, N=2, J=1, Betha=1, B=0, steps=1, d=0.5, filename='data'):
        self.N = N
        self.J = J
        self.Betha = Betha
        self.B = B
        self.steps = steps
        self.d = d
        self.filename = filename

        self.M = np.ones((self.N, self.N))
        self.random_density()
        self.H = self.energy()
        self.image = Image.new('RGB', (self.N, self.N), (255, 255, 255))

    def random_density(self):
        self.M.flat[np.random.choice(self.N*self.N,int(self.N*self.N * (1-self.d)),replace = False )] = -1

    def draw_image(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.M[i,j] == -1:
                    self.image.putpixel((i,j),(0,0,0))
        self.image.save('test_image.png')

    def energy(self):
        E_ij = 0
        E_iB = 0
        for i in range(self.N):
            for j in range(self.N):
                if j != self.N - 1:
                    E_ij += -self.J*self.M[i,j]*self.M[i,j+1]
                if i != self.N-1:
                    E_ij += -self.J * self.M[i, j] * self.M[i +1, j]
                E_iB += -self.B * self.M[i, j]
        return E_ij + E_iB

    def step(self):
        i, j = np.random.randint(self.N), np.random.randint(self.N)
        H_0 = self.H
        self.M[i,j] *= -1
        H_1 = self.energy()
        if H_1 - H_0 < 0 or np.random.rand() < np.exp(-self.B * (H_1 - H_0)):
            self.H = H_1
        else:
            self.M[i,j] *= -1

    def monte_carlo(self):
        for i in range(self.N*self.N):
            self.step()



