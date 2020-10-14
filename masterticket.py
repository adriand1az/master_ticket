TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100


def calculate_price(tickets):  
  return (tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining > 0 : 
  name = input("What is your name?: ").capitalize()
  print(f"Tickets Reamining: {tickets_remaining}")  
  try:
    tickets = int(input(f"Hi {name}, how many tickets do you want?: "))
    if tickets > tickets_remaining:
        raise ValueError(f"there are only {tickets_remaining} tickets remaining")
  except ValueError as err:
    print(f"Oh no we ran into an issue. {err} ")
  else:
    total_cost = calculate_price(tickets)
    print(f"{name} that will cost you ${total_cost}")
    confirm = input("Would you like to confirm this order?: ")
    if confirm.lower() == "yes":
      tickets_remaining -= tickets
      print("SOLD!")
    else:
      print(f"Thank You {name}, Have a great day!")
  
print(f"We are currently sold out, sorry {name}!")
                
   
