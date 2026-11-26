print("=" * 40)
print("          DATA CONVERSION UTILITY")
print("=" * 40)

product_name = input("Enter Product Name: ")
price = float(input("Enter Price: "))
quantity = int(input("Enter Quantity: "))

total_price = price * quantity
amount_str = str(total_price)

print("\n" + "-" * 40)
print("          TYPE CASTING SUMMARY")
print("-" * 40)

print(f"{'Variable':<15}{'Value':<15}{'Python Type'}")
print("-" * 40)
print(f"{'product_name':<15}{product_name:<15}{type(product_name)}")
print(f"{'price':<15}{price:<15}{type(price)}")
print(f"{'quantity':<15}{quantity:<15}{type(quantity)}")
print(f"{'total_price':<15}{total_price:<15}{type(total_price)}")
print(f"{'amount_str':<15}{amount_str:<15}{type(amount_str)}")

print("\n" + "=" * 40)
print("              TAX INVOICE")
print("=" * 40)
print(f"Product Name : {product_name}")
print(f"Price per Unit : Rs. {price:.2f}")
print(f"Quantity       : {quantity}")
print(f"Invoice Total  : Rs. {total_price:.1f}")
print("=" * 40)