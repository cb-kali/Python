Atm_Pin = {"Name":"Udit","Pin":1234567890}
# key --> name
# value --> pin
print(Atm_Pin['Name'])
# Access the value by using Key(Name)
New_Pin = Atm_Pin['Pin']
print(f"You enter {New_Pin} this pin . ")
# Access the key by the value 
print(Atm_Pin["Name"])
# continue with dictionary data typ: Now to modify dictionary.
Atm_Pin = {"Name":"Udit","Pin":1234567890}
# Req --> Modifty Nmae and Position
Atm_Pin['name'] = "Roshan"
print(Atm_Pin)
# Modify the pin to get as 1234567891
Atm_Pin["pin"] = 1234567891
print(Atm_Pin)
# Req --> printing the modified pin
print(f"You enter {Atm_Pin['Pin']} this pin .")
Fav_lang = {"Roshan":"Java","Udit":"C","Shali":"C++"}
print(Fav_lang)
lang = Fav_lang["Roshan"].title()
print(f"Roshan favourite language is {lang}.")
