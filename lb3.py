def calculate_expression(n):
    nn = int(str(n) + str(n))
    nnn = int(str(n) + str(n) + str(n))
    result = n + nn + nnn
    return result
print('--------------------------------------------------------')
# Зчитуємо вхідні дані
n1 = int(input("Введіть ціле число: "))
n2 = int(input("Введіть інше ціле число: "))
n3 = int(input("Ще одне ціле число: "))

# Обчислюємо та виводимо результат
result1 = calculate_expression(n1)
result2 = calculate_expression(n2)
result3 = calculate_expression(n3)

print(result1)
print(result2)
print(result3)
print('--------------------------------------------------------')
