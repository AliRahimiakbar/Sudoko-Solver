def get_input():
    counter = 0
    sudoku = [0] * 9
    for i in range(9):
        sudoku[i] = [0] * 9
    for i in range(9):
        data = input().split()
        for j in range(9):
            if data[j] != '.':
                sudoku[i][j] = int(data[j])
            else:
                counter += 1
    return [sudoku, counter]


def copy_list(table):
    mat = [0] * 9
    for i in range(9):
        mat[i] = [0] * 9
    for i in range(9):
        for j in range(9):
            mat[i][j] = table[i][j]
    return mat


def count_available(table, i_num, j_num):
    list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if i_num == 4 and j_num == 5:
        x = 0
    for i in range(9):
        if table[i][j_num] in list_num:
            list_num.remove(table[i][j_num])
        if table[i_num][i] in list_num:
            list_num.remove(table[i_num][i])
    x = i_num // 3
    y = j_num // 3
    for i in range(3):
        for k in range(3):
            if table[x * 3 + i][y * 3 + k] in list_num:
                list_num.remove(table[x * 3 + i][y * 3 + k])
    return list_num


def find_less_available(table):
    number_available = []
    min_num = 10
    i_less = 10
    j_less = 10
    for i in range(9):
        for j in range(9):
            if table[i][j] == 0:
                x = count_available(table, i, j)
                if min_num > len(x):
                    number_available = x
                    min_num = len(x)
                    i_less = i
                    j_less = j
    return [i_less, j_less, number_available]


def back_tracking(table, counter):
    if counter == 0:
        return [table, True]
    i_pos, j_pos, available_num = find_less_available(table)
    if len(available_num) == 0:
        return [table, False]
    for i in range(len(available_num)):
        table[i_pos][j_pos] = available_num[i]
        mat = copy_list(table)
        answer = back_tracking(mat, counter - 1)
        if answer[1]:
            return [answer[0], True]
    return [table, False]


def print_table(table):
    for i in range(9):
        print(*table[i], sep=" ")


sudoku_table, num = get_input()

table, data = back_tracking(copy_list(sudoku_table), num)

if data:
    print_table(table)
