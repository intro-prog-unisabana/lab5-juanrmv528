# FREEZE CODE BEGIN
def transform_data(x: int, y: float, z: str) -> float:
    result = (x * y) / (len(z) + 1) + sum(ord(c) for c in z) % 10
    return round(result, 2)
# FREEZE CODE END

from mystery_module import transform_data

x = int(input())
y = float(input())

result = transform_data(x, y, "quiz_test")

print(result)