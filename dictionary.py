mycar = {
    "brand" : "lambhorgini", 
    "model" : "Aventador",
    "year"  : 2019,
    "color" : "Black"
}

print(mycar)

#Accessing
print(mycar['model'])
print(mycar["color"])

#Changing
mycar['color'] = 'Red'
print(mycar['color'])

mycar['year'] = '2020'
print(mycar['year'])

#looping
for key in mycar:
    print(key, "=", mycar[key])

#Check if exist 
if "color" in mycar:
    print("The dictionary contains the key called Color")

#Dictionary Length
print(len(mycar))

#Adding items to the dictionary
mycar['Power'] = "700 BHP"
print(mycar)

#Removing an item from dictionary 
mycar.pop('color')
print(mycar)

#Make the dictionary empty
mycar.clear()
print(mycar)

#Deleting the empty dictionary
del mycar 
print(mycar)