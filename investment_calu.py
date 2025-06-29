#simple stock portfolio tracker
#predefined stock prices
stock_prices = {
    "AAPL":180,
    "TESLA": 250,
    "GOOGL": 2800,
    "AMZN":3300,
    "MSFT": 350
}
print("\n\n")
print("Welcome to Stock investment calculator ")

print("\n\nfollowing are the current top shares of the company:")
for company in stock_prices.keys():
    print(company)

total = 0 
while True:
    name=str(input("Enter the name of the share to get the value:")).upper()
    
    if name in stock_prices:
        print(f"The current price of the {name} is Rs.{stock_prices[name]}\n")
        quantity=int(input(f"Enter the no. of the shares u wanna buy of {name}:"))
        investment= quantity * stock_prices[name]
        print(f"{quantity} shares of {name} will be Rs. {investment}")
        print("\n")
        total += investment
        print(investment,"added in your portfolio\n")
    else:
        print("Share is not available")
    more_shares=str(input("Do you want to buy more shares ? (yes/no) :")).strip().lower()
    print("\n")
    if more_shares != "yes":
        break 
    print("\n")
    print("Your total investment will be Rs.",total)


        

        




