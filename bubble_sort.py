def bubble_sort(unsor_list, how_many_swaps=None):
    if how_many_swaps==0:
        return unsor_list
    else:
        how_many_swaps = 0
        for i in range(len(unsor_list) - 1):
            if unsor_list[i] > unsor_list[i + 1]:
                temp = unsor_list[i]
                unsor_list[i] = unsor_list[i + 1]
                unsor_list[i + 1] = temp
                how_many_swaps += 1
        return bubble_sort(unsor_list, how_many_swaps)



print(bubble_sort([2,0,9,-3,5,8,1]))