"""
5
hello world ! welcome to gec course for exploring world of programming 
good luck in the quiz
ararararararararararrar

2
cat 1 ! 2 4 3 5 6 7 8 9 0 
act cat cat act 0

5
This is 4 words

5
This 
is 
4
words

2
duplicate duplicate duplicate duplicate
duplicate duplicate 2 21 33 11 22
123 324 duplicate

0

"""
import string

input_lines = []
n = int(input())

while True:
    try:
        line = input().strip()
        if line:
            input_lines.append(line)
    except:
        break
#put the inputs together
input_str = ' '.join(input_lines)
input_str = [word.strip(string.whitespace) for word in input_str.split()]
#Sorting the inputs by len,ord
word_list = [(word, len(word), sum(ord(c) for c in word)) for word in input_str]
word_list.sort(key=lambda x: (x[1], x[2]), reverse=True)
#Printing by using occur
num_printed = 0
for word, _, _ in word_list:
    if num_printed < n:
        print(word)
        num_printed += 1
    else:
        break




