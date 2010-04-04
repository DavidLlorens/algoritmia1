from algoritmia.problems.sorting.interfaces import IInPlaceSorter

class InPlaceInsertionSorter(IInPlaceSorter):#[three
    def sort(self, a: "IList<T>"):
        for i in range(1, len(a)):
            x = a[i]
            j = i-1
            while j >= 0 and x < a[j]:
                a[j+1] = a[j]
                j -= 1
            a[j+1] = x #]three