data = input() #10,Debby,*
data = data.split(",")
multi = int(data[0])
print(multi*(data[2]+data[1]) + data[2])