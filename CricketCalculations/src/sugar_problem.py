#The price of a Kg of sugar is 5 dollars. If a customer buys 150 Kgs or more,
#the Customer gets a discount of 25 dollars, else no discount.

# 100 100 X 5 = 500 
# 150 X 5 = 750 , 150 >= 150 , 25 discount = 25, 725 
# 170 X 5 = 

no_of_kgs_bought=0
sugar_per_kg=5
discount=25
discount_threshold_in_kgs=150
total_bill=0
total_discount=0

no_of_kgs_bought=input('Enter the number of Kilograms of Sugar you want to buy?: ')
total_bill=(int(no_of_kgs_bought) * sugar_per_kg)

if int(no_of_kgs_bought) >= discount_threshold_in_kgs:
    total_bill=total_bill - discount
    total_discount=discount

print("You have to pay "+ str(total_bill)+" dollars.")
print("Discount:"+ str(total_discount))




