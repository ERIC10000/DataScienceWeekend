# Python Collections/Arrays
# List -> syntax for creating list []
# properties -> ordered, modifiable/mutable, allow duplicates

countries = ["Kenya", "Uganda", "Ethiopia", "Tanzania", "Rwanda"]
print(type(countries))

# List Operations
# 1.Printing items
print(countries)
# 2.Specific Items
# Indexing -> starts from zero []
print(countries[2])
print(countries[4])
# Print out a range of values
# range [:], full colon
# first item is included, last excluded
print(countries[1:4])
print(countries[:])

# Add/Update
# add -> append(), insert()

countries.append("S.Sudan")
print(countries)

countries.insert(2, "DRC")
print(countries)

# extend() -> Adds a list to another list
newList = ["Nigeria", "Gambia", "Morrocco", "Ghana"]
countries.extend(newList)
print(countries)

# Updates
countries[2] = "S.Africa"
print(countries)

# Remove
# remove(), pop()

countries.remove("S.Africa")
print(countries)

countries.pop(3)
print(countries)
# clear
countries.clear()
print(countries)
# del
del countries
print(countries)
