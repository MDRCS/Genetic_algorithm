from unittest import TestCase
from libs.genetic import Genetic

class TestGenetic(TestCase):

    def setUp(self) -> None:
        DATASET = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
        TARGET = "Hello world!"
        self.solution_test = Genetic(TARGET,DATASET)

    def test_fitness(self):
        self.assertEqual(len(self.solution_test.target),len(self.solution_test.population_initialization()))


    def test_solution(self):
        self.assertEqual(self.solution_test.get_optimal(),self.solution_test.target)

    def test_optimal(self):
        self.assertEqual(len(self.solution_test.get_optimal()),len(self.solution_test.target))

    def test_For_I_am_fearfully_and_wonderfully_made(self):
        target = "For I am fearfully and wonderfully made."
        self.solution_test.target  = target
        self.assertEqual(self.solution_test.get_optimal(),target)