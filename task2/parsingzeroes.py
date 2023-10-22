encoded = input("Pls enter an encoded string: ")
index = list(filter(None, encoded.split('0')))
parsed = {
    "first_name": index[0],
    "last_name": index[1],
    "id": index[2]
}
print(parsed)

