
#for loops

items=[]
prices=[]
item_name="none"
price=0
for i in range(3):
    item_name=input("Enter item name:")
    price=input("Enter price:")
    items.append(item_name)
    prices.append(int(price))

total_price=0

for i in range(3):
    print("Item is "+items[i])
    print("Item price is "+ str(prices[i]))
    total_price = total_price + prices[i]

print("Your total bill is: "+str(total_price))

































'''choice='y'



'''
#choice='y'
#for i in range(10):
#    print(i)
