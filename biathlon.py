import random

def splash():
    print(
            '''
            \n\n\n
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            \n
                    Welcome to Splasch   
                  \n\n\n 
                  - A hit or miss game -
            \n
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            '''
         )
    return None #Enligt uppgiften måste den retunera None

def open():
    return 0

def closed():
    return 1

def is_open(target):
    return True if target == open() else False

def is_closed(target):
    return True if target == closed() else False

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
    return "* " if is_open(target) else "0 "

def targets_to_string(targets):
    return list(map(target_to_string, targets))

def view_targets(targets):
    print("\n1 2 3 4 5")
    for x in targets_to_string(targets):
        print(x, end="")
    return None

def random_hit():
    return True if random.randint(0,1) == open() else False

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
splash() #Skapar ett nytt spel
ts = new_target() #Du får en ny tom spelplan

print("\nYou got 5 shots\n----------------") #Instruktioner

view_targets(ts)

actualshot = 0 #Räknar effektiva siffror

#antalskott = int(input("Så många skott vill du ha: "))
antalskott = 5

while actualshot != antalskott:
    t = parse_target(input(f"\n\nShot {actualshot+1} at: "))
    if t in range(0,5):
        print(shoot(t, ts))
        view_targets(ts) #Visar den uppdaterade spelplanen
        actualshot += 1
    else:
        print(t)


print("\n\nYou hit", hits(ts), "of 5 targets.")
