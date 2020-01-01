import sys 

ary = sys.stdin.readline().split(' ')
ary_new = [int(a) for a in ary]

print(type(ary))
print(ary_new)
print(sys.thread_info)
