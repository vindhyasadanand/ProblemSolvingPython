# to check one string is rotation of other
def check_rotation(s1, s2):
    if len(s1) != len(s2):
        print("they are of different lengths")
        return
    s1 = s1 + s1
    if s1.count(s2) > 0:
        print("They are rotations of each other")
    else:
        print("They are not rotations of each other")


s1 = "mango"
s2 = "juice"
check_rotation(s1, s2)



