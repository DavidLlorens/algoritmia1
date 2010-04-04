#coding: latin1
from abc import ABCMeta, abstractmethod

class IDecreaseAndConquerProblem(metaclass=ABCMeta): #[reduce
    @abstractmethod
    def is_simple(self) -> "bool": pass
    
    @abstractmethod
    def trivial_solution(self) -> "Solution": pass
    
    @abstractmethod
    def decrease(self) -> "IDecreaseAndConquerProblem": pass

    def process(self, s: "Solution") -> "Solution":
        return s
        
class DecreaseAndConquerSolver:
    def solve(self, problem: "IDecreaseAndConquerProblem") -> "Solution":
        if problem.is_simple():
            return problem.trivial_solution()
        else:
            return problem.process(self.solve(problem.decrease())) #]reduce

class TailRecursiveDecreaseAndConquerSolver: #[tail
    def solve(self, problem: "IDecreaseAndConquerProblem") -> "Solution":
        if problem.is_simple():
            return problem.trivial_solution()
        else:
            return self.solve(problem.decrease()) #]tail

class IterativeDecreaseAndConquerSolver: #[tailit
    def solve(self, problem: "IDecreaseAndConquerProblem") -> "Solution":
        while not problem.is_simple():
            problem = problem.decrease()
        return problem.trivial_solution() #]tailit