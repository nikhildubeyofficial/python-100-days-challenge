# f-strings in python

letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Nikhil"

print(letter.format(name,country))

print(f"Hey my name is {name} and I am from {country}")

price = 49.9990909
print(f"For only {price:.2f} dollars!")

print(f"{2*30}")