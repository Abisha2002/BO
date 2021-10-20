
#Quizz over een vluchtelling.
import time
print("Welkom bij de quizz waar je in de positie van een vluchtelling zit, Je gaat hier multiple choise vragen beantwoorden.")
time.sleep(3)
print("Je bent een vluchtelling in syrie die de optie krijgt om te vluchten van de oorlog naar een veilig land het is aan jou of je dat ook  gaat doen")

#vragen 
def vraag17():
    print("Wat wil je mee nemen?")
    print("a = Foto's van vroeger ")
    print("b = Telefoon met contactgegevens van je famillie")


def vraag11():


def vraag10():
    print("weet je zeker dat je een mes wilt mee nemen?")
    print("a = Ja")
    print("b = nee ")
    antwood10 = input
    if antwood10.lower == "a":
        print("dit is geen veilig keuze")
        print(vraag18())
    elif antwood10.lower == "b":
        print(vraag17())


def vraag9():
    print("er staan 3 containers om mee in proberen te gaan voor welke container ga je?")
    time.sleep(0.5)
    print("a = Rood")
    print("b = Groen")
    print("c = bruin")
    antwoord9 = input
    if antwoord9.lower == "a":
        print("Deze container is dicht, probeer een ander!")
        print(vraag9())
    elif antwoord9.lower == "b":
        print("Deze container is open!")
        print(vraag16())
    elif antwoord9.lower == "c":
        print("Deze container is dicht, probeer een ander!")
        print(vraag9())


def vraag8():
    print("via welke route wil je gaan vlucten?")
    print("a = Boot")
    print("b = Vracht")
    antwoord8 = input
    if antwoord8.lower == "a":
        print("De route met de boot duurt lang, je moet eten mee nemen")
        print(vraag7())
    elif antwoord8.lower == "b":
        print("Je wilt gaan vluchten via vracht")
        print(vraag9())

def vraag7():
    print("Wat ga je doen?")
    print("a = Je steelt eten uit de supermarkt")
    print("b = Je hebt geen geld dus je gaat zonder eten op de boot stappen") #1 je eet later van een mens op de boot die dood is 2 dood door voedselvergifteging
    antwoord7 = input()
    if antwoord7.lower == "a":
        print("Je word gepakt door de politie tijdens het stelen van voedsel! Je gaat hierdoor de gevangenis in hierbij eindigt je vlucht!")
        time.sleep(2)
        print("Probeer opnieuw te spelen!")
        print(vraag1())
    elif antwoord7.lower() == "b":
        print("je hebt ervoor gekozen om te gaan vluchten zonder voedsel")
        print(vraag15()) #je krijgt honger op de boot wat doe je?


def vraag6():
    print("Waar willen jullie heen vluchten met ze 3en?")
    print("a = Nederland")
    print("b = Canada")
    print("c = Griekenland")
    antwoord6 = input()
    if antwoord6.lower == "a":
        print("jullie gaan nu proberen naar nederland te vluchten")
        print(vraag12())
    elif antwoord6.lower() == "b":
        print("jullie gaan nu proberen naar Canada vluchten")
        print(vraag13())
    elif antwoord6.lower == "c":
        print("jullie gaan nu proberen naar Griekenland te vluchten")
        print(vraag14())


def vraag5():
    print("Jullie kunnen een niet te zware rugtas mee nemen, wat nemen jullie mee in je rugtas?")
    print("a = Een mes") # Einde 2 door tassen controle waar mes word gevonden.
    print("b = Foto's van vroeger")
    print("c = Telefoon met contactgegevens van je famillie")
    antwoord5 = input()
    if antwoord5.lower == "a":
        print(vraag10()) #weetje zeker dat je een mes wilt mee nemen?
    elif antwoord5.lower() == "b":
        print("Dit is een veilige keuze, dit zal geen kwaad doen bij controles.")
        print(vraag11())
    elif antwoord5.lower == "c":
        print("Dit is een veilige keuze")
        print(vraag16())


def vraag4():
    print("Via welke route wil je gaan vluchten?")
    print("a = Boot")
    print("b = Vliegtuig")
    print("c = Vracht")
    antwoord4 = input()
    if antwoord4.lower == "a":
        print("Je wilt gaan vluchten op een boot")
        print("De route met de boot duurt lang, je moet eten mee nemen")
        print(vraag7()) 
    elif antwoord4.lower() == "b":
        print("Je hebt geen geldig paspoort! hierdoor kom je nooit door de douane heen, kies een andere route!")
        print(vraag8()) #dezelfde als vraag 4 maar zonder optie vliegtuig
    elif antwoord4.lower() == "c":
        print("Je wilt gaan vluchten via vracht.")
        print(vraag9())


def vraag3(): 
    print("Vind jij het een goed dat je broer zijn bestevriend wilt mee nemen?")  
    print("a = Ja goed idee!")  
    print("b = Nee de broer mag niet mee")
    antwoord3 = input()
    if antwoord3.lower == "a":
        print("Je gaat samen vluchten met je broer en zijn bestevriend")
        time.sleep(1)
        print(vraag6())
    elif antwoord3.lower() == "b":
        print("De beste vriend mag niet mee je broer wilt ook niet mee, je gaat nu alleen vluchten")
        print(vraag4()) 


def vraag2(): 
    print("Met wie wil je gaan vluchten?")
    print("a = Broer")
    print("b = Beste vriendin")
    print("c = Moeder")
    antwoord2 = input() 
    if antwoord2.lower() == "a":
        print("Je hebt gekozen om met je broer te vluchten, je broer wilt zijn bestevriend mee nemen. \n")
        time.sleep(2)
        print(vraag3())
    elif antwoord2.lower() == "b":
        print("je beste vriendin wilt niet mee vluchten, je gaat nu alleen vluchten")
        print(vraag4())        
    elif antwoord2.lower() == "c":
        print("je kiest ervoor om samen met je moeder te gaan vluchten")
        print(vraag5())


def vraag1():
    print("Wil je gaan vluchten.?")
    print("a = ja ik wil vluchten.")
    print("b = nee. ")
    print("c = ja maar ik wil iemand meennemen.")
    antwoord1 = input()
    if antwoord1.lower() == "a": 
        print("Je hebt gekozen om te vluchten.\n") 
        time.sleep(1)
        print(vraag4())
    elif antwoord1.lower() == "b": 
        print("Je kiest ervoor om niet te gaan vluchten hierdoor ga je dood.")
        time.sleep(1)
        print(vraag1())
        print("Je bent dood gegaan, probeer het opnieuw.")
    elif antwoord1.lower() == "c":
        print("Je hebt gekozen om met iemand te vluchten.")
        print(vraag2())
    else:
        print("Kies a, b, c")
print(vraag1())

