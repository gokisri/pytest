def print_pyramid(n):
    num = 1
    for i in range(1, n + 1):
        # Print leading spaces
        print(' ' * (n - i), end='')
        
        # Print numbers
        for j in range(i):
            print(num, end=' ')
            num += 1
            if num > 20:  # Stop if we have printed up to 20
                return
        
        # Move to the next line
        print()

# Call the function to print the pyramid
print_pyramid(5)
