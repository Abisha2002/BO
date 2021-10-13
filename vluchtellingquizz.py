#Quizz over een vluchtelling.
import time
print("Welkom bij de quizz waar je in de positie van een vluchtelling zit, Je gaat hier multiple choise vragen beantwoorden.")
time.sleep(3)
print("Je bent een vluchtelling in syrie die de optie krijgt om te vluchten van de oorlog naar een veilig land het is aan jou of je dat ook  gaat doen")

#vragen 

def vraag1():
    print("Wil je gaan vluchten?")
    print("a = ja ik wil vluchten")
    print("b = nee ")
    print("c = ja maar ik wil iemand meennemen")
    antwoord1 = input()
    if antwoord1.lower() == "a": 
        print("Je hebt gekozen om te vluchten.\n") 
        time.sleep(1.0)
        print(vraag3())
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




#vraag 2 
print("vraag 2")
answer2 = input ("Met wie wil je gaan vluchten? \n a. Broer \n b. Beste vriendin \n c. Moeder \n Answer: ")
if answer2 == "a" or answer2 == "Broer":
    print ("je hebt gekozen om te gaan vluchten met je broer, de beste vriend van je broer wilt mee ")

#vraag2.1
print("vraag 2.1")
answer2.1 = input("De beste vriend van je broer wilt meegaan, vind jij het dat ook een goed idee? \n a. ja \n b. nee \n Answer:")
if answer2.1 == "a" or answer2




