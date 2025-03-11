# List Methods

l = [11,42,54,65,45,77,4,5,6]
print(l)
l.append(7)
l.sort(reverse=True)
l.reverse()
print(l.index(1))
print(l.count(1))
m = l.copy()
m[0] = 0
print(l)

l.insert(1,122)
print(l)

m = [900,877,345]
l.extend(m)
print(l)