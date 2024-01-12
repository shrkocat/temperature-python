# Input Statements
t = float(input("what is your temperature? "))
print("°C->c  °F->f K->k °R->r °Re->re")

w = input("What is the initial unit?: ")

u = input("What is the new unit?: ")

# Conversion Statements for Celsius
if w == "c":
    if u == "f":
        r = round((t * 9/5) + 32, 1)
        u = "°F"
        
    elif u == "k":
        r = round(t + 273.15, 1)
        u = "K"
        
    elif u == "r":
        r = round((t * 9/5)+491.67, 1)
        u = "°R"
        
    elif u == "re":
        r = round((t*4)/5, 1)
        u = "°Re"
        
    elif u == "c":
        r = t
        print("no convertion happened")
        
    else:
        r = 0
        print("This is not a valid unit for this converter!")

# Conversion Statements for Fahrenheit
if w == "f":
    if u == "c":
        r = round((t * 5/9) - 32, 1)
        u = "°C"
        
    elif u == "k":
        r = round((5/9 * t)+ 459.67, 1)
        u = "K"
        
    elif u == "r":
        r = round(t +491.67, 1)
        u = "°R"
        
    elif u == "re":
        r = round((t-32)*49)
        u = "°Re"
        
    elif u == "f":
        r = t
        print("no convertion happened")
        
    else:
        r = 0
        print("This is not a valid unit for this converter!")

# Conversion Statements for Kelvin
if w == "k":
    if u == "c":
        r = round(t - 273.15, 1)
        u = "°C"
        
    elif u == "f":
        r = round((t - 273.15) * 9 / 5 + 32, 1)
        u = "°F"
        
    elif u == "k":
        r = round((t - 273.15)*(1.8+491.67), 1)
        u = "K"
        
    elif u == "re":
        r = round((t - 273.15) * 0.8)
        u = "°Re"
        
    elif u == "k":
        r = t
        print("no convertion happened")
        
    else:
        r = 0
        print("This is not a valid unit for this converter!")

# Conversion Statements for Rankine
if w == "r":
    if u == "c":
        r = round((t*9/5)+491.67 , 1)
        u = "°C"
        
    elif u == "f":
        r = round(t+ 459.67, 1)
        u = "°F"
        
    elif u == "r":
        r = round(1.8 * t, 1)
        u = "°R"
        
    elif u == "re":
        r = round((t - 32 - 459.67) / 2.25, 1)
        u = "°Re"
        
    elif u == "r":
        r = t
        print("no convertion happened")
        
    else:
        r = 0
        print("This is not a valid unit for this converter!")

# Conversion Statements for Réaumur
if w == "re":
    if u == "c":
        r = round(t*1.25, 1)
        u = "°C"
        
    elif u == "f":
        r = round(t * 94 + 32, 1)
        u = "°F"
        
    elif u == "k":
        r = round(1.25 * t + 273.15, 1)
        u = "K"
        
    elif u == "re":
        r = round((t - 32 - 459.67) / 2.25, 1)
        u = "°Re"
        
    elif u == "re":
        r = t
        print("no convertion happened")
        
    else:
        r = 0
        print("This is not a valid unit for this converter!")

# Final Output 
print(f"the new temperature is: {r} {u}" )
