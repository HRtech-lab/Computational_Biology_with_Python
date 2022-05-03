import numpy as np


def matrix_labelling(first, last):
    tags = []
    for i in range(ord(first), ord(last) + 1):
        tags.append(chr(i))
    return tags


def joining_tags_of_matrix(tags, val1, val2):
    if val2 < val1:
        val1,val2 = val2, val1
    tags[val1] = "(" + tags[val1] + "," + tags[val2] + ")"
    del tags[val2]


def joining_values_of_matrix(matrix, val1, val2):
    if val2 < val1:
        val1, val2 = val2, val1
    row = []
    for i in range(0, val1):
        row.append((matrix[val1][i] + matrix[val2][i]) / 2)
    matrix[val1] = row
    for i in range(val1 + 1, val2):
        matrix[i][val1] = (matrix[i][val1] + matrix[val2][i]) / 2
    for i in range(val2 + 1, len(matrix)):
        matrix[i][val1] = (matrix[i][val1] + matrix[i][val2]) / 2
        del matrix[i][val2]
    del matrix[val2]


def find_lowest_element(matrix):
    min_cell = float("inf")
    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            if matrix[a][b] < min_cell:
                min_cell = matrix[a][b]
                x, y = a, b
    return x, y


def algothim_UPGMA(matrix, tags):
    while len(tags) > 1:
        x, y = find_lowest_element(matrix)
        joining_values_of_matrix(matrix, x, y)
        joining_tags_of_matrix(tags, x, y)
    return tags[0]


def main():
    Matrix_tags = matrix_labelling("A", "E")  # A through G

    Matrix = [[], [5], [8, 11], [12, 14, 9], [15, 16, 13, 7], ]

    newick_tree_label_grouping = algothim_UPGMA(Matrix, Matrix_tags)
    print(newick_tree_label_grouping)
    f = open("answer.txt","w+")
    f.write(newick_tree_label_grouping)


if __name__ == "__main__":
    main()
