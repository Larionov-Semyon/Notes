import time
import random

# sum = int(input())
# a1 = input()
# a2 = input()
# a3 = input()

sum = 100
N = 10000
a1 = " ".join([str(random.choice(range(200))) for i in range(N)])
a2 = " ".join([str(random.choice(range(200))) for i in range(N)])
a3 = " ".join([str(random.choice(range(200))) for i in range(N)])

# a1 = " ".join([str(i) for i in range(N)])
# a2 = " ".join([str(abs(round(random.random()) * 100) % 100) for i in range(N)])
# a3 = " ".join([str(i) for i in range(N, 0, -1)])

# print(a1, " --- ", a2, " --- ", a3)
print("--")

start_time = time.time()

l1 = list(map(int, a1.split()))[1:]
l2 = list(map(int, a2.split()))[1:]
l3 = list(map(int, a3.split()))[1:]
b = True
ind = 0
for x1 in range(len(l1)):
    for x2 in range(len(l2)):
        for x3 in range(len(l3)):
            # ind += 1
            if l1[x1] + l2[x2] + l3[x3] == sum:
                print(x1, x2, x3)
                print(" ot: ", l1[x1], l2[x2], l3[x3])
                b = False
                break
        if not b:
            break
    if not b:
        break
if b:
    print(-1)

print("--- %s HARD ---" % (time.time() - start_time), ind)
start_time = time.time()

# -----------------------------------------------

l1 = list(map(int, a1.split()))[1:]
l2 = list(map(int, a2.split()))[1:]
l3 = list(map(int, a3.split()))[1:]
ind = 0
b = True
for x1 in range(len(l1)):
    if not b:
        break
    if l1[x1] > sum:
        continue
    for x2 in range(len(l2)):
        if not b:
            break
        if l2[x2] > sum - l1[x1]:
            continue
        s = sum - l1[x1] - l2[x2]
        for x3 in range(len(l3)):
            ind += 1
            if l3[x3] == s:
                print(x1, x2, x3)
                print(" ot: ", l1[x1], l2[x2], l3[x3])
                b = False
                break
if b:
    print(-1)

print("--- %s NEW ---" % (time.time() - start_time), ind)
start_time = time.time()

l1 = list(map(int, a1.split()))[1:]
l2 = list(map(int, a2.split()))[1:]
l3 = list(map(int, a3.split()))[1:]
l1 = sorted([(l1[i], i) for i in range(len(l1))])
l2 = sorted([(l2[i], i) for i in range(len(l2))])
l3 = sorted([(l3[i], i) for i in range(len(l3))], key=lambda x: (x[0], -x[1]))
fl = False
# ans = (len(l1), len(l2), len(l3))
for aval, apos in l1:
    cpos = len(l3) - 1
    for bval, bpos in l2:
        while cpos > 0 and aval + bval + l3[cpos][0] > s:
            cpos -= 1
        if aval + bval + l3[cpos][0] == sum and (not fl or (apos, bpos, cpos) < ans):
            ans = apos, bpos, l3[cpos][1]
            fl = True
if fl:
    print(*ans)
else:
    print(-1)


print("--- %s new program with hash seconds ---" % (time.time() - start_time))
start_time = time.time()
#     -------------------


# l1, l2, l3 = a1.split(), a2.split(), a3.split()
# l1 = [(int(l1[i]), i - 1) for i in range(1, len(l1)) if int(l1[i]) <= sum]
# l2 = [(int(l2[i]), i - 1) for i in range(1, len(l2)) if int(l2[i]) <= sum]
# l3 = [(int(l3[i]), i - 1) for i in range(1, len(l3)) if int(l3[i]) <= sum]
# l1 = sorted(l1, reverse=False)
# l2 = sorted(l2, reverse=False)
# l3 = sorted(l3, reverse=False)
# # print(l2)



# l1, l2, l3 = a1.split(), a2.split(), a3.split()
# l1 = [(int(l1[i]), i - 1) for i in range(1, len(l1))]
# l2 = [(int(l2[i]), i - 1) for i in range(1, len(l2))]
# l3 = [(int(l3[i]), i - 1) for i in range(1, len(l3))]
# l1 = sorted(l1, reverse=False)
# l2 = sorted(l2, reverse=False)
# l3 = sorted(l3, reverse=False)
# # print(l1, l2, l3)
#
# x1_, x2_, x3_ = None, None, None
# b = True
# for x1, y1 in l1:
#     if b and x1_ != x1 and x1 < sum:
#         x1_ = x1
#         for x2, y2 in l2:
#             if b and x2_ != x2 and x1 < sum:
#                 x2_ = x2
#                 for x3, y3 in l3:
#                     if b and x3_ != x3 and x1 < sum:
#                         if x1 + x2 + x3 == sum:
#                             print(y1, y2, y3)
#                             print(" ot: ", x1, x2, x3)
#                             b = False
#
# if b:
#     print(-1)
# print("--- %s new program with hash seconds ---" % (time.time() - start_time))
# start_time = time.time()