#Tim Lucas
#Lab4-1
#2025 06 __


#main function prompts user to enter temperature
#asks user if Celsius or Fahrenheit
#call correct function to convert tempt
#if an invalid value is entered an error message should be displayed
    #and the user should be prompted to enter valid date 
#program should not end until valid input entered.

def celsius_to_fahrenheit(temp):
    ftemp = (temp * 9/5) + 32
    print(f"The current temperature is {temp:.1f} celsius. This temperature in Fahrenheit is {ftemp:.2f} degrees")
    
#value returning function that has Fahrenheait passed to it and and converts to Celsius
# and returns its value   
def fahrenheit_to_celsius(temp):
    ctemp = (temp - 32) * 5/9
    return ctemp


def main():
    
    temperature = float(input("What is the current temperature? "))
    while True:
        f_or_c = input("Did you enter the temperature in (c)elsius or (f)ahrenheit? ")
        if f_or_c.lower() == "f":
            celtemp = fahrenheit_to_celsius(temperature)
            print(f"The current temperature is {temperature:.1f} fahrenheit. This temperature in celsius is {celtemp:.2f} degrees.")
            break
    
        elif f_or_c == "c":
            celsius_to_fahrenheit(temperature)            
            break
    
        else:
            print("Invalid input, Please enter a c or f")
        
#void function has Celsius as argument passed to it and converts to Fahrenheit 
#and prints value

main()

