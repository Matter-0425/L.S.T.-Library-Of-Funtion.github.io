def print_diamond(N):
    if N % 2 == 0:
        raise ValueError("N 必須是奇數")
    
    # 打印上半部分，包括中间那行
    for i in range(N // 2 + 1):
        print(' ' * i + '*' * (N - 2 * i))
    
    # 打印下半部分
    for i in range(N // 2 - 1, -1, -1):
        print(' ' * i + '*' * (N - 2 * i))

# 示例使用
N = int(input("輸入奇數N："))
print_diamond(N)
