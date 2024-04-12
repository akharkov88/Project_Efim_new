
# tt = '239/30'.split('/')
#
#
#
# print(int(tt[0])//int(tt[1]))
# print(int(tt[0])/int(tt[1]))
# print(int(tt[0])%int(tt[1]))
#
# number = 23
# sum = 0
# for i in range (1,number):
#     if i%3==0 or i%5==0:
#         sum = sum + i
#

# text = 'aabdfrad'
# str=''
# count = 0
# for v in text:
#     if text.count(v)>1 and str.count(v)==0:
#         count+=1
#         str+=v
# print(count)

# alp = 'abcdefghijklm'
#
# s = 'abababbababsdjdkj'
#
# print(list(filter(lambda x: alp.count(x)==0 ,s)))
#  x[::-1]
# s = 'hello my name is DARKSIDE'
#
#
#
# print(' '.join(list(map(lambda x: x if len(x)<5 else x[::-1],s.split(' ')))))
#
# print([x if len(x)>5 else x[::-1] for x in s.split(' ')])

# n=str(493193)
#
# while len(n)>1:
#     n = str(sum(map(lambda x: int(x), list(n))))
# print(n)

# order = [1,2,3,1,2,1,2,3,1,3,1,1,1]
# max_e = 1
#
# # if max_e==1: print(list(set(order)))
# for i in range(len(order)-1,-1,-1):
#     if order.count(order[i])>max_e:
#             order=order[:i]+order[i+1:]
# print(order)

