import random
import time
# név
print("Jujutsu Kaisen Karakter Készítő \n")
# Képesség Lista
Jujutsu_Kepeseg = ['Black Flash(common)', 'Black Flash(common)', 'Black Flash(common)', 'Black Flash(common)', 'Black Flash(common)', 'Black Flash(common)', 'Black Flash(common)', 'Cursed Technique Lapse: Blue(rare)', 'Cursed Technique Lapse: Red(rare)', 'Dismantle(rare)',
                   'Idle Transfiguration(rare)', 'Star Rage(epic)', 'Cursed Speech(common)', 'Copy(epic)', 'Disaster Flames(rare)', 'Cleave(rare)', 'Hollow Technique: Purple(epic)', 'blood maipulation(uncommon)',
                   'Ratio(uncommon)', 'Ryoiki Tenkai: Malevolent Shrine(legendary)', 'Ryoiki Tenkai: Unlimited Void(legendary)', 'You have no abilty', 'You have no abilty', 'Ten Shadows(epic)', 'Ratio(common)', 'Ratio(common)', 'Ratio(common)', 'Ratio(common)', 'Ratio(common)', 'Boogie Woogie(rare)',
                   'You have no abilty', 'You have no abilty', 'You have no abilty', 'You have no abilty', 'You have no abilty', 'You have no abilty', 'You have no abilty', 'You have no abilty', 'Ratio(common)', 'Ratio(common)', 'Ratio(common)', 'Ratio(common)', 'Black Flash(common)', 'Black Flash(common)',]
# Klán Lista
Jujutsu_Clan = ['Gojo Clan(legendary)',
                'Zenin Family(epic)', 'Zenin Family(epic)', 'Kamo Family(rare)', 'Kamo Family(rare)', 'Inumaki Family(rare)', 'Inumaki Family(rare)', 'Inumaki Family(rare)', 'Inumaki Family(rare)',
                'Fujiwara Family(uncommon)', 'Fujiwara Family(uncommon)', 'Fujiwara Family(uncommon)', 'Fujiwara Family(uncommon)', 'Fujiwara Family(uncommon)', 'Fujiwara Family(uncommon)',
                'You have no clan', 'You have no clan', 'You have no clan', 'You have no clan', 'You have no clan', 'You have no clan', 'You have no clan', 'You have no clan', 'You have no clan', 'You have no clan', 'You have no clan',
                'You have no clan', 'You have no clan', 'You have no clan', 'You have no clan', 'You have no clan', 'You have no clan', 'You have no clan', 'You have no clan', 'You have no clan', 'You have no clan', 'You have no clan',
                'You have no clan', 'You have no clan', 'You have no clan', 'You have no clan', 'You have no clan', 'You have no clan', 'You have no clan', 'You have no clan', 'You have no clan', 'You have no clan', 'You have no clan', 'You have no clan',]
# Osztáy Lista
Jujutsu_Grade = ['Grade 4', 'Grade 4', 'Grade 4', 'Grade 4', 'Grade 4', 'Grade 4', 'Grade 4', 'Grade 4', 'Grade 4', 'Grade 4', 'Grade 3',
                 'Grade 3', 'Grade 3', 'Grade 3', 'Grade 3', 'Grade 3', 'Grade 3', 'Grade 3', 'Semi-Grade 2', 'Semi-Grade 2', 'Semi-Grade 2', 'Semi-Grade 2', 'Semi-Grade 2', 'Grade 2', 'Grade 2', 'Grade 2', 'Semi-Grade 1', 'Grade 1', 'Special Grade 1',
                 'Special Grade']
# porgetesed szam az elsőrésznél
alap_progetesed = 5
# név
print("Your ability \n")
# pörgetés
progess1 = input("spin to (enter)")
# belépés a while loopba
while progess1 == "" and alap_progetesed == 5 or 4 or 3 or 2 or 1:
    # minden pörgetésél vonjon le egyet
    alap_progetesed = alap_progetesed-1
# randomizált képesség
    Kepesseg = random.choices(Jujutsu_Kepeseg)
# képpesség kiíratása
    for i in Kepesseg:
        print(f"Your Ability is: {i}", end="\n")
# alap progetesed
    print(f"spin you have: {alap_progetesed}")
# maradjon a képesseg vagy ne
    marad = input("stay this abilty?(y/enter to spin):")
    print("")
# ha nincs több progetésed
    if alap_progetesed == 0:
        time.sleep(0.6)
        print("you have no spin\n")
        time.sleep(0.2)
        for i in Kepesseg:
            print(f"Your Ability is: {i}", end="\n")
            time.sleep(0.5)
        break
# ha azt az opciót választja hogy maradjon
    if marad == "y":
        for i in Kepesseg:
            print(f"Your Ability is: {i}", end="\n")
            time.sleep(0.5)
        break
# második rész, úgyan az mint az első csak behelyetsítve
alap_progetesed1 = 5

print("\n Your Clan \n")

progess2 = input("spin to (enter)")


while progess2 == "" and alap_progetesed1 == 5 or 4 or 3 or 2 or 1:

    alap_progetesed1 = alap_progetesed1-1

    Kepesseg1 = random.choices(Jujutsu_Clan)
    for x in Kepesseg1:
        print(f"Your Clan is: {x}", end="\n")
    print(f"spin you have: {alap_progetesed1}")
    marad = input("stay this abilty?(y/enter to spin):")
    print("")
    if alap_progetesed1 == 0:
        time.sleep(0.6)
        print("you have no spin\n")
        time.sleep(0.2)
        for x in Kepesseg1:
            print(f"Your Clan is: {x}", end="\n")
            time.sleep(0.5)
        break

    if marad == "y":
        for x in Kepesseg1:
            print(f"Your Clan is: {x}", end="\n")
            time.sleep(0.5)
        break

# harmadik rész, úgyan az mint az első csak behelyetsítve

alap_progetesed3 = 5
print("")
print("\n Your Grade\n ")

progess3 = input("spin to (enter)")

while progess3 == "" and alap_progetesed3 == 5 or 4 or 3 or 2 or 1:

    alap_progetesed3 = alap_progetesed3-1

    Kepesseg2 = random.choices(Jujutsu_Grade)
    for v in Kepesseg2:
        print(f"Your Grade is: {v}", end="\n")
    print(f"spin you have: {alap_progetesed3}")
    marad = input("stay this abilty?(y/enter to spin):")
    print("")
    if alap_progetesed3 == 0:
        time.sleep(0.6)
        print("you have no spin\n")
        time.sleep(0.2)
        for v in Kepesseg2:
            print(f"Your Grade is: {v}", end="\n")
            time.sleep(0.5)
        break

    if marad == "y":
        for v in Kepesseg2:
            print(f"Your Grade is: {v}", end="\n")
            time.sleep(0.5)
        break
# vége szűnet
time.sleep(0.75)
# végére minden kiíratása
for i in Kepesseg:
    print(f"Your Ability is: {i}\n", end="\n")
for x in Kepesseg1:
    print(f"Your Clan is: {x}\n", end="\n")
# készítő
print("by: Váradi Zsolt")
