kuukaudet = ("tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu", "marraskuu", "joulukuu")
while True:
    #lisätty tarkistusluuppi siltä varalta, ettei käyttäjä anna järkevää numeroa
    jarjestysnumero = int(input("Anna kuukauden numero (1-12): "))
    if jarjestysnumero == 0 or jarjestysnumero not in range(len(kuukaudet) + 1):
        print("Valitse numero väliltä 1-12")
    else:
        break
kuukausi = kuukaudet[jarjestysnumero-1]
if kuukausi == "joulukuu" or kuukausi == "tammikuu" or kuukausi == "helmikuu":
    print(kuukausi, "on talvella")
elif kuukausi == "maaliskuu" or kuukausi == "huhtikuu" or kuukausi == "toukokuu":
    print(kuukausi, "on keväällä")
elif kuukausi == "kesäkuu" or kuukausi == "heinäkuu" or kuukausi == "elokuu":
    print(kuukausi, "on kesällä")
elif kuukausi == "syyskuu" or kuukausi == "lokakuu" or kuukausi == "marraskuu":
    print(kuukausi, "on syksyllä")
