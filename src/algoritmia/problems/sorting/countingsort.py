from algoritmia.problems.sorting.interfaces import ISorter

class CountingSorter(ISorter): #[Counting
    def sorted(self, a: "IList<int>") -> "sorted IList<int>": 
        if len(a) == 0: return []
        b = [0] * len(a)
        k = max(a) + 1
        c = [0] * k
        for v in a: c[v] += 1
        for i in range(1, k): c[i] += c[i-1]
        for j in range(len(a)-1,-1,-1):
            b[c[a[j]]-1] = a[j]
            c[a[j]] -= 1
        return b #]Counting
