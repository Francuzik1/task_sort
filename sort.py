import random
unorder_list = [6, 10, 14, 3, 2, 1, 7, 9, 4, 11, 8, 12, 15, 13, 5]
print(len(unorder_list))
#bubble sort
bubble_num = None
while bubble_num != (len(unorder_list)-1):
    bubble_num = 0
    for i in range(len(unorder_list)-1):
        if unorder_list[i] < unorder_list[i+1]:
            bubble_num += 1
        else:
            unorder_list[i] = unorder_list[i+1] + unorder_list[i]
            unorder_list[i+1] = unorder_list[i] - unorder_list[i+1]
            unorder_list[i] = unorder_list[i] - unorder_list[i+1]
print(unorder_list)
#Insrtion sort
unorder_list = [6, 10, 14, 3, 2, 1, 7, 9, 4, 11, 8, 12, 15, 13, 5]
for i in range(1, len(unorder_list)):
    x = unorder_list[i]
    j = i
    while j > 0 and unorder_list[j-1] > x:
        unorder_list[j] = unorder_list[j-1]
        j -= 1
    unorder_list[j] = x
print(unorder_list)
#Selection sort
unorder_list = [6, 10, 14, 3, 2, 1, 7, 9, 4, 11, 8, 12, 15, 13, 5]
n = len(unorder_list)
for i in range(n-1):
    m = i
    for j in range(i+1, n):
        if unorder_list[j] < unorder_list[m]:
            m = j
    unorder_list[i], unorder_list[m] = unorder_list[m], unorder_list[i]
print(unorder_list)
#Sorted :D
unorder_list = [6, 10, 14, 3, 2, 1, 7, 9, 4, 11, 8, 12, 15, 13, 5]
print(sorted(unorder_list))
#quicksort
def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]
    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)

unorder_list = [6, 10, 14, 3, 2, 1, 7, 9, 4, 11, 8, 12, 15, 13, 5]
print(quicksort(unorder_list))