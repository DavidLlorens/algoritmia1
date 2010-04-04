from algoritmia.problems.searching import ISortedSearcher

class SequentialSearcher(ISortedSearcher):#[alg
    def index(self, a: "sorted IList<T>", x: "T") -> "int or None":
        for i in range(len(a)):
            if x == a[i]:
                return i
            elif x < a[i]:
                return None
        return None#]alg
