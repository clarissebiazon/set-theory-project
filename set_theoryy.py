def union(setA, setB):
    return setA.union(setB)

def intersection(setA, setB):
    return setA.intersection(setB)

def difference(setA, setB):
    return setA.difference(setB), setB.difference(setA)

def subset(setA, setB):
    return setA.issubset(setB)

setA = set(map(int, input("Enter elements of set A separated by spaces: ").split()))
setB = set(map(int, input("Enter elements of set B separated by spaces: ").split()))

print("Union of A and B:", union(setA, setB))
print("Intersection of A and B:", intersection(setA, setB))
diffA, diffB = difference(setA, setB)
print("Difference A - B:", diffA)
print("Difference B - A:", diffB)
print("Is A a subset of B?", subset(setA, setB))
