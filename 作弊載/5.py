def print_star_pattern(N):
    if N % 2 == 0:
        raise ValueError("N 必須是奇數")
    for i in range(1, N + 1):
        print('*' * i)

# 示例使用
N = int(input("輸入奇數N："))
print_star_pattern(N)
