# Naive search is iterating through the entire list.
# l = [1, 5, 7, 9, 13]
# target = 14

# def naive_search(l, target):
#     for i in range(len(l)):
#         if l[i] == target:
#             return i
#     return -1

# print(naive_search(l, target))


#Binary Search
def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1
    return None

sequence_a = [1, 4, 7, 9, 11, 34, 67]
item_a = 11

print(binary_search(sequence_a, item_a))

#Binary search complexity
# n = len(seq)
# k = #steps
# n*1/2*1/2*1/2.... = n/2**K
#log₂n

        

    

