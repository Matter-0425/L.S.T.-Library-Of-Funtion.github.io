def print_right_aligned_star_pattern(N):
    if N % 2 == 0:
        raise ValueError("N 必須是奇數")
    for i in range(1, N + 1):
        print(' ' * (N - i) + '*' * i)

# 示例使用
N = int(input("輸入奇數N："))
print_right_aligned_star_pattern(N)
