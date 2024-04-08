def descending_order(numbers):
    # Sort the numbers in descending order
    numbers.sort(reverse=True)
    return numbers

def main():
    # Input list of numbers
    numbers = []
    n = int(input("Enter the number of elements in the list: "))
    
    for i in range(n):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)
    
    # Display the original list
    print("Original list:", numbers)
    
    # Display the list in descending order
    sorted_numbers = descending_order(numbers)
    print("List in descending order:", sorted_numbers)

if __name__ == "__main__":
    main()
