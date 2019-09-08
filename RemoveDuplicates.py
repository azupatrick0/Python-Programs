def remove_duplicates(user_input):
    if not user_input.isalpha():
        pass
    else:
        user_input_length= len(user_input)
        list_one= list(user_input)
        set_one= set(list_one)
        set_one_list= list(set_one)
        set_one_list_length= len(set_one_list)
        resolved_length= user_input_length - set_one_list_length
        list_two= list(set_one)
        list_two=sorted(list_two)
        unlist= ""
        for character in (list_two):
            unlist= unlist  + character
        list_three= [unlist,resolved_length]
        tuple_one= tuple(list_three)
        return tuple_one
