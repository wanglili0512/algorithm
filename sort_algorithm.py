lst = [5, 7, 2, 4, 1, 8, 3, 9, 6]


# 冒泡排序
def bubble_sort(arg):
    # 进行 len(arg)-1 轮
    for i in range(len(lst) - 1):
        # 每轮比较次数递减，且进行相邻两个数的比较
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


if __name__ == '__main__':
    bubble_sort(lst)
    print(lst)
