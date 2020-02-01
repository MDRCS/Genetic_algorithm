import datetime
import random
import statistics
import time
import sys

" This library gonna be an example of genetic algorithms mapped on guessing password example "

class Chromosome:

    def __init__(self,genes,fitness):
        self.genes = genes
        self.fitness = fitness

class Genetic:

    def __init__(self,target,dataset):
        self.start_time = datetime.datetime.now()
        self.target = target
        self.dataset = dataset

    def population_initialization(self):
        guess = ''
        length_target = len(self.target)
        length_dataset = len(self.dataset)

        while len(guess) < length_target:
            guess += self.dataset[random.randint(0, length_dataset - 1)]
        genes = guess
        fitness = self.get_fitness(genes)
        return Chromosome(genes, fitness)

    def get_fitness(self,guess):
        return sum(
            1 for i in range(len(guess))
            if guess[i] == self.target[i]
        )

    def mutate(self,parent):

        index = random.randint(0, len(parent.genes) - 1)
        child = parent
        new_gene, alternate = random.sample(self.dataset, 2)
        gene = new_gene
        if child.genes[index] == new_gene: gene = alternate
        child_genes = [child.genes[i] if i != index else gene for i in range(len(child.genes))]
        genes = ''.join(child_genes)
        fitness = self.get_fitness(genes)
        return Chromosome(genes,fitness)

    def display(self,guess):
        timeDiff = datetime.datetime.now() - self.start_time
        print("{0}\t{1}\t{2}".format(guess.genes, guess.fitness, str(timeDiff)))

    def get_optimal(self):
        random.seed()  # generate the same previous generated value
        length_target = len(self.target)

        parent = self.population_initialization()
        self.display(parent)
        while True:

            child = self.mutate(parent)
            if child.fitness > parent.fitness:
                parent = child
                self.display(parent)

            if child.fitness >= length_target:
                break

        return child



class Benchmark:

    @staticmethod
    def run(func,length):
        timings = []
        #stdout = sys.stdout #Allows us to redirect results of display function for each iteration from the console
        for i in range(length):
            #sys.stdout = None
            start = time.time()
            func()
            seconds = time.time() - start
           # sys.stdout = stdout
            timings.append(seconds)
            mean = statistics.mean(timings)
            if i < 10 or i % 10 == 9:
                print("{0} Mean : {1:3.2f} sec, Standard deviation : {2:3.2f} sec".format(1 + i, mean,
                                                     statistics.stdev(timings, mean) if i > 1 else 0))

