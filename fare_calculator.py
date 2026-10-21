
# Travel Fare Calculator
FARE_RATE = 14

# Validate passenger name
name = input("Enter passenger name: ")
if name.strip() == "":
    print("Error: Passenger name cannot be empty.")
    name = input("Enter passenger name again: ")

# Validate distance
distance_input = input("Enter distance (km): ")
try:
    distance = float(distance_input)
    if distance <= 0:
        print("Error: Distance must be greater than 0.")
        distance = float(input("Enter distance again (km): "))
except ValueError:
    print("Error: Please enter a valid number.")
    distance = float(input("Enter distance again (km): "))

# Validate number of passengers
passengers_input = input("Enter number of passengers: ")
try:
    passengers = int(passengers_input)
    if passengers <= 0:
        print("Error: Passengers must be a positive whole number.")
        passengers = int(input("Enter number of passengers again: "))
except ValueError:
    print("Error: Please enter a positive whole number.")
    passengers = int(input("Enter number of passengers again: "))

# Calculate fare
total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))
