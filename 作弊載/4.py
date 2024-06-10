def series_sum(N):
    if N < 2:
        raise ValueError("N 必須大於等於 2")
    total_sum = 0.0
    for i in range(1, N):
        total_sum += (1 / i) * (1 / (i + 1))
    return total_sum

# 示例使用
N = int(input("輸入整數N："))
print(f"1/1 * 1/2 + 1/2 * 1/3 + ... + 1/{N-1} * 1/{N} = {series_sum(N)}")
