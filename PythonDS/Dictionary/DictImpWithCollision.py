class HashTable:
    def __init__(self):
        # self.MAX indicates size of array/list
        self.MAX = 100
        # used list comprehension here we are assigning None to all the elements which are in the range
        # 0 to 99
        self.arr = [None for i in range(self.MAX)]

    # get_hash method will give the index where this particular key is stored in arr
    def get_hash(self,key):
        h = 0
        for char in key:
            # ord method will return asci value of particular character
            h+=ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    '''def __del__(self,key):
        h = self.get_hash(key)
        self.arr[h] =None'''

t = HashTable()
t["May 31"] = "Vindhya"
t["Feb 1"] = "Aparna"
t["March 5"] = "Lakshmi"
print(t.arr)
print(t["May 31"])
print(t["Feb 1"])
print(t["March 5"])



