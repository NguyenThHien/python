#S(N) = S(N-1) + (N-th chữ cái) + S(N-1) độ dài của chuổi
# mid là vị trí trung tâm chuỗi, k = mid thì cout kí tự thêm vào, k < mid thì tìm trong chuỗi s(n-1), k > mid thì k-=mid và tìm trong chuoỗi s(n-1)
def find_kth_character(N, K):
    def get_char_at_position(N, K):
        if N == 1:
            return 'A'
        length = 2 ** N - 1
        mid = length // 2 + 1
        
        if K == mid:
            return chr(ord('A') + N - 1)
        elif K < mid:
            return get_char_at_position(N - 1, K)
        else:
            return get_char_at_position(N - 1, K - mid)
    
    return get_char_at_position(N, K)

# Đọc số bộ test
T = int(input().strip())

for _ in range(T):
    n, k = map(int, input().strip().split())
    print(find_kth_character(n, k))