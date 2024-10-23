   # Question 2(i)
# Define a function named calculate_bmi that takes a person's weight (in kilograms) and height (in 
# meters) as parameters and returns their BMI. (BMI = weight/height) 
# Calculate and sen their BMI category: 
# Below 18.5: "Underweight" 
# 18.5 to 24.9: "Normal weight" 
# 25 to 29.9: "Overweight" 
# 30 or above: "Obese" 
            #soln
def calculate_bmi(weight, height):
    # Calculate BMI
    bmi = weight / (height ** 2)
    
    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    return bmi, category

# Example usage:
weight = 70  # in kilograms
height = 1.75  # in meters
bmi, category = calculate_bmi(weight, height)
print(f"BMI: {bmi:.2f}, Category: {category}")

         
         
# Question 2(ii)
# Use a function to calculate the volume of a cylinder V = π r2 h. Choose a function name in line with what you want to 
# achieve. Radius r and height h should be in parameters. Make sure you use the real pie value (import math)
              #soln
import math

def calculate_cylinder_volume(radius, height):
    """Calculate the volume of a cylinder given its radius and height."""
    volume = math.pi * (radius ** 2) * height
    return volume

# Example usage:
r = 5  # radius
h = 10  # height
volume = calculate_cylinder_volume(r, h)
print(f"The volume of the cylinder is: {volume:.2f}")
