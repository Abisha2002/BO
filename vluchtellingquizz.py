
#Quizz over een vluchtelling.
import time
print("Welkom bij de quizz waar je in de positie van een vluchtelling zit, Je gaat hier multiple choise vragen beantwoorden.")
time.sleep(3)
print("Je bent een vluchtelling in syrie die de optie krijgt om te vluchten van de oorlog naar een veilig land het is aan jou of je dat ook  gaat doen")

#vragen 

def vraag23():
    print(" De boot waar je nu op zit gaat naar nederland!")
    print("Wil je naar nederland vluchten?")
    print("a = Ja ")
    print("b = Nee")
    antwoord = input()
    if antwoord.lower() == "a": #win 
        print("Je hebt het behaald! je bent veilig aangekomen in nederland!")
    elif antwoord.lower() == "b": #einde
        print("Aangezien je echt niet naar nederland wilt vluchten, spring je van de boot")
        print("Je vlucht eindigd hier")
        vraag22()

def vraag22():
    print("Wil je opnieuw spelen?")
    print("a = Ja ")
    print("b = Nee ")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag1()
    elif antwoord.lower() == "b":
        print("Bedankt voor het spelen!")

def vraag21(): #zandzakken
    print("Zodra de containers te veel bewegen kunnen de stapels zand op je vallen.")
    print("Wat ga je doen?")
    print("a = Je blijft op dezelfde plek want je kent de boot verder niet.")
    print("b = Je gaat bovenop de container klimmen. ")
    antwoord = input()
    if antwoord.lower() == "a": #einde
        print("De stapels met zakken zand zijn op je gevallen waardoor je bent dood gegaan")
        print("hierdoor eindigd je vlucht")
        vraag22()
    elif antwoord.lower() == "b": #einde
        print("Vlak voordat de boot kon vertrekken werd er een container geplaatst boven op de container waar jij op ligt")
        print("Je bent hierdoor geplet en overleden je vlucht eindigd hier")
        vraag22()


def vraag20(): 
    print("Waar ga je jezelf verstoppen?")
    print("a = In de container tussen de stapels zakken vol zand ")
    print("b = Ik ga boven op de container liggen")
    print("c = bij de dieren")
    antwoord = input()
    if antwoord.lower() == "a": 
        print("Hier kan je wel voor even blijven maar niet voor lang")
        vraag21()
    elif antwoord.lower() == "b": #einde
        print("Vlak voordat de boot kon vertrekken werd er een container geplaatst boven op de container waar jij op ligt")
        print("Je bent hierdoor geplet en overleden je vlucht eindigd hier")
        vraag22()
    elif antwoord.lower() == "c": #einde
        print("Bij de dieren hangen camera's hierdoor word je gepakt")
        print("je vlucht eindigd hier")
        vraag22()


def vraag19(): # je hebt voedsel gestolen van iemand op de boot. 
    print("Degene waar je voedsel van hebt gestolen heeft niks door dus dit is de manier hoe je gaat overleven.")
    print("Er is een optie om over te stappen op een groter boot, ga je dit doen?")
    print("a = Ja ik stap over")
    print("b = Nee ik blijf op de boot")    
    antwoord15 = input()
    if antwoord15.lower() == "a":
        print("dit is de juiste keuze want de oude boot is gezonken")
        vraag23()
    elif antwoord15.lower() == "b": #einde
        print("Je koos ervoor om niet te gaan overstappen helaas is de boot waar je nu op zit gezonken.\n")
        print("Je vlucht eindigt hier")
        vraag22()


def vraag18():#moeder
    print("Er is een tassencontrole, hierbij word je mes ontdekt in je tas.\n ")
    print("Je word mee genomen naar het bureau, je vlucht eindigt hier.\n")
    time.sleep(5)
    vraag22()


def vraag17(): #einde 
    print("Wat wil je mee nemen?")
    print("a = Foto's van vroeger ")
    print("b = Telefoon met contactgegevens van je famillie")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag11
    elif antwoord.lower() == "b":
        vraag12()  


