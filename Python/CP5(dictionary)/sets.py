k = set() #Empty set
l = {} #Empty dictionary
s = {21 , 3, 4, 59, 6, 7, 8, 9, 10} #A set is a collection of unique elements. It is unordered and unindexed.
n= {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(s  , type(s))

s.remove(59);
print(s)

print(s.union(n))
print(s.intersection(n))