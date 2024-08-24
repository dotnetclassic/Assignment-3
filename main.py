from datetime import date


#calculate your age based on the current year and your birth year.

dobYear = input("Enter your birth year: ")
today = date.today().year
diff = today - int(dobYear)

print(diff)

#Write a program that calculates the area of a rectangle using length and width variables
length = 10
width = 20
area = length * width #length * width
print("Area of rectangle:", area) #200

#Write a program that calculates the area of a circle.

radius = int(input("Enter radius: "))  #example radius of circle
area = 3.14 * radius * radius #pi * r^2
print("Area of circle:", area) #314.0

#Write a program that calculates the area of the cube.
side = int(input("Enter side: "))
area = 6 * side * side #6 * side^2
print("Area of cube:", area) #600


#Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable.
fahrenheit = int(input("Enter temperature in Fahrenheit: ")) #100
celsius = (fahrenheit - 32) * 5/9 #(F - 32) * 5/9
print("Celsius:", celsius) #37.77777777777778

#Convert a given number of seconds into minutes and seconds using variables.
seconds = 1000
minutes = seconds // 60
remainingSeconds = seconds % 60 #1000 % 60 = 40
print("Minutes:", minutes, "Seconds:", remainingSeconds) #16 40

#Write a program that calculates the percentage.
totalMarks = 100
obtainedMarks = 80
percentage = (obtainedMarks / totalMarks) * 100
print("Percentage:", percentage) #80.0%

