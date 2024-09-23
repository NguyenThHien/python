T = int(input())
for _ in range(T):
    mes = input().strip().split()  # Đọc và phân tách thông báo thành các từ
    res = []  # Danh sách lưu kết quả
    max_len = 100  # Độ dài tối đa của thông báo
    current_len = 0  # Độ dài hiện tại của thông báo

    for word in mes:
        # Tính toán tổng độ dài mới nếu thêm từ này vào
        # +1 cho khoảng trắng nếu res không rỗng
        if current_len + len(word) + (1 if res else 0) <= max_len:
            if res:
                res.append(' ')  # Thêm khoảng trắng nếu không phải từ đầu tiên
            res.append(word)  # Thêm từ vào kết quả
            current_len += len(word) + (1 if res else 0)  # Cập nhật độ dài hiện tại
        else:
            break  # Dừng lại nếu thêm từ này làm vượt quá độ dài tối đa

    print("".join(res))  # In kết quả