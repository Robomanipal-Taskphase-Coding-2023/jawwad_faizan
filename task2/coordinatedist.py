print ("Enter (x1,y1) values: ")

x1 = int(input())
y1 = int(input())

print ("Enter (x2,y2) values: ")

x2 = int(input())
y2 = int(input())

dist = ((x1-x2)**2 - (y2-y1)**2)**0.5

print(f"The distance bw these points is {dist}")

