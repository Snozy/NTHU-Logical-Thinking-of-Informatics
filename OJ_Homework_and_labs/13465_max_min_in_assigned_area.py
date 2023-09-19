# Prompt user for input
input_list = input()

# Split input by commas
test = input_list.split(",")

# Check if both 'i1' and 'i2' are present in the input
if 'i1' in test and 'i2' in test:
    final_ans = None
else:
    # Determine if we need to find minimum or maximum value
    find_min = 'i2' in test
    find_max = 'i1' in test

    # Remove 'i1' and 'i2' from the list
    test = [i for i in test if i not in ('i1', 'i2')]

    # Find 'f' and 'b' values
    f_value = next((i for i in test if i.startswith(('f', 'F'))), None)
    b_value = next((i for i in test if i.startswith(('b', 'B'))), None)

    # Remove 'f' and 'b' values from the list
    test = [i for i in test if i not in (f_value, b_value)]

    # Convert values to integers
    test = [int(i) for i in test]

    # Find the final answer
    if (f_value and int(f_value[1:]) == 0) or (b_value and int(b_value[1:]) == 0):
        final_ans = None
    elif f_value:
        index_num = int(f_value[1:])
        final_ans = max(test[:index_num]) if find_max else min(test[:index_num]) if find_min else None
    elif b_value:
        index_num = int(b_value[1:])
        final_ans = max(test[-index_num:]) if find_max else min(test[-index_num:]) if find_min else None
    else:
        final_ans = max(test) if find_max else min(test) if find_min else None

# Print the final answer
print(final_ans)
