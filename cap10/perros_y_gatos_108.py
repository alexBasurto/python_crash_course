filename_1 = "cap10\\perross.txt"
filename_2 = "cap10\\gatos.txt"
files =[filename_1, filename_2]

for file in files:
    try:
        with open(file, "r", encoding="utf-8") as f:
            lines = f.read()

    except FileNotFoundError:
        #print(f"\nEl fichero con nombre {file} no existe.")
        pass

    else:
        print(f"\n{file}")
        print(lines)