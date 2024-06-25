s = input()
L = []
vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'Y', 'y']
for i in s:
    if i not in vowels:
        L.append('.'+str.lower(i))
print(''.join(L))