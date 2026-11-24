age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ")

if age >= 18 and has_id == "yes":
    print("Both conditions are true.")

if age >= 18 or has_id == "yes":
    print("At least one condition is true.")

if not age >= 18:
    print("You are below 18.")