import random

class RandomGenerator():

    def __init__(self, size=100, density=0.25):
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
            file = open(file, 'w')
            for i in edges:
                file.write(str(i[0]) + " " + str(i[1]) + "\n")
            file.close()


class ColoredGenerator():
    def __init__(self, size = 100, density=0.2, colors=5):
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
            file = open(file, 'w')
            for i in edges:
                file.write(str(i))
            file.close()

class CliqueGenerator():
    def __init__(self, size = 100, density=0.2, cliqueSize=5):
        self.size = size
        self.density = density
        self.cliqueSize = cliqueSize

    def generate(self, file=None):
        edges = set()
        clique = set()
        for i in range(self.cliqueSize):
            vertex = int(random.random() * self.size)
            while vertex in clique:
                vertex = int(random.random() * self.size)
            clique.add(vertex)
        clique = list(clique)
        for i in clique:
            for j in clique:
                if i != j and i < j:
                    edges.add((i, j))
        for i in range(self.size):
            for j in range(i, self.size):
                if i%self.cliqueSize != j%self.cliqueSize and random.random() <= self.density:
                    edges.add((i, j))
        random.shuffle(list(edges))
        if file is not None:
            file = open(file, 'w')
            for i in edges:
                file.write(str(i[0]) + " " + str(i[1]) + "\n")
            file.close()
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
        if file is not None:
            file = open(file, 'w')
            for e in edges:
                file.write(str(i[0]) + " " + str(i[1]) + "\n")
            file.close()
        else:
            print(nodes)
            print(edges)

class IntervalGenerator():
    def __init__(self, size=10, density=0.5):
        self.size = size
        self.density = density

    def generate(self, file=None):
        intervals = []
        edges = set()
        for i in range(self.size):
            intervals.append(i)
            intervals.append(i)
        for i in range(self.size):
            for j in range(len(intervals) - 1):
                if random.random() < self.density:
                    temp = intervals[j]
                    intervals[j] = intervals[j + 1]
                    intervals[j + 1] = temp
        for i in range(self.size):
            curr = intervals.index(i) + 1
            while intervals[curr] != i:
                if intervals[curr] > i:
                    edges.add((i, intervals[curr]))
                curr += 1
        random.shuffle(list(edges))
        if file is not None:
            file = open(file, 'w')
            for i in edges:
                file.write(str(i[0]) + " " + str(i[1]) + "\n")
            file.close()
        else:
            for i in edges:
                print(str(i))



       








