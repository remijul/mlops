def reverse_str_ko(initial_string):
    final_string = ''
    index = len(initial_string)
    while index > 0:
        final_string += initial_string[index - 2] # Error here in the function for reversing
        index = index - 1
    return final_string

print(reverse_str_ko(initial_string='abc'))


def reverse_str_ok(initial_string):
    final_string = ''
    index = len(initial_string)
    while index > 0:
        final_string += initial_string[index - 1] # No error here in the function for reversing
        index = index - 1
    return final_string

print(reverse_str_ok(initial_string='abc'))