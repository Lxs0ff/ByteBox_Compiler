import os
import subprocess
import time

opcodes = {
    "load":"00001",
    "store":"00010",
    "add":"00011",
    "subtract":"00100",
    "increment":"00101",
    "decrement":"00110",
    "or":"00111",
    "and":"01000",
    "xor":"01001",
    "invert":"01010",
    "shiftup":"01011",
    "shiftdown":"01100",
    "video":"01101",
    "out":"01110",
    "in":"01111",
    "jump":"10000",
    "jumpif":"10001",
    "passth":"10010",
    "halt":"10011",
    "ldi":"10100",
    "sdi":"10101",
    "nor":"10110",
    "nand":"10111",
    "xnor":"11000",
    #"":"11001",
    "resetreg":"11010",
    #"":"11011",
    #"":"11100",
    #"":"11101",
    #"":"11110",
    #"":"11111"
}

total_time = 0
line_count = 0

in_file = open('input.txt', "r")
lines = in_file.readlines()

os.remove('output.txt')
out_file = open('output.txt', "a")

def error():
    end_time = time.time
    total_time = end_time - start_time
    print("There was an error in the code at line: " + line_count)
    print("After " + total_time + " seconds")
    in_file.close
    out_file.close
    os.remove('output.txt')
    time.sleep(10)
    exit()
    return

start_time = time.time
for line in lines:
    line_count += 1
    if line_count < 32:
        newline = ""
        words = line.split(' ')
        for x in words:
            if not x.isnumeric:
                x = int(x)
                if x < 256:
                    x = bin(x)
                    if int(x) > 0:
                        x = x.removeprefix("0b")
                    else:
                        x = x.removeprefix("1b")
                else: 
                    error()
            else:
                x.lower()
                if x in opcodes:
                    x = opcodes.get(x)
                else:
                    error()
            newline += x
        out_file.write(newline + '\n')
        print(newline)
    else:
        break

end_time = time.time
total_time = end_time - start_time

in_file.close
out_file.close
print("Compiling Sucessfull in " + total_time + "seconds")
schem_question = input("Do you want to convert to a schematic(y/n): ")
if schem_question == "y" or schem_question == "Y":
    subprocess.run(["python", "out_to_mcschem.py"])
print("Exiting in 10 seconds...")
time.sleep(10)