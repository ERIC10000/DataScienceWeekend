# Python Tuples -> syntax () brackets
# properties -> ordered, immutable/unmodifiable, allow duplicates

countries = ("Kenya", "Uganda", "Ethiopia", "Tanzania", "Rwanda")
print(type(countries))
country = ("S.Africa",)
print(type(country))

# Operations
print(countries)
print(countries[3])

print(countries[1:3])

list_countries = list(countries)
print(list_countries)

list_countries.append("S.sudan")
print(list_countries)

countries = tuple(list_countries)
print(countries)
