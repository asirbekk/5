A = [2, 4, 6, 5, 5, 4, 7, 8, 9, 4]
i = 0
if len(A) == 10:
	while i < len(A):
		if A[i] % 3 == 0:
			print(A[i])
			pass
		i += 1
		pass
else:
	print("Вывод ошибки Неверный размер списка!")