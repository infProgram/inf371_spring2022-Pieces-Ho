def convertCelciusToFahrenheit(cel):
    print("convert!")

if __name__ == "__main__":
    isRunning = True
    while isRunning:
        cel = input("Input the Celcius.")
        convertCelciusToFahrenheit(cel)
        q = input("Quit now? (input Q)")
        if q == 'q'or q =='Q':
            isRunning = False
    



    
