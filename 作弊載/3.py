def factorial(N):
    if N < 0:
        raise ValueError("N 必須是非負整數")
    result = 1
    for i in range(2, N + 1):
        result *= i
    return result

# 示例使用
N = int(input("輸入整數N："))
print(f"{N}! = {factorial(N)}")
