
import time


stan = {
    "metoda_nauki": None,
    "imie" : None
}

import random 

tipy = [
    "Rób mikrocele zamiast dużych celów - rozbij zadania na jak najmniejsze etapy.",
    "Jeśli możesz, zmień miejsce nauki - nowy bodziec to nowe skupienie.",
    "Weź 3 głębokie wdechy i zmuś się do powolnego wydechu - to reset dla układu nerwowego.",
    "W mózgu nie da się zbudować pałacu w godzinę - zrób fundament.",
    "Nikt nie ogarnia życia w 100% - Odstresuś tym bardziej."
]

def cwiczenia_oddechowe():
    print("Odstresuś: Ile razy chcesz wykonać te ćwiczenia? ( jeden raz - jeden wdech – wydech)")
    odpowiedz2 = int(input("Ty: "))

    if odpowiedz2 < 1:
        print("Odstresuś: widzę, że nie masz aktualnie wystarczająco czasu na ćwiczenie oddechowe, napisz jak znajdziesz trochę czasu")
    else:
        print("Odstresuś: super, zaczynamy ćwiczenie oddechowe")
        rundy = odpowiedz2

        for i in range(rundy):
            print(f"\nRunda {i+1}")
            print("Weź wdech...")
            time.sleep(3)
            print("Teraz wydech...")
            time.sleep(3)
        
        print("\nOdstresuś: ćwiczenie zakończone!")

def stres_egzaminem():
     print("Odstresuś: Potrzebujesz się narazie zrelaksować, czy chcesz się lepiej przygotować do zaliczenia")
     odpowiedz3 = input("Ty:")

     if "przygotować" in odpowiedz3.lower():
         if stan["metoda_nauki"]:
            print(f"Odstresuś: Ostatnio zapisałem, że lubisz metodę {stan['metoda_nauki']}, nadal chcesz jej używać, czy chcesz spróbować jakiejś innej?")
         else: print("Odstresuś: Co myślisz o tym żebym wypisał Ci najlepsze sposoby na naukę")
         odpowiedz4 = input("Ty: ")
         if "super" in odpowiedz4.lower() or "dobry" in odpowiedz4.lower():
            print("Odstresuś: Oto najlepsze sposoby na naukę:")
            print("- metoda Pomodoro,")
            print("- spaced repetition,")
            print("- technika Feynmana,")
            print("- active recall,")
            print("- dual coding")
            print("chcesz się dowiedzieć, więcej o którejś z metod? (tak/ nie)")
            odpowiedz6 = input("Ty: ")
            
            if "tak" in odpowiedz6.lower():
                print("Odstresuś: super, o której?")
                odpowiedz7 = input("Ty: ")

                if "pomodoro" in odpowiedz7.lower():
                    print("Odstresuś: uczysz się 25 minut w pełnym skupieniu, potem robisz 5 minut przerwy. Po 4 rundach robisz przerwę 15 minut.")
                    print("Co myślisz o tej metodzie nauki?")
                    odpowiedz8 = input("Ty: ")
                    if "super" in odpowiedz8.lower() or "podoba" in odpowiedz8.lower():
                        print("super, zapisuję, że lubisz tą metodę")
                        stan["metoda_nauki"] = "metoda Pomodoro"
                    if "nie" in odpowiedz8.lower():
                        print(":/")

        
                if "repetition" in odpowiedz7.lower():
                    print("Odstresuś: uczysz się czegoś i powtarzasz to po określonych, coraz większych odstępach czasu.")
                    print("Co myślisz o tej metodzie nauki?")
                    odpowiedz9 = input("Ty: ")
                    if "super" in odpowiedz9.lower() or "podoba" in odpowiedz9.lower():
                        print("super, zapisuję, że lubisz tą metodę")
                        stan["metoda_nauki"] = "spaced repetition"
                    if "nie" in odpowiedz9.lower():
                        print(":/")
                        
                if "feynmana" in odpowiedz7.lower():
                    print("Odstresuś: tłumaczysz sobie/komuś/zabawce temat którego się uczysz prostym językiem, jakbyś uczył/a dziecko")
                    print("Co myślisz o tej metodzie nauki?")
                    odpowiedz10 = input("Ty: ")
                    if "super" in odpowiedz10.lower() or "podoba" in odpowiedz10.lower():
                        print("super, zapisuję, że lubisz tą metodę")
                        stan["metoda_nauki"] = "technika feynmana"
                        if "nie" in odpowiedz10.lower():
                            print(":/")

                if "recall" in odpowiedz7.lower():
                    print("Odstresuś: powtarzasz aktywnie wiedzę np. przez testy, quizy lub własne pytania")
                    print("Co myślisz o tej metodzie naukı?")
                    odpowiedz11 = input("Ty: ")
                    if "super" in odpowiedz11.lower() or "podoba" in odpowiedz11.lower():
                        print("super, zapisuję, że lubisz tą metodę")
                        stan["metoda_nauki"] = "active recall"
                        if "nie" in odpowiedz11.lower():
                            print(":/")

                if "coding" in odpowiedz7.lower():
                    print("Odstresuś: łączysz tekst ze schematami, obrazami, rysunkami tworząc skojarzenia.")
                    print("Co myślisz o tej metodzie naukı?")
                    odpowiedz12 = input("Ty: ")
                    if "super" in odpowiedz12.lower() or "podoba" in odpowiedz12.lower():
                        print("super, zapisuję, że lubisz tą metodę")
                        stan["metoda_nauki"] = "dual coding"
                        if "nie" in odpowiedz12.lower():
                            print(":/")
            
         if "nie" in odpowiedz4.lower() or "zły" in odpowiedz4.lower():
            print("Odstresuś: w takim razie chciałbyś jakiegoś tipa?")
            odpowiedz13 = input("Ty: ")
            if "tak" in odpowiedz13.lower() or "chętnie" in odpowiedz13.lower():
                losowy_tip = random.choice(tipy)
                print("Odstresuś:", losowy_tip)
            else:
                print("Odstresuś: ok")
                

     if "zrelaksować" in odpowiedz3.lower():
        print("Odstresuś: Co myślisz o ćwiczeniach oddechowych?")
        odpowiedz5 = input("Ty: ")
        
        if "super" in odpowiedz5.lower() or "dobry" in odpowiedz5.lower():
            cwiczenia_oddechowe()
        if "nie" in odpowiedz5.lower() or "zły" in odpowiedz5.lower():
            print("Odstresuś: ok")    

