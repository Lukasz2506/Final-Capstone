# Sorting - Implement two types of sorting algorithms: Merge sort and bubble sort.

# Bubble sort

def bubble_sort(*args):
    # returns sorted list of arguments (numbers)
    sorted_list = []
    a_list = list(args)
    n = 0
    while len(a_list) > 0:
        # if sorted_list is empty, put the first argument into it.
        if len(sorted_list) == 0:
            sorted_list.append(a_list.pop(n))
        # if some of element already exists in sorted list, put it in their neighbourhood.
        elif a_list[n] in sorted_list:
            sorted_list.insert(sorted_list.index(a_list[n]), a_list.pop(n))
        # if next argument is greater, put it after.
        elif a_list[n] >= sorted_list[-1]:
            sorted_list.append(a_list.pop(n))
        # if next argument is lower, put it before.
        elif a_list[n] < sorted_list[-1]:
            sorted_list.insert(-2, a_list.pop(n))
    return sorted_list


print(bubble_sort(3, 2, 1, 5, 8, 9, 1, 3, 3, 5, 8, 19))
