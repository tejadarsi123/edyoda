string = input("comma seperated integers : ").split(',')
input_list1 = map(int,string)
output_list1 = list(map(lambda val : 3*val, input_list1))
print(output_list1)