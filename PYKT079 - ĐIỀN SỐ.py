T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()  # Sửa lỗi, gọi phương thức sort() để sắp xếp dãy số

    l = a[0]  # Giá trị nhỏ nhất trong dãy
    r = a[-1]  # Giá trị lớn nhất trong dãy

    # Danh sách đánh dấu sự xuất hiện của các số trong khoảng từ l đến r
    dd = [0] * (r + 1)  # Phải đủ lớn để bao gồm tất cả số trong khoảng từ l đến r

    # Đánh dấu sự xuất hiện của các số trong dãy a
    for num in a:
        dd[num] = 1

    cnt = 0
    # Đếm số lượng số không xuất hiện trong dãy
    for i in range(l, r + 1):
        if dd[i] == 0:
            cnt += 1

    print(cnt)