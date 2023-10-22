
print("Input 3 numbers pls: ")

nums = [input(), input(), input()]
i = 0
greatest = nums[0]

while i < 3:
    if nums[i] > greatest:
        greatest = nums[i]
    i +=1



print("the largest was",greatest)