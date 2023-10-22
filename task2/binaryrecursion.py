def binary(num):
    if num == 0:
        return ""
    else:
        return binary(num//2) + str(num%2)
    
num = int(input("Enter a decimal number: "))

print("The binary of it is ", binary(num))