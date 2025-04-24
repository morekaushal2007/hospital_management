#linear search
def linear(a,target,n):
    for i in range(0,n-1):
        if a[i]==target:
            return i
    return -1
a=[3,4,2,5,6,8,1]
n=len(a)
print(linear(a,8,n))