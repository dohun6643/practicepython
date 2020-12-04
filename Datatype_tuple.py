# len(tuple), max(tuple), min(tuple), tuple(seq)
cast = ("cleese", "Palin", 34.52, "idle", "cleese")
print(cast[2],cast[-2],cast[1:])
print(len(cast))
# print(max(cast))
# print(max(cast), min(cast)) 


def cmp(a,b):
    print(a,b)
    return (a>b) - (a<b)

tuple1, tuple2 = (123,'xyz'), (456,'abc')
print(cmp(tuple1, tuple2))

print(cmp(tuple2, tuple1))

tuple3 = tuple2 + (786,)
print(cmp(tuple2, tuple3))
