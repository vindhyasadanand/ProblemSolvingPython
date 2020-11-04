''''
1. if the array size is odd then median is middle element
2. if array
'''
def merge_sorted_lists(a,b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i=j= 0
    while i<len_a and j<len_b:
        if a[i]<=b[j]:
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(b[j])
            j +=1

    while(i<len_a):
        sorted_list.append(a[i])
        i = i + 1


    while(j<len_b):
        sorted_list.append(b[j])
        j+=1

    # we finished with merging of two sorted lists
    len_sorted_list = len(sorted_list)
    mid = len_sorted_list // 2
    if not len_sorted_list %2==0:
        print("list with odd members")
        return sorted_list[mid]
    else:
        median = int((sorted_list[mid] + sorted_list[mid-1])/2)

        return median

print(merge_sorted_lists([5,6,7],[2,3,4]))


