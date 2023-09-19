'''
hello john
how are you
bcdda eabf
bag hic jak

'''
import string

# Get input
input_lines = []
while True:
    try:
        line = input().strip()
        if line:
            input_lines.append(line)
    except:
        break
input_str = ' '.join(input_lines)

# Count frequencies
char_count = {}
for char in input_str:
    if char == ' ':
        continue
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
        
sorted_dict = tuple(sorted(char_count.items(), key=lambda x: x[1], reverse = True))
#Replace with ascii lowercase
char_map = {}
for i, (char, _) in enumerate(sorted_dict):
    char_map[char] = string.ascii_lowercase[i]

# Encode input string
encoded_lines = []
for line in input_lines:
    encoded_line = ''
    for char in line:
        if char == ' ':
            encoded_line += ' '
        else:
            encoded_line += char_map[char]
    encoded_lines.append(encoded_line)
#Print the mssge
output_str = '\n'.join(encoded_lines)
print(output_str)
