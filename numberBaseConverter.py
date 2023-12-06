


def BinaryToDecimal(numberInput):
    currentExponent = len(numberInput) -1
    numberOutput = 0
    for digit in numberInput:
        numberOutput = numberOutput + int(digit) * (2 ** currentExponent)
        currentExponent -= 1
    return numberOutput

def HexaToDecimal(numberInput):
    currentExponent = len(numberInput) -1
    numberOutput = 0
    for digit in numberInput:
        digit.replace(A, 10)
        digit.replace(B, 11)
        digit.replace(C, 12)
        digit.replace(D, 13)
        digit.replace(E, 14)
        digit.replace(F, 15)
        numberOutput = numberOutput + int(digit) * (16 ** currentExponent)
        currentExponent -= 1
    return numberOutput


def DecimalToHex(numberInput):
    return str(hex(numberInput))[2:]

def DecimalToBinary(numberInput):
    return str(bin(numberInput))[2:]

    







inputType = input("What type is the input? (binary, decimal, hexadecimal) ")
outputType = input("What type is the output? (binary, decimal, hexadecimal) ")
numberInput = input("Input the number: ")
inputNumberList = list(numberInput)

if inputType == "binary":
    decimalNumber = (BinaryToDecimal(inputNumberList))
    if outputType == "binary":
        print (numberInput)
        
    elif outputType == "decimal":
        print (decimalNumber)
        
    elif outputType == "hexadecimal":
        print (DecimalToHex(int(decimalNumber)))
        
elif inputType == "hexadecimal":
    decimalNumber = (HexToDecimal(int(inputNumberList)))
    if outputType == "hexadecimal":
        print (numberInput)
        
    elif outputType == "decimal":
        print (decimalNumber)
        
    elif outputType == "binary":
        print (DecimalToBinary(int(decimalNumber)))
        
if inputType == "decimal":
    if outputType == "decimal":
        print (numberInput)
        
    elif outputType == "hexadecimal":
        print (DecimalToHex(int(numberInput)))
        
    elif outputType == "binary":
        print (DecimalToBinary(int(numberInput)))
