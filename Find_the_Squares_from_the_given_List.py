string = input("comma seperated integers : ").split(',')
list_values = map(int,string)
output_list = list(map(lambda val: val**2, list_values))
print(output_list)