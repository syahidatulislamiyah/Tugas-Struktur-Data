def reverse_list_of_integers(list):
    reversed_array=[]
    for a in range(0, len(list)):
        reversed_array.append(list[len(list)-a-1])
    return reversed_array

print(reverse_list_of_integers([1,2,3,4,5]))
