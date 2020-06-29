arr = [[0, -4, -6, 0, -7, -6],[-1, -2, -6, -8, -3, -1],[-8, -4, -2, -8, -8, -6],[-3, -1, -2, -5, -7, -4],[-3, -5, -3, -6, -6, -6],[-3, -6, 0, -8, -6, -7]]
sum = []
max_sum = 0
for i in range(0, len(arr) - 2):
    for j in range (0, len(arr[i]) - 2):
        sum1 = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        sum2 = arr[i+1][j+1]
        sum3 = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        sumt = sum1 + sum2 + sum3
        if sumt > max_sum:
            ma  

max_sum = max(sum)
print(max_sum)

# 0, -4, -6, 0, -7, -6
# -1, -2, -6, -8, -3, -1
# -8, -4, -2, -8, -8, -6
# -3, -1, -2, -5, -7, -4
# -3, -5, -3, -6, -6, -6
# -3, -6, 0, -8, -6, -7
