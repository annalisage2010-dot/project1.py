
passenger_name = "Sally"        
destination = "Delhi"         
ticket_price = 450.50        
number_of_tickets = 5         
is_available = True
 
print("Passenger Name:", passenger_name)
print("Destination:", destination)
print("Ticket Price: Rs", ticket_price)
print("Number of Tickets:", number_of_tickets)
print("Tickets Available?", is_available)
 
print(type(passenger_name))
print(type(destination))
print(type(ticket_price))
print(type(number_of_tickets))
print(type(is_available))
 
 
total_cost = ticket_price * number_of_tickets
discount = 150
final_cost = total_cost - discount
 
print("\nTotal Cost: Rs", total_cost)
print("Discount: Rs", discount)
print("Final Cost: Rs", final_cost)
 
print("Double Ticket Price: Rs", ticket_price * 2)
print("Ticket Price After Rs40 Increase: Rs", ticket_price + 40)
print("Half Ticket Price: Rs", ticket_price / 2)
 
print("\nIs ticket price under Rs1000?", ticket_price < 1000)
print("Are more than 2 tickets booked?", number_of_tickets > 2)
print("Is destination Delhi?", destination == "Delhi")
print("Is final cost less than Rs2000?", final_cost < 2000)
 
 
travel_message = passenger_name + " is travelling to " + destination + "."
print("\nTravel Message:", travel_message)
 
print("Destination in uppercase:", destination.upper())
print("Passenger name in lowercase:", passenger_name.lower())
print("First letter of destination:", destination[0])
print("Length of passenger name:", len(passenger_name))
 
 
print("\n------------------------------")
print("TRAVEL TICKET SUMMARY")
print("--------------------------------")
print("Passenger:", passenger_name)
print("Destination:", destination)
print("Tickets Booked:", number_of_tickets)
print("Final Amount to Pay: Rs", final_cost)
print("Booking Confirmed?", is_available)
