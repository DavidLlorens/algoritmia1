from algoritmia.problems.searching import ISortedSearcher

class NaiveSequentialSearcher(ISortedSearcher): #[alg
    def index(self, a: "sorted IList<T>", x: "T") -> "int or None": 
        index = None
        for i in range(len(a)):
            if x == a[i]: 
                index = i
        return index #]alg