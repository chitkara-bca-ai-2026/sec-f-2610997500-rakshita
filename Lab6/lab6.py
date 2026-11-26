#SHOP BILLING SYSTEM

item=input("enter the Item name:")
price=float(input("Enter the Price per unit:"))
quantity=int(input("Enter the Quantity:"))
total_amount = price*quantity
print(total_amount  )
if total_amount>5000:
    print("discount=20%")
    discount_amount=total_amount*0.2
elif total_amount>2000:
    print("discount=10%")
    discount_amount=total_amount*0.1
elif total_amount>1000:
    print("discount=5%")
    discount_amount=total_amount*0.05
else:
    print("discount=0%")