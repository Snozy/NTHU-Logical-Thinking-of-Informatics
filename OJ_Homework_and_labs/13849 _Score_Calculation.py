#Jerry,1/2,3/3,10
#Ben,2/2,4/5,5
#Kevin,2/4,5/6,20

def calculate_final_score(input_str):
    input_components = input_str.split(",")
    name = input_components[0]
    test1 = input_components[1].split("/")
    test1_result = (float(test1[0]) / float(test1[1])) * 40.0
    test2 = input_components[2].split("/")
    test2_result = float(test2[0]) / float(test2[1]) * 60.0
    bonus_points = int(input_components[3])
    final_score = round(float(test1_result) + float(test2_result) + bonus_points, 2)
    return f'Student_Name:{name},Final_Score:{final_score:.2f}'

final_scores = []
n = 3
while True and n>0:
    input_str = input()
    final_scores.append(calculate_final_score(input_str))
    n = n - 1
for score in final_scores:
      print(score)
