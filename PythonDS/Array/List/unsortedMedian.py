class Solution:
    def find_median(self, v):
        # Code here
        v.sort()
        len_v = len(v)
        mid = len_v // 2
        if not len_v % 2 == 0:
            return v[mid]
        else:
            median = int((v[mid] + v[mid - 1]) / 2)
            return median


'''
Array is of odd length then middle element will be median
Array is of even length then median = (arr[mid] + arr[mid-1] / 2)
'''