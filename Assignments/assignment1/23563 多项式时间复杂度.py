s = input()+'+'
monomial = []
polynomial = []
i = 0

while i < len(s):
    if s[i] != '+':
        monomial.append(s[i])
    else:
        polynomial.append(''.join(monomial))
        monomial = []
    i += 1

exponents = []
exponent = []
for x in range(len(polynomial)):
    if polynomial[x][0] != '0':
        for y in range(len(polynomial[x])-1,-1,-1):
            if polynomial[x][y] in '0123456789':
                exponent.append(polynomial[x][y])
            elif polynomial[x][y] == '^':
                exponent.reverse()
                exponents.append(int(''.join(exponent)))
                exponent = []
                break
exponents.sort()
print('n^' + str(exponents[-1]))