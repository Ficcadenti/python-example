
import itertools as it

def multiply(n):
    nDigits=len(str(abs(n)))
    print(nDigits)
    return n*(5**nDigits)


def score(dice):
    punto = 0

    valori = [dice.count(i) for i in range(1, 7)]

    punto += sum([a * b for a, b in zip([a // 3 for a in valori],[1000, 200, 300, 400, 500, 600])])

    if valori[0] > 2:
        valori[0] -= 3
    if valori[4] > 2:
        valori[4] -= 3

    punto += sum([a * b for a, b in zip(valori, [100, 0, 0, 0, 50, 0])])

    return punto

def permutations(string):
    
    return [''.join(strn) for strn in
            list(set(it.permutations(string, len(string))))]


print(multiply(10))

print(score([2, 3, 4, 6, 2]))

print(sorted(permutations('a')))
print(sorted(permutations('ab')))
print(sorted(permutations('aabb')))