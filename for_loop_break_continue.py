numbers = list(range(1, 11))

for num in numbers:
    if num == 3:
        continue  # Skip the rest of this iteration
    
    if num == 7:
        break  # Exit the loop completely
    
    print(num)

nested_for_loop_multiplication_table.py

for i in range(1, 6):
    for j in range(1, 6):  # Indent this loop!
        product = i * j  # Indent this line!
        print(f"{product:4}", end="")  # Indent this line!
    print()  # Indent this line! fix this code
