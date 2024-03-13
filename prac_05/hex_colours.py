COLOR_TO_CODE = {"Amber": "#ffbf00", "Aqua": "#00ffff", "Baby Blue": "#89cff0", "Beige": "#f5f5dc",
                 "Black": "#000000", "White": "#ffffff"}
print(COLOR_TO_CODE)
colour_name = input("Enter color name: ").title()
while colour_name != '':
    try:
        print(colour_name, "is", COLOR_TO_CODE[colour_name])
    except KeyError:
        print("Invalid color name")
    colour_name = input("Enter color name: ").title()
