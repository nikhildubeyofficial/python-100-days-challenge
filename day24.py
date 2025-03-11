# Tuples

# tup = (1,)
tup = (1,4,6,7,3,9)
# tup[0] = 90  this is not allowed
print(type(tup))
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
print(tup[3])


if 342 in tup:
    print("Yes")

tup2 = tup[1:4]
print(tup2)