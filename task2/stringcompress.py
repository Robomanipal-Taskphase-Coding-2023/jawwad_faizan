def compress_string(s):
    
    compressed_string = ""
    current_char = s[0]
    char_count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            char_count += 1
        else:
            if char_count > 1:
                compressed_string += f"({char_count}, {current_char})"
            else:
                compressed_string += current_char

            current_char = s[i]
            char_count = 1

    

    return compressed_string

# Example usage:
input_string = "aaabbcddddeee"
compressed_result = compress_string(input_string)
print("Compressed String:", compressed_result)
