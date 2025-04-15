# Define a function to calculate the discount
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or more
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = (discount_percent / 100) * price
        # Subtract the discount from the original price
        final_price = price - discount_amount
        return final_price
    else:
        # If discount is less than 20%, return the original price
        return price

# Ask the user to enter the original price
price_input = input("Enter the original price of the item: ")
# Ask the user to enter the discount percentage
discount_input = input("Enter the discount percentage: ")

# Convert inputs from string to float
price = float(price_input)
discount_percent = float(discount_input)

# Call the function to get the final price
final_price = calculate_discount(price, discount_percent)

# Show the result
if discount_percent >= 20:
    print("Discount applied!")
    print("The final price is: $" + str(round(final_price, 2)))
else:
    print("No discount applied.")
    print("The price remains: $" + str(round(final_price, 2)))
