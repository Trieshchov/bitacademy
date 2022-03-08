password_value = "baas"
ged_password_value = "medewerker"
input_password = input("Enter Password: ")
if password_value == input_password:
    print("Totale toegang")
elif ged_password_value == input_password:
    print("Gedeeltelijke toegang")
else:
    print("Geen toegang")
