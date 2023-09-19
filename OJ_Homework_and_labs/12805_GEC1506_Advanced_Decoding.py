user_input = input().lower()
encode = input()
#split_values = encode.split("1")
#split_values = [value + "1" for value in split_values if value != ""]

#print(split_values)



char_count = {}
for char in user_input:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Sort the characters by frequency in descending order
sorted_dict = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

# Assign the encoding based on the frequency order
encoding_dict = {}
current_code = '1'  # Start with '1' for the most frequent character

for char, freq in sorted_dict:
    encoding_dict[char] = current_code
    current_code = '0' + current_code

# Encode the characters in the user input
encoded_output = []
for char in user_input:
    if char in encoding_dict:
        encoded_output.append((char, encoding_dict[char]))

# Adjust the encoding length for the least frequent character
least_frequent_char = sorted_dict[-1][0]
least_frequent_length = len(encoding_dict[least_frequent_char])

for i in range(len(encoded_output)):
    char, encoding = encoded_output[i]
    if char == least_frequent_char:
        encoded_output[i] = (char, '0' * least_frequent_length)

decoding_dict = {code: char for char, code in encoding_dict.items()}

# Adjust the encoding length for the least frequent character
least_frequent_char = sorted_dict[-1][0]
least_frequent_length = len(encoding_dict[least_frequent_char])

# Handle special cases for space and 'n'
decoding_dict['0' * least_frequent_length] = ' '  # Replace adjusted encoding with space character
decoding_dict['0' * (least_frequent_length - 1)] = 'n'  # Replace adjusted encoding with 'n' character

# Decode the encoded input
decoded_message = ''
current_code = ''
for digit in encode:
    current_code += digit
    if current_code in decoding_dict:
        decoded_message += decoding_dict[current_code]
        current_code = ''

print(decoded_message)
#print(tuple(encoded_output))
