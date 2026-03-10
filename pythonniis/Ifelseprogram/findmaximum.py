print("Enter two numbers:")
a = int(input())
b = int(input())

print("1. Find Maximum")
print("2. Find Minimum")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Maximum =", max(a, b))
    case 2:
        print("Minimum =", min(a, b))
    case _:
        print("Invalid choice")