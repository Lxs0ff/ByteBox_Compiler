import subprocess
from datetime import datetime

try:
    import mcshematic
except:
    print("McShem library not found, importing library...")
    subprocess.run(["python3","-m","pip", "install", "mcschematic"]) 
    import mcschematic

x = 0
y = 0
z = 0
line_count = 0
schem = mcschematic.MCSchematic()

bin_file = open('output.txt', "r")
bin_lines = bin_file.readlines()

for line in bin_lines:
    line_count += 1
    if line_count > 1:
        if line_count == 17:
            y = -1
            x = 0
            z = 8
        else:
            x += 4
    if line_count > 32:
        break
    for bit in line:
        y -= 2
        if line_count == 1:
            y = -1
        if bit == 0:
            schem.place()
        else:
            if bit == 1:
                schem.setBlock( (x,y,z) , "minecraft:redstone_block")
            else:
                schem.setBlock( (x,y,z) , "minecraft:air")

now = datetime.now()
current_time = now.strftime("%H_%M")
schem.save(  "schematics", current_time + "_code", mcschematic.Version.JE_1_19_4)