from algoritmia.problems.sorting.interfaces import IInPlaceSorter

class InPlaceSelectionSorter(IInPlaceSorter):#[alg
    def sort(self, a: "IList<T>"): 
        for i in range(len(a)-1):
            k = i
            for j in range(i+1, len(a)):
                if a[j] < a[k]: k = j
            a[i], a[k] = a[k], a[i] #]alg
