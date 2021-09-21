# Simple example of a memory maneger (from Training on algorithms from Yande)
# Dynamic memory allocation
import os


def initmemory():
    os.system('cls')
    maxn = int(input("Input maxn: "))

    memory = []
    for i in range(maxn):
        # ...append([ key, left son, right son ])
        memory.append([0, i + 1, 0])
    return [memory, 0]


def newnode(memstruct):
    memory, firstfree = memstruct
    memstruct[1] = memory[firstfree][1]
    return firstfree


def delnode(memstruct, index):
    memory, firstfree = memstruct
    memory[index][1] = firstfree
    memstruct[1] = index


def printnode(memstruct):
    os.system('cls')
    print("First element {}".format(memstruct[1]))
    length = len(memstruct[0])
    print("Index:    ", "".join([" %5d |" % i for i in range(length)]))
    print("Key:      ", "".join([" %5d |" % (memstruct[0][i][0]) for i in range(length)]))
    print("Left Son: ", "".join([" %5d |" % (memstruct[0][i][1]) for i in range(length)]))
    print("Right Son:", "".join([" %5d |" % (memstruct[0][i][2]) for i in range(length)]))


if __name__ == "__main__":
    memstruct = initmemory()
    printnode(memstruct)
    while 1:
        action = input("Command: q - exit, d - delete, n - new, i - init: ")
        if action == "d":
            delnode(memstruct, 1)
        elif action == "n":
            newnode(memstruct)
        elif action == "i":
            memstruct = initmemory()
        else:
            print("Exit")
            exit()

        printnode(memstruct)





