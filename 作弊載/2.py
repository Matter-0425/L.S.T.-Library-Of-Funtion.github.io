def sum_of_even_integers(N):
    if N % 2 != 0:
        raise ValueError("N 必須是偶數")
    return N * (N + 2) // 4

# 示例使用
N = int(input("輸入偶數N："))
print(f"2 + 4 + 6 + ... + {N} = {sum_of_even_integers(N)}")
