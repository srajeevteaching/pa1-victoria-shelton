#Team Members: Victoria Shelton
#Course: CS151, Dr.Rajeev
#Date: 9/22/21
#Programming Assignment: 1
#Program Inputs: Length, width, and height of a room in feet.
#Program Outputs: Amount of primer and paint needed in gallons.

#Program asks user to input dimensions and converts the inputs to floats.
print("Please input the dimensions of the room.")
length = float(input("Input length: "))
width = float(input("Input width: "))
height = float(input("Input height: "))

#Program calculates total area to be painted and amount of primer and paint needed.

area = (length*width)+(length*height*2)+(width*height*2)
primer = area / 200
paint = area / 350

#Program outputs total area to be painted and amount of primer and paint needed.

print("The total area to be painted is: " + str(area) + " sqft.")
print("The amount of primer needed is: " + str(primer) + " gallons.")
print("The amount of paint needed is: " + str(paint) + " gallons.")