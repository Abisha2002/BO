
#Quizz over een vluchtelling.
import time
print("Welkom bij de quizz waar je in de positie van een vluchtelling zit, Je gaat hier multiple choise vragen beantwoorden.")
time.sleep(3)
print("Je bent een vluchtelling in syrie die de optie krijgt om te vluchten van de oorlog naar een veilig land het is aan jou of je dat ook  gaat doen")

#vragen 
def vraag3(): 
    print("Vind jij het een goed dat je broer zijn bestevriend wilt mee nemen?")  
    print("a = Ja goed idee!")  
    print("b = Nee de broer mag niet mee")
    antwoord3 = input()
    if antwoord3.lower == "a":
        print("Je gaat samen vluchten met je broer en zijn bestevriend")
        time.sleep(1)
        print(vraag4())
    elif antwoord4.lower() == "b":
        print("De beste vriend mag niet mee je broer wilt ook niet mee, je gaat nu alleen vluchten")


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
        print("je beste vriendin wilt niet mee vluchten")
        print(vraag4())        


def vraag1():
    print("Wil je gaan vluchten?")
    print("a = ja ik wil vluchten")
    print("b = nee ")
    print("c = ja maar ik wil iemand meennemen")
    antwoord1 = input()
    if antwoord1.lower() == "a": 
        print("Je hebt gekozen om te vluchten.\n") 
        time.sleep(1)
        print(vraag2())
    elif antwoord1.lower() == "b": 
        print("Je kiest ervoor om niet te gaan vluchten hierdoor ga je dood.")
        time.sleep(1)
        print(vraag1())
        print("Je bent dood gegaan, probeer het opnieuw")
    elif antwoord1.lower() == "c":
        print("Wie wil je meenemen")
        print(vraag2())
    else:
        print("Kies a, b, c")
print(vraag1())


