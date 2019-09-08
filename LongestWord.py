# This function returns the longest string in a sentence
def longest_string(string):
    current_longest_string = ''
    longest_string = ''
    array_of_strings = string.split()
    if(len(array_of_strings) == 1):
        return array_of_strings[0]
    else:
        array_of_strings.append('')
        for index in range(len(array_of_strings) - 1):
            if(len(array_of_strings[index]) > len(array_of_strings[index + 1])):
                current_longest_string = array_of_strings[index]
                if(len(current_longest_string) >= len(longest_string)):
                    longest_string = current_longest_string
        return longest_string