#Question 4(i)
# Create a list of five of your favorite foods. Write a Python program to:
# Add two more items to the list.
# Remove one item from the list.
# Print the updated list.
        #soln
# Initial list of favorite foods
favorite_foods = ["Pizza", "Sushi", "Ice Cream", "Tacos", "Pasta"]

# Adding two more items to the list
favorite_foods.append("Burgers")
favorite_foods.append("Salad")

# Removing one item from the list
favorite_foods.remove("Tacos")

# Printing the updated list
print("Updated list of favorite foods:")
print(favorite_foods)



#Question 4(ii)
# Given the list numbers = [2, 5, 8, 10, 3, 6], write a Python program to:
# Print the first and last elements of the list.
# Print the list in reverse order.
# Calculate and print the sum of all the elements in the list.
      #soln
# Given list of numbers
numbers = [2, 5, 8, 10, 3, 6]

# Print the first and last elements of the list
first_element = numbers[0]
last_element = numbers[-1]
print("First element:", first_element)
print("Last element:", last_element)

# Print the list in reverse order
reversed_list = numbers[::-1]
print("Reversed list:", reversed_list)

# Calculate and print the sum of all the elements in the list
sum_of_elements = sum(numbers)
print("Sum of all elements:", sum_of_elements)
