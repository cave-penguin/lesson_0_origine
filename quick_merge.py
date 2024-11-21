# list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
# list2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]


def quick_merge(l1, l2):
    result = []
    p1 = 0
    p2 = 0
    while p1 < len(l1) and p2 < len(l2):
        if l1[p1] <= l2[p2]:
            result.append(l1[p1])
            p1 += 1
        else:
            result.append(l2[p2])
            p2 += 1
    if p1 < len(l1):
        result += l1[p1:]

    else:
        result += l2[p2:]

    return result


# n = int(input())
# res = [int(num) for num in input().split()]
# for _ in range(n - 1):
#     cur_list = [int(num) for num in input().split()]
#     res = quick_merge(res, cur_list)
#
# print(*res)


# l3 = quick_merge(list1, list2)
#
# print(l3)
