def parse_command(input):
    space_index = input.find(" ")
    if space_index >= 0:
        return input[0:space_index]
    else:
        return 'add'