def vraag16(): #boot
    print("Je ziet dat er iemand is overleden op de boot en dat mensen op de boot het vlees van die mens op eten.")
    print("Langzamerhand krijg jij ook honger, wat doe je?\n")
    print("a = Niks eten want je hebt niks bij je")
    print("b = Je gaat de vlees van de overleden persoon eten.")
    print("c = Je steelt voedsel van een ander op de boot ")
    antwoord = input()
    if antwoord.lower() == "a":
        print("Je overlijd aan honger")
        print("Je vlucht eindigd hier, probeer opnieuw te spelen!")
        time.sleep(1)
        vraag1()
    elif antwoord.lower() == "b":
        print("Je overlijd aan voedselvergiftiging ")
        print("Je vlucht eindigd hier, probeer opnieuw te spelen!")
        time.sleep(1)
        vraag1()
    elif antwoord.lower() == "c":
        print("dit is de juiste antwooord")
        vraag19() 


def vraag15(): #jullie gaan vluchten naar griekenland
    print("TEST")
    print("TEST")
    antwoord15 = input()
    if antwoord15.lower() == "a":
        print("aaa")
    elif antwoord15.lower() == "b":
        print("bbb")

def vraag14(): #jullie gaan vluchten naar canada 
    print("TEST")
    print("TEST")
    antwoord = input()
    if antwoord.lower() == "a":
        print("aaa")
    elif antwoord.lower() == "b":
        print("bbb")


def vraag13(): #jullie willen vluchten naar nederland
    print("TEST")
    print("TEST")
    antwoord = input()
    if antwoord.lower() == "a":
        print("aaa")
    elif antwoord.lower() == "b":
        print("bbb")


def vraag12(): #einde
    print("Iemand op de boot wilt je telefoon lenen om te bellen naar zijn famille")
    print("a = Hij mag de telefoon gebruiken")
    print("Je belt eerst naar jouwn eigen famillie en daarna mag hij bellen.")
    antwoord = input()
    if antwoord.lower() == "a":
        print("Degene aan wie je de telefoon gaf heeft een crimineel gebeld, tijdens een controle word jij er mee gepakt.")
        print("Je moet nu mee naar het bureau hierdoor eindigt je vlucht\n")
        vraag22() #wil je opnieuw spelen?
    elif antwoord.lower()  == "b":
        print("Je telefoon explodeerd hierdoor ga je dood en eindigt je vlucht hier.")
        vraag22() #wil je opnieuw spelen?


def vraag11():
    print("Je tas word doorgezocht tijdens een controle. \n")
    print("Op 1 van de fotos die je bij je hebt staat iemand op die in de gevangenis zit voor het stelen van een auto. \n")
    print("Jij word nu verdacht, je word mee genomen naar het bureau hierdoor eindigt je vlucht hier. \n")
    time.sleep(5)
    print("wil je opnieuw spelen?")
    print("a = Ja")
    print("b = nee ")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag1()
    elif antwoord.lower() == "b":
        vraag22()


def vraag10(): 
    print("weet je zeker dat je een mes wilt mee nemen?")
    print("a = Ja")
    print("b = nee ")
    antwoord = input()
    if antwoord.lower() == "a":
        print("dit is geen veilig keuze")
        vraag18()
    elif antwoord.lower() == "b":
        vraag17() #done


def vraag9():
    print("er staan 3 containers om mee in proberen te gaan voor welke container ga je?")
    time.sleep(0.5)
    print("a = Rood")
    print("b = Groen")
    print("c = bruin")
    antwoord = input()
    if antwoord.lower() == "a":
        print("Deze container is dicht, probeer een ander!")
        vraag9() #done
    elif antwoord.lower() == "b":
        print("Deze container is open!")
        vraag20() #done
    elif antwoord.lower() == "c":
        print("Deze container is dicht, probeer een ander!")
        vraag9() #done


def vraag8():
    print("via welke route wil je gaan vlucten?")
    print("a = Boot")
    print("b = Vracht")
    antwoord = input()
    if antwoord.lower() == "a":
        print("De route met de boot duurt lang, je moet eten mee nemen")
        vraag7()
    elif antwoord.lower() == "b": #vracht
        print("Je wilt gaan vluchten via vracht")
        vraag9()


