import numpy as np
Y = "ACCGTT"
X = "AGTTCA"


def GET_SCORE(n1, n2, penalty=-2, reward=1):
    if n1 == n2:
        return reward
    else:
        return penalty

penalty = -3
reward = 1
mismatch = -1
def global_alignment(X, Y, penalty=-2, reward=1):
    # initialize score matrix
    score_matrix = np.ndarray((len(X) + 1, len(Y) + 1))

    for i in range(len(X) + 1):
        score_matrix[i, 0] = penalty * i

    for j in range(len(Y) + 1):
        score_matrix[0, j] = penalty * j

# initialize score matrix
score_matrix = np.ndarray((len(X) + 1, len(Y) + 1))

for i in range(len(X) + 1):
    score_matrix[i, 0] = penalty * i

for j in range(len(Y) + 1):
    score_matrix[0, j] = penalty * j

    # define each cell in the matrix by as the max score possible in that stage
    for i in range(1, len(X) + 1):
        for j in range(1, len(Y) + 1):
            match = score_matrix[i - 1, j - 1] + GET_SCORE(X[i - 1], Y[j - 1], mismatch, reward)
            delete = score_matrix[i - 1, j] + penalty
            insert = score_matrix[i, j - 1] + penalty

            score_matrix[i, j] = max([match, delete, insert])

    i = len(X)
    j = len(Y)

    align_X = ""
    align_Y = ""

    while i > 0 or j > 0:

        current_score = score_matrix[i, j]
        left_score = score_matrix[i - 1, j]

        if i > 0 and j > 0 and X[i - 1] == Y[j - 1]:
            align_X = X[i - 1] + align_X
            align_Y = Y[j - 1] + align_Y
            i = i - 1
            j = j - 1

        elif i > 0 and current_score == left_score + penalty:
            align_X = X[i - 1] + align_X
            align_Y = "-" + align_Y
            i = i - 1

        else:
            align_X = "-" + align_X
            align_Y = Y[j - 1] + align_Y
            j = j - 1

print(align_X)
print(align_Y)
print(score_matrix)
print("\nGlobal Alignment By HASSAN RAZA")
