from algoritmia.problems.sorting.interfaces import IInPlaceSorter

class InPlaceBubbleSorter(IInPlaceSorter):#[three
    def sort(self, a: "IList<T>"):
        for i in range(len(a)-1):
            for j in range(len(a)-1-i):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]#]three
