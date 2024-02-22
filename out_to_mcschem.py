import subprocess
from datetime import datetime

try:
    import mcschematic
except:
    print("McShem library not found, importing library...")
    subprocess.run(["pip", "install", "mcschematic"]) 

schem = mcschematic.MCSchematic()

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
schem.save(  "code_schems", current_time + "_code", mcschematic.Version.JE_1_19_4)