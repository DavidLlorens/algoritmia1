#coding: latin1
from abc import ABCMeta, abstractmethod

class IDivideAndConquerProblem(metaclass=ABCMeta): #[intro
    @abstractmethod
    def is_simple(self) -> "bool": pass
        
    @abstractmethod
    def trivial_solution(self) -> "Solution": pass

    @abstractmethod
    def divide(self) -> "Iterable<IDivideAndConquerProblem>": pass

    @abstractmethod
    def combine(self, solutions: "Iterable<Solution>") -> "Solution": pass

class DivideAndConquerSolver:
    def solve(self, problem: "IDivideAndConquerProblem") -> "Solution":
        if problem.is_simple():
            return problem.trivial_solution()
        else:
            return problem.combine(self.solve(p) for p in problem.divide()) #] intro
