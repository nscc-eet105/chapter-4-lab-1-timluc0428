#Tim Lucas
#Lab4-1
#2025 06 __


#main function prompts user to enter temperature
#asks user if Celsius or Fahrenheit
#call correct function to convert tempt
#if an invalid value is entered an error message should be displayed
    #and the user should be prompted to enter valid date 
#program should not end until valid input entered.
def main()
    
    temperature = int(input("What is the current temperature? "))
    f_or_c = input("Is the temperature Celsius or Fahrenheit (c or f): ")
    While True:
        if f_or_c.lower() = "f":
            fahrenheit_to_celsius()
                ...
        elif: f_or_c = "c"
            celsius_to_fahrenheit(temperature)
                ...
        else:
            print("Please enter a c or f")
        
#void function has Celsius as argument passed to it and converts to Fahrenheit 
#and prints value
def celsius_to_fahrenheit(temp)
    ftemp = (temp * 9/5) + 32
    print(ftemp)
    
#value returning function that has Fahrenheait passed to it and and converts to Celsius
# and returns its value   
def fahrenheit_to_celsius()


main()

