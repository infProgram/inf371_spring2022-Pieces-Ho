def convertCelciusToFahrenheit(cel):
    F = 1.8*cel+32
    return F

if __name__ == "__main__":
    isRunning = True
    while isRunning:
        cel = input("Input the Celcius: ")
        Fa = convertCelciusToFahrenheit(float(cel))
        print("The Fahrenheit is:" , Fa)
        q = input("Quit now? (input Q)")
        if q == 'q'or q =='Q':
            isRunning = False
    



    
