# Dictionaries -> values pairs (key, value), syntax {} braces
# Properties -> ordered, modifiable, no duplicate values

phone = {"name": "Samsung Fold",
         "memory": 16,
         "storage": 256,
         "color": ["red", "gold", "black"],
         "owner": {"name": "Joseph",
                   "contacts": [712345678, "joseph@gmail.com"]
                   },
         "location": "Sarit Center",
         "IMEI": 1.23456,
         "isBought": False,
         "isBrand": True

         }

print(type(phone))

# Dictionary Operations
print(phone)
# keys

print(phone.keys())
print(phone.values())
print(phone.items())

print(phone["owner"])
print(phone["storage"])

# Add/Update
phone["storage"] = 128
print(phone["storage"])

phone["color"][1] = "Blue"
print(phone)

# In dictionary phone traverse to reach owner email and update the email
phone["owner"]["contacts"][1] = "new@gmail.com"
print(phone)
