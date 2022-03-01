A = [1, 5, 1, 10, 50]
productArray = []
for i, value_1 in enumerate(A):
    product = 1
    for j, value_2 in enumerate(A):
        if i == j:
            continue
        product *= value_2
    if product == value_1:
        productArray.append(value_1)
print(productArray)
