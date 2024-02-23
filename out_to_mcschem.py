import subprocess
from datetime import datetime

try:
    import mcschematic
except:
    print("McShem library not found, importing library...")
    subprocess.run(["pip", "install", "mcschematic"]) 

x = 0
y = 0
z = 0
schem = mcschematic.MCSchematic()

bin_file = open('output.txt', "r")
bin_lines = bin_file.readlines()

for line in lines:
    line_count += 1
    if line_count > 1:
        if line_count == 17:
            y = -1
            x = 
            z =
        else:
            += 4
    if line_count > 32:
        break
    for bit in line:
        y -= 2
        if line_count == 1:
            y = -1
        if bit = 0:
            schem.place()
        else:
            if bit = 1:
                schem.setBlock( (x,y,z) , "minecraft:redstone_block")
            else:
                schem.setBlock( (x,y,z) , "minecraft:air")

now = datetime.now()
current_time = now.strftime("%H:%M")
schem.save(  "code_schems", current_time + "_code", mcschematic.Version.JE_1_19_4)