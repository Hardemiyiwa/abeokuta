# Simulated a football match ticket system
seat_numbers = {x for x in range(1, 51)}
print(seat_numbers)
# bokink a seat
booked = int(input("Enter a seat number you want to book: "))
# Removing booked seats from the set
seat_removed = seat_numbers.remove(booked)
# showing remaing seats after each booking
print(f"Remaing seat nummber: {seat_numbers}")