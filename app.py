from libs.genetic import Genetic,Benchmark

if __name__ == "__main__":

    # DATASET = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.1234567890"
    # TARGET = "HamzaBen1997"

    DATASET = "01"
    l = ['1' for i in range(100)]
    TARGET = ''.join(l)
    solution_algorithm = Genetic(TARGET,DATASET)
    Benchmark.run(solution_algorithm.get_optimal,100)



