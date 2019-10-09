import random

def splasch():
    print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("      Welcome to Splasch\n\n\n    - A hit or miss game -")
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return None #Enligt uppgiften måste den retunera None

def open():
    return 0

def closed():
    return 1

def is_open(target):
    if target == open(): #Måste jämföras med funktionen open()
        return True
    return False

def is_closed(target):
    if target == closed(): #Måste jämföras med funktionen closed()
        return True
    return False

def new_target():
    tomlista = []
    for x in range(5):
        tomlista.append(open()) #Måste använda funktionen open()
    return tomlista

def close_target(target, targets):
    targets[target] = closed()
    return targets

def hits(targets):
    y = 0
    for x in targets:
        if is_closed(x): #Måste använda funktionen is_closed
            y += 1
    return y

def target_to_string(target):
    if is_open(target):
        return "* "
    elif is_closed(target):
        return "0 "

def targets_to_string(targets):
    nylista = []
    for x in targets:
        nylista.append(target_to_string(x))
    return nylista

def view_targets(targets):
    print("\n1 2 3 4 5")
    for x in targets_to_string(targets):
        print(x, end="")
    return None

def random_hit():
    if random.randint(0,1) == open():
        return True
    return False

def shoot(target, targets):
    hit = random_hit()

    if hit and is_open(targets[target]):
        close_target(target, targets)
        return "\nHit on open target"
    elif hit and is_closed(targets[target]):
        return "\nHit on closed target"
    elif not hit:
        return "\nMiss!"
    return None

def parse_target(string):
    if string.isdigit() and int(string) in range(1,6): #Range 1-5 tar emot allt mellan 1-5
        return int(string)-1
    else:
        return "Invalid target"
    return None

#======== Spelapparaten ==================
splasch() #Skapar ett nytt spel
ts = new_target() #Du får en ny tom spelplan

print("\nYou got 5 shots\n----------------") #Instruktioner

view_targets(ts)

actualshot = 0 #Räknar effektiva siffror

while actualshot != 5:
    t = parse_target(input(f"\n\nShot {actualshot+1} at: "))
    if t in range(0,5):
        print(shoot(t, ts))
        view_targets(ts) #Visar den uppdaterade spelplanen
        actualshot += 1
    else:
        print(t)


print("\n\nYou hit", hits(ts), "of 5 targets.")
