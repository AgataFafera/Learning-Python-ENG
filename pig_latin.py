def pig_latin(my_input):
    parts = my_input.split()
    second_list = [ string[1:] + string[0] + 'ay' for string in parts  ]
    return ' '.join(second_list)

string_in = input("Type your string: ")
print(pig_latin(string_in))
