
def total(*args):
    a = 0
    for i in args:
        a += i
    return a

print(total(1,2,3,4))

def num(*nums):
    return(sum(nums))

print(num(1,2,3))


