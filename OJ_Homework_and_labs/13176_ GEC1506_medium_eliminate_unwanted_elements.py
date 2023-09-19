wanted_list = input()
wanted_list = wanted_list.split(" ")
unwanted_list = input()
unwanted_list = unwanted_list.split(" ")
printing = " "
wanted_list = [i for i in wanted_list if i not in (unwanted_list)]
print(" ".join(wanted_list))
