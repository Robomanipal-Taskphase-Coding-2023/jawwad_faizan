n = int(input("How many numbers do you want? "))
array = []
i = 0

while i < n:
    array.append(int(input(f"Input {i+1}th number: ")))
    i +=1

i = 0
greatest = array[0]

while i < n:
    if array[i] > greatest:
        greatest = array[i]
    i +=1


array.remove(greatest)


i = 0
greatest = array[0]

while i < n-1:
    if array[i] > greatest:
        greatest = array[i]
    i +=1

print(f"2nd largest no. is {greatest}")

