import random
from random import randint

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

open = lambda : 0 #Retunerar 0
closed = lambda : 1 #Retunerar 1
is_open = lambda target : True if target == open() else False #Om lika med open() retuneras True, annars False.
is_closed = lambda target : True if target == closed() else False #Om lika med closed() retuneras True, annars False.

def new_target(): #Skpar och retunerar en ny tom lista
    tomlista = []
    for x in range(5):
        tomlista.append(open())
    return tomlista

def close_target(target, targets): #Stänger det givna luckan och retunerar den uppdaterade spelplanen
    targets[target] = closed()
    return targets

def hits(targets): #Räknar och retunerar antalet träffar som man gjort.
    number_of_hits = 0
    for x in targets:
        if is_closed(x):
            number_of_hits += 1
    return number_of_hits

def target_to_string(target): #Retunerar den givna luckan i string-format
    return "* " if is_open(target) else "0 "

def targets_to_string(targets): #Retunerar hela lsitan i string-format
    return list(map(target_to_string, targets))

def view_targets(targets): #Skriver spelplanen
    print("\n1 2 3 4 5")
    for x in targets_to_string(targets):
        print(x, end="") #Slutar på end="" för att inte skapa en ny rad
    return None

def random_hit():
    return True if random.randint(0,1) == open() else False #Slumpar om man träffar eller ej. 50% sannolikhet

def shoot(target, targets):
    hit = random_hit()

    if hit and is_open(targets[target]): #Om den träffar och luckan var öppen
        close_target(target, targets)
        return "\nHit on open target"
    elif hit and is_closed(targets[target]): #Om den träffar och luckan var stängd
        return "\nHit on closed target"
    elif not hit: #Om den missar
        return "\nMiss!"
    return None

def parse_target(string): #Tar emot input från användaren
    if string.isdigit() and int(string) in range(1,6): #Kollar om det det är en siffra och är inom 1-5
        return int(string)-1 #Retunerar i form av int.
    else: #Om inputen inte är en siffra
        return "Invalid target"
    return None

#======== Spelapparaten ==================
splasch() #Skriver ut välkomsmeddelande.
ts = new_target() #Du får en ny tom spelplan

print("\nYou got 5 shots\n----------------") #Instruktioner

view_targets(ts) #Visar spelplanen

actualshot = 0 #Räknar effektiva siffror
antalskott = 5 #Antal skott man har
#antalskott = int(input("Så många skott vill du ha: ")) #Om man vill välja antal skott själv.

while actualshot != antalskott: #Den fortsätter tills man skjutit alla sina skott
    t = parse_target(input(f"\n\nShot {actualshot+1} at: "))
    if t in range(0,5):
        print(shoot(t, ts))
        view_targets(ts) #Visar den uppdaterade spelplanen
        actualshot += 1
    else:
        print(t)

print("\n\nYou hit", hits(ts), "of 5 targets.")

