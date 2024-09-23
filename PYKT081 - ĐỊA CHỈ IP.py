import re
def is_valid_ip(s):
    pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    match = re.match(pattern, s)
    if not match:
        return False
    parts = match.groups()
    for part in parts:
        num = int(part)
        if not (0<=num<=255) or part!=str(num):
            # Đảm bảo giá trị từ 0 đến 255 và không có số 0 thừa
            return False
    return True



T = int(input())
for _ in range(T):
    s = input()
    if is_valid_ip(s):
        print("YES")
    else:
        print("NO")
    