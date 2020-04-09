numbers = [7, 8, 9, 10, 10, 12, 11, 50, 45, 12, 8, 55, 1, 10, 15, 75]

#using for loop method
def deduplicate(old_list):
    new_list = list()
    [new_list.append(number) for number in old_list if number not in new_list]
    #for number in old_list:
        #if number not in new_list:
            #new_list.append(number)
    return sorted(new_list)

#using set method
def deduplicate_v2(old_list_2):
    #return {number for number in numbers}
    return (sorted(set(old_list_2)))



print(deduplicate(numbers))
print(deduplicate_v2(numbers))

