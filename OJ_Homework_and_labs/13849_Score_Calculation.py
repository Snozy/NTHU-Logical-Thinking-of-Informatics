#Jerry,1/2,3/3,10
#Ben,2/2,4/5,5
#Kevin,2/4,5/6,20
input1 = input().split(",")
input2 = input().split(",")
input3 = input().split(",")
#Jerry
test1 = input1[1].split("/")
test1_result = (float(test1[0]) / float(test1[1])) * 40.0

test2 = input1[2].split("/")
test2_result = float(test2[0]) / float(test2[1]) * 60.0

final1 = round(float(test1_result) + float(test2_result) + int(input1[3]), 2)
#BEN
Btest1 = input2[1].split("/")
Btest1_result = (float(Btest1[0]) / float(Btest1[1])) * 40.0

Btest2 = input2[2].split("/")
Btest2_result = float(Btest2[0]) / float(Btest2[1]) * 60.0

final2 = round(float(Btest1_result) + float(Btest2_result) + int(input2[3]), 2)
#KEVIN
Ktest1 = input3[1].split("/")
Ktest1_result = (float(Ktest1[0]) / float(Ktest1[1])) * 40.0

Ktest2 = input3[2].split("/")
Ktest2_result = float(Ktest2[0]) / float(Ktest2[1]) * 60.0

final3 = round(float(Ktest1_result) + float(Ktest2_result) + int(input3[3]), 2)

print(f'Student_Name:{input1[0]},Final_Score:{final1:.2f}')
print(f'Student_Name:{input2[0]},Final_Score:{final2:.2f}')
print(f'Student_Name:{input3[0]},Final_Score:{final3:.2f}')