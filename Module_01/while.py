def count_down(start_number):
  current = start_number
  while (current > 0):
    print("countdown:", str(current))
    current -= 1
  print("Zero!")
count_down(3)

def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
          break

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 


