def apply_convolution(image, kernel, N, M):
    kernel_size = 3
    k = kernel_size // 2
    result_sum = 0

    # Initialize the result matrix
    result_matrix = [[0] * M for _ in range(N)]

    # Apply convolution
    for i in range(k, N - k):
        for j in range(k, M - k):
            convolution_sum = 0
            for u in range(-k, k + 1):
                for v in range(-k, k + 1):
                    convolution_sum += image[i + u][j + v] * kernel[u + k][v + k]
            result_matrix[i][j] = convolution_sum
            result_sum += convolution_sum

    return result_sum

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        row = list(map(int, input().split()))
        a.append(row)
    for i in range(3):
        row = list(map(int, input().split()))
        b.append(row)
    print(apply_convolution(a, b, n, m))