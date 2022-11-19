counties = ["Nairobi", "Nyeri", "Uasin Gishu", "Kericho", "Trans Nzoia", "Nakuru",
            "Homa Bay", "Mombasa", "Taita Taveta", "Nyandarua", "Kilifi"]
print(len(counties))

single_names = []
double_names = []

 # if len(county.split()) == 2
# single = no space
# double = " " a space

for county in counties:
    # if " " in county:
    #     double_names.append(county)
    if len(county.split()) == 2:
        double_names.append(county)

    else:
        single_names.append(county)

print(single_names)
print("================")
print(double_names)

# Search in Collections using for loops and decisions
languages = ["PHP", "Java", "Python", "JavaScript", "R", "C#"]
for langauge in languages:
    if langauge == "R":
        print("R is Found")
    else:
        print(langauge)
# Functions
# Libraries/Modules


# Explanatory Data Analysis
# Reading a dataset to colab
# Understanding data
# Analysis- > Insights

# Library -> pandas
