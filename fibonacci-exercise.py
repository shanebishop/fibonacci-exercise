def fib():
	numbers_to_display = int(input("How many numbers do you want to display? "))
	
	if numbers_to_display == 1:
		print(0)
		return
	elif numbers_to_display == 2:
		print("0,1")
		return
	
	partial_sequence = [0, 1]
	
	for i in range(1, numbers_to_display):
		partial_sequence.append(partial_sequence[i-1] + partial_sequence[i])
	print(*partial_sequence, sep=",")

fib()