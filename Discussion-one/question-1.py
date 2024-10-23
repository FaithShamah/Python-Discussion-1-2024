# Question 1(i)
# Temperature Classifier: Using a function, write a Python script that takes a temperature as input and classifies it into the 
# following categories: 
# Below 0°C: Freezing
# 0 to 10°C: Cold 
# 11 to 20°C; Moderate 
# 21 to 30°C: Warm 
# Above 30°C: Hot 
         #Soln
def temperature_classifier(temp):
    if temp < 0:
        return "Freezing"
    elif 0 <= temp <=10:
        return "Cold"
    elif 11 <= temp <= 20:
        return "Moderate"
    elif 21 <= temp <= 30:
        return "Warm"
    else: 
        return "Hot"
try:
    temperature = float(input("Enter the temperature in °C: "))
    classification = temperature_classifier(temperature)
    print(f"The temperature is classified as: {classification}")
except ValueError:
    print("Please enter a valid number")
    
    
# Question 1(ii)
# The volume of a sphere with radius r is (4/3)*pie*r**3. What is the volume of the sphere with radius 8. 
# Use a function and make sure the radius is entered from the keyboard and provide the answer in 1 decimal place
      #Soln
import math
def calculate_volume_of_the_sphere(radius):
    volume = (4/3) * math.pi * radius ** 3
    return volume
radius = float(input("Enter the radius of the sphere: "))
volume = calculate_volume_of_the_sphere(radius)
print(f"The volume of the sphere with radius{radius} is {volume:.1f}")