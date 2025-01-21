with open("students.txt", "w") as file:
 
    file.write("mia\n")
    file.write("hessa\n")
    file.write("noli\n")
    file.write("astrid\n")
    file.write("rudy\n")
    file.write("bor\n")
    file.write("feliciy\n")
    file.write("eva\n")
    file.write("yazzi\n")
    file.write("Nati\n")
    file.write("leo\n")
    file.write("Lavinia\n")
    file.write("Abdulmohsen\n")
    file.write("yahya\n")
    file.write("jeston\n")
    file.write("aleks b\n")
    file.write("aleks h\n")
    file.write("francis\n")
    file.write("andres\n")
    file.write("mateo\n")
    file.write("pascal\n")
    file.write("colin\n")
    
with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())
        print(line[1])
 
new_line = input("Enter a new name:")
 
with open("students.txt", "a") as file:
    file.write(new_line + "\n")
 
with open("students.txt", "r") as file:
    for line in file:
        print(line.split(",",1)[0].strip())
 
with open("students.txt", "r") as file:
    for line in file:
        if len(line)>6:
            print(line)
