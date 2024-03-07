import random

def maarata_voitja(mangija1, mangija2):
    if mangija1 == mangija2:
        return "Viik!"
    elif (mangija1 == "kivi" and mangija2 == "kaarid") or (mangija1 == "paber" and mangija2 == "kivi") or (mangija1 == "kaarid" and mangija2 == "paber"):
        return "Mangija voidab!"
    else:
        return "Robot voidab!"

def mangimine(rezhiim):
   mangijad = ["Mangija 1", "Robot"] if rezhiim == "robot" else ["Mangija 1", "Mangija 2"]
   tulemused = []

   for _ in range(3):
        mangija1_valik = input(f"{mangijad[0]}, sisestage oma valik (kivi, paber, kaarid): ").lower()

        if rezhiim == "robot":
            mangija2_valik = random.choice(["kivi", "paber", "kaarid"])
            print(f"{mangijad[1]} valis: {mangija2_valik}")
        else:
            mangija2_valik = input(f"{mangijad[1]}, sisestage oma valik (kivi, paber, kaarid): ").lower()

        tulemus = maarata_voitja(mangija1_valik, mangija2_valik)
        tulemused.append(tulemus)
        print(tulemus)

   return tulemused

while True:
    rezhiim = input("Vali rezhiim (robot/inimene): ").lower()
    mangu_tulemused = mangimine(rezhiim)

    Mangija1_voidab = mangu_tulemused.count("Mangija 1 voidab!")
    Mangija2_voidab = mangu_tulemused.count("Mangija 2 voidab!")

    if Mangija1_voidab > Mangija2_voidab:
        print("Mangija 1 voidab mangu!")
    elif Mangija2_voidab > Mangija1_voidab:
        print("Mangija 2 voidab mangu!")
    else:
        print("Viik!")

    mangi_uuesti = input("Kas sa tahad uuesti mangida? (jah/ei): ")
    if mangi_uuesti.lower() != "jah":
        break