def vraag7(): #boot
    print("Wat ga je doen?")
    print("a = Je steelt eten uit de supermarkt")
    print("b = Je hebt geen geld dus je gaat zonder eten op de boot stappen")
    antwoord = input()
    if antwoord.lower() == "a": #einde
        print("Je word gepakt door de politie tijdens het stelen van voedsel! Je gaat hierdoor de gevangenis in hierbij eindigt je vlucht!")
        time.sleep(2)
        print("Probeer opnieuw te spelen!")
        vraag1()
    elif antwoord.lower() == "b":
        print("je hebt ervoor gekozen om te gaan vluchten zonder voedsel, je zit nu al 1 dag op de boot.")
        time.sleep(1)
        vraag16()


def vraag6(): #broer en bestevriend.
    print("Waar willen jullie heen vluchten met ze 3en?")
    print("a = Nederland")
    print("b = Canada")
    print("c = Griekenland")
    antwoord = input()
    if antwoord.lower() == "a":
        print("jullie gaan nu proberen naar nederland te vluchten \n")
        time.sleep(0.5)
        vraag13()
    elif antwoord.lower() == "b":
        print("jullie gaan nu proberen naar Canada vluchten")
        vraag14()
    elif antwoord.lower() == "c":
        print("jullie gaan nu proberen naar Griekenland te vluchten")
        vraag15()


def vraag5(): #moeder
    print("Jullie kunnen een niet te zware rugtas mee nemen, wat nemen jullie mee in je rugtas?")
    print("a = Een mes") # Einde 3 door tassen controle waar mes word gevonden.
    print("b = Foto's van vroeger")
    print("c = Telefoon met contactgegevens van je famillie")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag10()
    elif antwoord.lower() == "b":
        print("Je hebt ervoor gekozen om foto's mee te nemen.")
        vraag11()
    elif antwoord.lower() == "c":
        vraag12()      


def vraag4(): #alleen
    print("Via welke route wil je gaan vluchten?")
    print("a = Boot")
    print("b = Vliegtuig")
    print("c = Vracht")
    antwoord = input()
    if antwoord.lower() == "a":
        print("Je wilt gaan vluchten op een boot \n")
        print("De route met de boot duurt lang, je moet eten mee nemen")
        vraag7()
    elif antwoord.lower() == "b":
        print("Je hebt geen geldig paspoort! hierdoor kom je nooit door de douane heen, kies een andere route!")
        vraag8()
    elif antwoord.lower() == "c": #vracht
        print("Je wilt gaan vluchten via vracht.")
        vraag9()


def vraag3(): 
    print("Vind jij het een goed dat je broer zijn bestevriend wilt mee nemen?")  
    print("a = Ja goed idee!")  
    print("b = Nee de broer mag niet mee")
    antwoord = input()
    if antwoord.lower() == "a":
        print("Je gaat samen vluchten met je broer en zijn bestevriend via een boot.\n")
        vraag6()
    elif antwoord.lower() == "b":
        print("De beste vriend mag niet mee je broer wilt ook niet mee, je gaat nu alleen vluchten")
        vraag4()


def vraag2():
    print("Met wie wil je gaan vluchten?")
    print("a = Broer")
    print("b = Beste vriendin")
    print("c = Moeder")
    antwoord = input() 
    if antwoord.lower() == "a":
        print("Je hebt gekozen om met je broer te vluchten, je broer wilt zijn bestevriend mee nemen.\n")
        time.sleep(2)
        vraag3()
    elif antwoord.lower() == "b":
        print("je beste vriendin wilt niet mee vluchten, je gaat nu alleen vluchten")
        vraag4()      
    elif antwoord.lower() == "c":
        print("je kiest ervoor om samen met je moeder te gaan vluchten")
        vraag5()


def vraag1():
    print("Wil je gaan vluchten.?")
    print("a = ja ik wil vluchten.")
    print("b = nee. ")
    print("c = ja maar ik wil iemand meennemen.")
    antwoord= input()
    if antwoord.lower() == "a": 
        print("Je hebt gekozen om te vluchten.\n") 
        time.sleep(1)
        vraag4()
    elif antwoord.lower() == "b": #einde1
        print("Je kiest ervoor om niet te gaan vluchten hierdoor ga je dood.")
        print("Hier eindigd je vlucht, probeer het opnieuw.")        
        time.sleep(1)
        vraag22()
    elif antwoord.lower() == "c":
        print("Je hebt gekozen om met iemand te vluchten.")
        vraag2()
    else:
        print("Kies a, b, c")
vraag1()
