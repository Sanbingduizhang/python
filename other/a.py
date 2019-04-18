# 冒泡排序
def bub_sort(s_list):
    for i in range(len(s_list) - 1):
        # 优化冒泡排序
        is_change = True
        for j in range(len(s_list) - 1 - i):
            if s_list[j] > s_list[j + 1]:
                s_list[j], s_list[j + 1] = s_list[j + 1], s_list[j]
                is_change = False
        if is_change:
            break
    return s_list

num = bub_sort([12, 5, 32, 1, 5, 87, 43])
print(num)
