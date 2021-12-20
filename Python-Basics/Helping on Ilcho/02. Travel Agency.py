tickets = int(input())
budget = int(input())
price_per_ticket = int(input())

price_per_ticket = tickets * price_per_ticket
if budget >= price_per_ticket:
    print(f"You can sell your client {tickets} tickets for the price of {price_per_ticket}$!")
    print(f"Your client should become a change of {budget - price_per_ticket}$!")
else:
    print(f"The budget of {budget}$ is not enough. Your client can't buy {tickets} tickets with this budget!")