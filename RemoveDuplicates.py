# This function removes duplicates characters from a given input
def remove_duplicates(user_input):
    unique_sorted_list_of_characters = sorted(list(set(list(user_input))))
    length_of_duplicate_characters = len(
        user_input) - len(unique_sorted_list_of_characters)
    returned_text_after_duplicates_removal = ""
    for character in (unique_sorted_list_of_characters):
        returned_text_after_duplicates_removal += character
    return tuple([returned_text_after_duplicates_removal, length_of_duplicate_characters])
