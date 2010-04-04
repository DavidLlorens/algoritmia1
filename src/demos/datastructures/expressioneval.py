#coding: latin1
from algoritmia.problems.traversals.treetraversals import PostorderTreeTraverser #[]dos
from algoritmia.datastructures.queues import Lifo #[pre
from algoritmia.datastructures.trees import ListOfListsTree

class ExpressionEvaluator:
    def __init__(self, createLifo=lambda: Lifo()):
        self.createLifo = createLifo

    def tokenize(self, expression: "str") -> "Iterable<str>":
        i = 0
        while i < len(expression):
            lexeme = []
            if '0' <= expression[i] <= '9':
                while i < len(expression) and '0' <= expression[i] <= '9':
                    lexeme.append(expression[i])
                    i += 1
                yield int(''.join(lexeme))
            elif expression[i] in '+*-/()':
                yield expression[i]
                i += 1
            else:
                i += 1

    def parse(self, expression: "str") -> "ITree<str>":
        S = self.createLifo()
        tree = []
        op = {'+': 0, '-': 0, '*': 1, '/': 1}
        for token in self.tokenize(expression):
            if type(token) == int:
                tree.append([token])
            elif token in op:
                while len(S) > 0 and S.top() in op and op[token] <= op[S.top()]:
                    tree[-2:] = [[S.pop(), tree[-2], tree[-1]]]
                S.push(token)
            elif token == '(':
                S.push('(')
            elif token == ')':
                while S.top() != '(':
                    tree[-2:] = [[S.pop(), tree[-2], tree[-1]]]
                S.pop()
        while len(S) > 0:
            tree[-2:] = [[S.pop(), tree[-2], tree[-1]]]
        return ListOfListsTree(tree[0]) #]pre

    def evaluate(self, exp: "str") -> "int": #[dos
        tree = self.parse(exp)
        stack = self.createLifo()
        visitor = lambda t: self.process_root(t, stack=stack)
        for dummy in PostorderTreeTraverser().traverse(tree, visitor): pass
        return stack.pop() 

    def process_root(self, tree: "ITree<str>", stack: "Lifo"):
        if isinstance(tree.root, str) and tree.root in "+-*/": 
            a, b = stack.pop(), stack.pop()
            if tree.root == '+': stack.push(b + a)
            elif tree.root == '-': stack.push(b - a)
            elif tree.root == '*': stack.push(b * a)
            else: stack.push(b // a)
        else: 
            stack.push(tree.root) #]dos
    
if __name__ == "__main__": #[tres
    ee = ExpressionEvaluator()
    exp = "2 - 5 + 3 * 6"
    print('{} -> {}'.format(ee.parse(exp), ee.evaluate(exp))) #]tres
