
# print(len(set(map(int, input().split())).intersection(set(map(int, input().split())))))


import time

# N = int(input())
# a = [1 for i in range(N + 1)]
# a[0] = 0
# # -1-Onknown 0-NO - 1-YES
# ans = input()
# while ans != "HELP":
#     l = list(map(int, ans.split()))
#     ans = input()
#     if ans == "YES":
#         l_ = [0 for i in range(N + 1)]
#         for i in l:
#             l_[i] = 1
#     else:
#         l_ = [1 for i in range(N + 1)]
#         for i in l:
#             l_[i] = 0
#     for i in range(N + 1):
#         a[i] = a[i] & l_[i]
#     ans = input()


start_time = time.time()

N = int(input())
glos = []
for i in range(N):
    set_num = set(input())
    glos.append(set_num)

N = int(input())
ans = [[], []]
max_c = -1
for i in range(N):
    c = 0
    an = input()
    ans[0].append(an)
    set_an = set(an)
    for y in glos:
        if len(set_an & y) == len(y):
            c += 1
    ans[1].append(c)
    if max_c < c:
        max_c = c

for i in range(N):
    if ans[1][i] == max_c:
        print(ans[0][i])

# print(glos)

print("--- %s new program with hash seconds ---" % (time.time() - start_time))