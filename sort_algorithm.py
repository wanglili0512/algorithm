"""
 created by Lily on 2020/12/3
"""

lst = [5, 7, 2, 4, 1, 8, 3, 9, 6]


# 冒泡排序
def bubble_sort(arg):
    # 进行 len(arg)-1 轮，无序区在前，每次在无序区选择最大的往后挪
    for i in range(len(lst) - 1):
        # 每轮比较次数递减，且进行相邻两个数的比较
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


# 选择排序
def select_sort(arg):
    # 进行 len(arg)-1 轮，无序区在后，每次在无序区选择最小的往前挪
    for i in range(len(lst) - 1):
        # 记录最小数的索引
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j
        if min_index != i:
            lst[min_index], lst[i] = lst[i], lst[min_index]


# 插入排序
def insert_sort(arg):
    # 进行 len(arg)-1 轮，无序区在后，依次把无序区的第一个插入有序区合适的位置
    for i in range(1, len(lst)):
        # 将摸到的牌暂时存起来
        tmp = lst[i]
        # j表示手里最大的牌
        j = i - 1
        while j >= 0 and lst[j] > tmp:
            lst[j+1] = lst[j]
            j = j - 1
        lst[j+1] = tmp


# 快速排序
def quick_sort(arg):
    if len(arg) <= 1:
        return arg
    else:
        tmp = arg[0]
        left = [i for i in arg[1:] if i <= tmp]
        right = [i for i in arg[1:] if i > tmp]
        return quick_sort(left) + [tmp] + quick_sort(right)


if __name__ == '__main__':
    # bubble_sort(lst)
    # select_sort(lst)
    # insert_sort(lst)
    print(lst)
    print(quick_sort(lst))
