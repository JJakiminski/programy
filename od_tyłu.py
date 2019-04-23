tekst = input("Wprowadź tekst: ")
copy = tekst
new_tekst = " "
lenght = len(tekst)
x = lenght-1


while lenght>0:
    new_tekst += tekst[-1]
    tekst =tekst[0:x]
    lenght = len(tekst)
    x = lenght-1


print("tekst od tyłu to: ", new_tekst)

input("\n\nAby zakończyć program, wciśnij Enter.")
