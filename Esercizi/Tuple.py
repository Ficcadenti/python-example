
t = 'abc', 123, 45.67
print(type(t))
print(len(t))
print(t)

tp=('abc', 123, 45.67)
print(type(tp))
print(tp)
print(len(tp))
print(t==tp)

tv=()
print(type(tv))
print(len(tv))
print(tv)

print(tp[:2])
print(tp[-1])
tadd=tp+(1,2,3,4,5)
print(tadd)

# t[0]='immutabile'
try:
    print(tadd.index('abc1'))
except ValueError:
    print("Oops!  That was no valid number.  Try again...")
