print("*** NUMBRIDEGA MÄNGUD ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = abs(int(input("Sisestage täisarv => "))) #paranda süntaks lisa ))
        break
    except ValueError:
         print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga pole mõtet midagi peale hakata")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrake, kui palju paaris ja mitu paaritu numbrit on arvus")
    print()
    c=b=a #paranda süntaks eemalda üks =
    paaris=0 #paranda süntaks eemalda üks =
    paaritu=0 #paranda süntaks eemalda üks =
    while b > 0: #paranda süntaks lisa :
            if b % 2 == 0: #paranda süntaks lisa =
                    paaris += 1 #paranda süntaks + vasakule
            else:
                    paaritu += 1 #paranda süntaks + vasakule
            b = b // 10
    print("Paaris arvude kogus:",paaris) #paranda süntaks ("Paaris arvude kogus:" paaris)
    print("Paaritu on:",paaritu) #paranda süntaks ("Paaritu on:" paaritu)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Pöörake* sisestatud number")
    print()
    b=0
    while a > 0: #paranda süntaks lisa :
        number = a % 10
        a = a // 10
        b = b * 10
        b += number #paranda süntaks + vasakule
    print("*Ümberpööratud* number", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Syracuse hüpoteesi testimine") #paranda süntaks eemalada üks (
    print()
    if c % 2 == 0: #paranda süntaks liigu vasakule
        print(c," - paarisarv. Jagage 2-ga.") #paranda süntaks (c" - paarisarv. Jagage 2-ga.")
    else:
        print(c," - paaritu number. Korrutage 3-ga, lisage 1 ja jagage 2-ga.")
    while c != 1:
            if c % 2 == 0: #paranda süntaks lisa üks =
                    c = c / 2 #paranda süntaks eemalda üks =
            else:
                    c = (3*c + 1) / 2 #paranda süntaks eemalda üks =s
            print(c, end=" ") #paranda süntaks lisa "
    print()
    print("Hüpotees on õige") #paranda süntaks eemalda '' ja lisa "
