#5 4 3 11 10 13 9 8 7 2
#YI*loJVe*yoJUXJ
number = input().split(" ")
secret_message = input()
for i in range(len(number)):
    number[i] = int(number[i])
number.sort()
for i in range(len(number)):
  number[i] = number[i] - 1
encoded_message = ""
final_msg = ""
for i in range(len(secret_message)):
  for j in number:
    encoded_message += secret_message[j].upper()
    if(len(number) < len(encoded_message)):
      break
  break
for i in range(len(encoded_message)):
  if(encoded_message[i] == "*"):
      final_msg += " "
  else:
      final_msg += encoded_message[i]
print(final_msg)