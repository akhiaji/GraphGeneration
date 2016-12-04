import random

class RandomGenerator():

    def __init__(self, size=100, density=0.5):
        self.size = size
        self.density = density

    def generate(self, file=None):
        edges = []
        for i in range(self.size):
            for j in range(i, self.size):
                if random.random() <= self.density:
                    edges.append((i, j))
        random.shuffle(edges)
        if file is not None:
            for i in edges:
                file.write(i)


class ColoredGenerator():
    def __init__(self, size = 100, density=0.5, colors=5):
        self.size = size
        self.density = density
        self.colors = colors

    def generate(self, file=None):
        edges = []
        for i in range(self.size):
            for j in range(i, self.size):
                if i%self.colors != j%self.colors and random.random() <= self.density:
                    edges.append((i, j))
        random.shuffle(edges)
        if file is not None:
            for i in edges:
                file.write(str(i))

class CliqueGenerator():
    def __init__(self, size = 100, density=0.5, cliqueSize=5):
        self.size = size
        self.density = density
        self.cliqueSize = cliqueSize

    def generate(self, file=None):
        edges = []
        clique = {}
        for i in range(self.cliqueSize):
            vertex = int(random.random() * self.size)
            while vertex in clique:
                vertex = int(random.random() * self.size)
            clique.add(vertex)
        clique = list(clique)
        for i in range(self.cliqueSize):
            for j in range(i, self.cliqueSize):
                edges.append((i, j))

        for i in range(self.size):
            for j in range(i, self.size):
                if i%self.cliqueSize != j%self.cliqueSize and random.random() <= self.density:
                    edges.append((i, j))
        random.shuffle(edges)
        if file is not None:
            for i in edges:
                file.write(str(i))
        else:
            for i in edges:
                print(str(i))

class PosetGenerator():

    def __init__(self, size = 10, height = 5, width = 5):
        self.size = size
        self.height = height
        self.width = width

    def generate(self, file=None):
        nodes = []
        edges = set()
        for i in range(self.size):
            node = int(random.random() * self.size)
            nodes.append(node)
            edges.add((node, node))
        for i in range(len(nodes)):
            for j in range(i, len(nodes)):
                a = nodes[i]
                b = nodes[j]
                if (a < b):
                    edges.add((a, b))
                elif (a > b):
                    edges.add((b, a))
        print(nodes)
        print(edges)








