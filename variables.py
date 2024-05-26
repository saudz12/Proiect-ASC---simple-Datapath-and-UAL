x = 4

BYTESCOUNT = 1
REGISCOUNT = 15
MUXSIZE = 3
OPRSIZE = 5

regInstruc = []
curInstruc = []

selA = []
selB = []
selD = []

opr = []

codes = {
}

registers = []
busA = []
busB = []

output = []

def initializeRegisters():
    global registers
    global codes
    global REGISCOUNT
    global BYTESCOUNT
    global OPRSIZE
    
    for i in range(0, REGISCOUNT+1): #number of registers - depends on number of bits in SELD
        registers += [[]]
        for j in range(0, BYTESCOUNT*8): #number of bits per word
            registers[i] += [0]
    
    codes["LOAD"] = []
    for i in range(0, OPRSIZE):
        codes["LOAD"] += [0]
    
    codes["NOT"] = []
    for i in range(0, OPRSIZE-1):
        codes["NOT"] += [0]
    codes["NOT"] += [1]
        
    codes["NEG"] = []
    for i in range(0, OPRSIZE-2):
        codes["NEG"] += [0]
    codes["NEG"] += [1, 0]
    
    codes["INC"] = []
    for i in range(0, OPRSIZE-2):
        codes["INC"] += [0]
    codes["INC"] += [1, 1]
    
    codes["DEC"] = []
    for i in range(0, OPRSIZE-3):
        codes["DEC"] += [0]
    codes["DEC"] += [1, 0, 0]
    
    codes["OR"] = []
    for i in range(0, OPRSIZE-3):
        codes["OR"] += [0]
    codes["OR"] += [1, 0, 1]
    
    codes["AND"] = []
    for i in range(0, OPRSIZE-3):
        codes["AND"] += [0]
    codes["AND"] += [1, 1, 0]
    
    codes["ADD"] = []
    for i in range(0, OPRSIZE-3):
        codes["ADD"] += [0]
    codes["ADD"] += [1, 1, 1]
    
    codes["SUB"] = []
    for i in range(0, OPRSIZE-4):
        codes["SUB"] += [0]
    codes["SUB"] += [1, 0, 0, 0]
    
    codes["MUL"] = []
    for i in range(0, OPRSIZE-4):
        codes["MUL"] += [0]
    codes["MUL"] += [1, 0, 0, 1]
    
    codes["DIV"] = []
    for i in range(0, OPRSIZE-4):
        codes["DIV"] += [0]
    codes["DIV"] += [1, 0, 1, 0]
    
    codes["XOR"] = []
    for i in range(0, OPRSIZE-4):
        codes["XOR"] += [0]
    codes["XOR"] += [1, 0, 1, 1]
    
    codes["RSH"] = []
    for i in range(0, OPRSIZE-4):
        codes['RSH'] += [0]
    codes['RSH'] += [1, 1, 0, 0]
    
    codes["LSH"] = []
    for i in range(0, OPRSIZE-4):
        codes["LSH"] += [0]
    codes["LSH"] += [1, 1, 0, 1]
    
    codes["LSC"] = []
    for i in range(0, OPRSIZE-4):
        codes["LSC"] += [0]
    codes["LSC"] += [1, 1, 1, 1]
    
    codes["NOR"] = []
    for i in range(0, OPRSIZE - 5):
        codes["NOR"] += [0]
    codes["NOR"] += [1, 0, 0, 0, 0]
    
    codes["NAND"] = []
    for i in range(0, OPRSIZE - 5):
        codes["NAND"] += [0]
    codes["NAND"] += [1, 0, 0, 0, 1]
    
    codes["XNOR"] = []
    for i in range(0, OPRSIZE - 5):
        codes["XNOR"] += [0]
    codes["XNOR"] += [1, 0, 0, 1, 0]
    
    codes["EQ"] = []
    for i in range(0, OPRSIZE - 5):
        codes["EQ"] += [0]
    codes["EQ"] += [1, 0, 0, 1, 1]
    
    codes["LESS"] = []
    for i in range(0, OPRSIZE - 5):
        codes["LESS"] += [0]
    codes["LESS"] += [1, 0, 1, 0, 0]
    
    codes["GRE"] = []
    for i in range(0, OPRSIZE - 5):
        codes["GRE"] += [0]
    codes["GRE"] += [1, 0, 1, 0, 1]
    
    codes["LEQ"] = []
    for i in range(0, OPRSIZE - 5):
        codes["LEQ"] += [0]
    codes["LEQ"] += [1, 0, 1, 1, 0]
    
    codes["GEQ"] = []
    for i in range(0, OPRSIZE - 5):
        codes["GEQ"] += [0]
    codes["GEQ"] += [1, 0, 1, 1, 1]
    
    '''codes["SUB"] = []
    for i in range(0, OPRSIZE - 5):
        codes["SUB"] += [0]
    codes["SUB"] += [1, 1, 0, 0, 0]
    
    codes["SUB"] = []
    for i in range(0, OPRSIZE - 5):
        codes["SUB"] += [0]
    codes["SUB"] += [1, 1, 0, 0, 1]
    
    codes["SUB"] = []
    for i in range(0, OPRSIZE - 5):
        codes["SUB"] += [0]
    codes["SUB"] += [1, 1, 0, 1, 0]
    
    codes["SUB"] = []
    for i in range(0, OPRSIZE - 5):
        codes["SUB"] += [0]
    codes["SUB"] += [1, 1, 0, 1, 1]
    
    codes["SUB"] = []
    for i in range(0, OPRSIZE - 5):
        codes["SUB"] += [0]
    codes["SUB"] += [1, 1, 1, 0, 0]'''
    
    codes["RES"] = []
    for i in range(0, OPRSIZE - 5):
        codes["RES"] += [0]
    codes["RES"] += [1, 1, 1, 0, 1]
    
    codes["IN"] = []
    for i in range(0, OPRSIZE - 5):
        codes["IN"] += [0]
    codes["IN"] += [1, 1, 1, 1, 0]
    
    codes["OUT"] = []
    for i in range(0, OPRSIZE - 5):
        codes["OUT"] += [0]
    codes["OUT"] += [1, 1, 1, 1, 1]
    
'''initializeRegisters()
print(codes)'''