def presjae():
    print("Odstresuś: Czujesz presję od siebie, czy od innych ludzi?")
    odpowiedz_presja = input("Ty: ")
    if "siebie" in odpowiedz_presja.lower():
        print("Chciałbyś parę wskazówek jak poradzić sobie z presją?")
        odpowiedz_p2 = input("Ty: ")
        if "tak" in odpowiedz_p2.lower():
            print("Oto pare wskazówek dla Ciebie:")
            print("✅ nie musisz być perfekcyjny/a, żeby być wartościowy/a,")
            print("🧩 sam wynik nie jest najważniejszy, liczy się wiedza którą zdobyłeś/aś,")
            print("✍️ doceniaj nawet te najmniejsze sukcesy, bo to z nich się rodzi wielki sukces,")
            print("📈 ustalaj drobne, realistyczne cele zamiast dużych,")
            print("👭 porozmawiaj o tym z zaufną osobą: rodzicem, kolegom, czy przyjacółką.")
    if "kogoś" in odpowiedz_presja.lower() or "rodziców" in odpowiedz_presja.lower() or "znajomych" in odpowiedz_presja.lower() or "ludzi" in odpowiedz_presja.lower():
        print("Chciałbyś parę wskazówek jak poradzić sobie z presją?")
        op3 = input("Ty: ")
        if "tak" in op3:
            print("Oto parę wskazówek dla Ciebie:")
            print("🗣️ porozmawiaj z osobą która wywołuje presję,")
            print("✨ pamiętaj, że to twoje zycie nie ich,")
            print("🏆 pamiętaj, że twoja wartość to nie tylko oceny i osiągnięcia,")
            print("🧠 pomyśl, czy ty chcesz tego sukcesu, czy ktoś inny, twoje zdanie jest najważniejsze.")
    
# główny program

print("Cześć! Jestem Odstresuś.")
print("Zanim zaczniemy, jak masz na imię?")
imie = input("Ty: ")
stan["imie"] = imie
print("Co się dzieje?")
wiadomosc = input("Ty: ")
if "egzamin" in wiadomosc.lower() or "kolokwium" in wiadomosc.lower() or "kartkówkę" in wiadomosc.lower() or "zaliczenie" in wiadomosc.lower() or "sprawdzian" in wiadomosc.lower() or "pytanie" in wiadomosc.lower():
    stres_egzaminem()
    
if "stres" in wiadomosc.lower() or "stresuje" in wiadomosc.lower() or "potrzebuje pomocy" in wiadomosc.lower() or "potrzebuje twojej pomocy" in wiadomosc.lower() or "potrzebuje jakiejś pomocy" in wiadomosc.lower():
    print("Odstresuś: Czym się stresujesz?")
    od0 = input("Ty: ")

    if "ogólnie" in od0.lower() or "wszytskim" in od0.lower() or "wieloma" in od0.lower():
        print("Odstresuś: W takim razie spróbuję Ci jakoś pomóc. Jakiego rodzaju pomocy potrzebujesz?")
        odpowiedz1 = input("Ty: ")

        if "ćwiczenia" in odpowiedz1.lower() or "oddechowe" in odpowiedz1.lower():
            cwiczenia_oddechowe()

    if "presję" in od0.lower():
        presjae()
    
    if "egzmaminem" in od0.lower() or "kolokwium" in od0.lower() or "zaliczeniem" in od0.lower() or "kartkówką" in od0.lower() or "sprawdzianem" in od0.lower() or "pytaniem" in od0.lower():
        stres_egzaminem()


if "presję" in wiadomosc.lower():
    presjae()

    