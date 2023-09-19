#0,20,3,7
#1,2,4,5,8,10,11,13,16,17,19
input_string = input()
user_list = input_string.split(",")
#print('list: ', user_list)
final_list = []
# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])

for i in range(user_list[0], user_list[1]):
    if i % user_list[2] == 0 or i % user_list[3] == 0:
        continue
    final_list.append(str(i))

print(",".join(final_list))
