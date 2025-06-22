arr = [7, 3, 5, 9, 10, 8, 3, 2, 2]
print(arr)
arr = arr[::-1]

for i in range(len(arr) -1):
	for j in range(len(arr) -i -1):
		arr[j] = arr[j] - arr[j +1]


arr = arr[::-1]
print(arr)
