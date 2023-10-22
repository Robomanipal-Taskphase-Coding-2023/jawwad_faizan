dictionary = {}
i = 1
n = int(input("Enter index to generate dictionary to: "))

while i <= n:
    dictionary[i] = i*i
    i+=1

print(dictionary)