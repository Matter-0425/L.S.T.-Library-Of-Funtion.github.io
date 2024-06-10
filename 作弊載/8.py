def print_star_pattern(N):
    if N % 2 == 0:
        raise ValueError("N 必須是奇數")
    
    middle = (N + 1) // 2
    
    # 打印上半部分，包括中间行
    for i in range(1, middle + 1):
        print('*' * i)
    
    # 打印下半部分
    for i in range(middle - 1, 0, -1):
        print('*' * i)

# 示例使用
N = int(input("輸入奇數N："))
print_star_pattern(N)
