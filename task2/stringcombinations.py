from itertools import permutations

s=input("Enter the string: ")
s = s.split()
words=permutations(s)

for i in words:
    sentence = ' '.join(i)
    print(sentence)