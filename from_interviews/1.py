# Изменить порядок слов
#
# Вам дана строка ‘s’ с некоторым количеством слов N. Нужно сделать так, чтобы исходный порядок слов в строке изменился на обратный.
#
# При этом в исходной строке между словами может быть множество пробелов, но в результате работы скрипта мы должны получить предложение с одним пробелом между словами, без пробелов в начале предложения и после его конца.
#
# Время выполнения скрипта не должно превышать 1 секунду.
import datetime
from queue import Queue
from sys import setrecursionlimit
from sys import stdin

string = "  Dgheyuw jkdsa    dadada  ewqewq      edadsad ewqewqe    "
start1 = datetime.datetime.now()


def string_formatter(s):
    words = s.split(" ")
    res = []
    for word in words:
        if word:
            res.insert(0, word)

    return " ".join(res)


# string_formatter(string)
end1 = datetime.datetime.now()
# print(end1 - start1)
"""
    Time Complexity  = O(N)
    Space Complexity = O(N)

    Where N is the length of the string.
"""

start2 = datetime.datetime.now()


def reverseString(str: str) -> str:

    # if the string is " " then return "".
    if str == "" or str == " ":
        return ""
    ans = ""

    start = len(str) - 1

    while start >= 0:

        # Skip multiple spaces.
        if str[start] == " ":
            start -= 1
        else:

            # Add space between words.
            if len(ans) > 0:
                ans += " "

            j = start

            while j >= 0 and str[j] != " ":
                j -= 1

            # add current word to ans.
            ans += str[j + 1 : j + 1 + start - j]
            start = j

    return ans


# reverseString(string)
end2 = datetime.datetime.now()
# print(end2 - start2)


"""Сумма всех чисел до N

Вам дано число N. Напишите скрипт, который считал бы сумму всех четных чисел в промежутке от 1 до N, включая N. К примеру, если N равняется 6, то вывод должен быть равен 2+4+6, то есть 12."""

N = 10
start3 = datetime.datetime.now()


def summa(N):
    counter = 1
    res = 0
    while counter <= N:
        if counter % 2 == 0:
            res += counter
            counter += 1
        counter += 1
    return res


# print(summa(N))
end3 = datetime.datetime.now()
# print(end3 - start3)
start4 = datetime.datetime.now()


def evenSumTillN(n):
    sum = (n // 2) * (n // 2 + 1)
    return sum


# print(evenSumTillN(N))
end4 = datetime.datetime.now()
# print(end4 - start4)


"""Палиндромы из чисел

У вас есть список из целых чисел. Вам нужно написать скрипт, который определит, является ли последовательность чисел палиндромом. Если это палиндром, нужно вернуть true, а если нет — вернуть false."""

arr = [1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1]


def is_palindrom(arr):
    return arr == arr[::-1]


# print(is_palindrom(arr))


class Node:
    def __init__(self, data):

        self.data = data
        self.next = None


def isPalindrome(head):

    # It stores the Linked List node value.
    st = []

    # Creating temporary Node.
    temp = head

    while temp is not None:

        # Add the current node value to stack.
        st.append(temp.data)

        # Move current pointer to next node.
        temp = temp.next

    while head is not None:

        # Get the top most element of stack.
        top = st.pop()

        if top != head.data:

            return False

        head = head.next

    return True


def takeinput():

    inputlist = [int(ele) for ele in input().split()]

    head = None
    tail = None

    for currentData in inputlist:

        if currentData == -1:
            break

        Newnode = Node(currentData)

        if head is None:
            head = Newnode
            tail = Newnode
        else:
            tail.next = Newnode
            tail = Newnode

    return head


# Main
# t = int(stdin.readline().rstrip())

# while t > 0:

#     head = takeinput()

#     if isPalindrome(head):
#         print('true')
#     else:
#         print('false')


#     t -= 1


"""Заменить пробелы

У вас есть строка STR, в которой есть слова с пробелами. Вам нужно заменить пробелы между словами на “@40”."""


STR = "fdsaffds fdsaffdsa fhhghhgf jytryeyte"


def func(string):
    res = ""
    for i in range(len(string)):
        if string[i] == " ":
            res += "@40"
        else:
            res += string[i]

    return res


# print(func(STR))


"""Уровни двоичного дерева

Вам дано двоичное дерево, в котором находятся целые числа. Ваш скрипт должен вывести последовательность чисел, которая бы показывала, как он проходил по двоичному дереву.

При этом количество попыток не должно превышать 100, количество ветвей дерева не должно быть меньше нуля и не должно превышать 1000, а числа дерева не должны быть отрицательными."""

setrecursionlimit(10**7)

#   Binary tree node class for reference


class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def getLevelOrder(root):

    output = []

    #   If given tree is empty
    if root == None:
        return output

    #   To traverse level by level
    level = Queue()

    #   Append root to the queue
    level.put(root)

    #   Iterater until queue does not become empty
    while not level.empty():

        #   Get the size of current level
        levelSize = level.qsize()

        #   Visit all node which are at current level and append their children if they exist
        while levelSize != 0:

            #   Get the front node from queue
            curr = level.get()

            #   Store in output
            output.append(curr.val)

            #   Append left child into queue if it exist
            if curr.left != None:
                level.put(curr.left)

            #   Append right child into queue if it exist
            if curr.right != None:
                level.put(curr.right)

            levelSize = levelSize - 1

    #   Return the output
    return output


#   Take input


def takeInput():

    arr = list(map(int, stdin.readline().strip().split(" ")))

    rootData = arr[0]

    n = len(arr)

    if rootData == -1:
        return None

    root = BinaryTreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while q.qsize() > 0:
        currentNode = q.get()

        leftChild = arr[index]

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        index += 1
        rightChild = arr[index]

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

        index += 1

    return root


def printAns(ans):
    for x in ans:
        print(x, end=" ")
    print()


# main
# T = int(stdin.readline().strip())
# for i in range(T):
#     root = takeInput()
#     ans = getLevelOrder(root)
#     printAns(ans)
