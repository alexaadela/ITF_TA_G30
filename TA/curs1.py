# importing "keyword" for keyword operations
import keyword

"""
INTRO - Primii pasi in programare => facem o scurta recapitulare
1. Environment Setup
=> am instalat IntelliJ IDEA (https://www.jetbrains.com/idea/download/#section=mac)
ce este IDE? => INTEGRATED DEVELOPMENT ENVIRONMENT - un mediu de dezvoltare al programelor (e ca un Word, dar mai avansat care ne ajuta sa scriem codul java)
Exemple de IDE-uri: pycharm, intelij, eclipse, visual studio, visual studio code
=> am instalat Pycharm, varianta comunity (https://www.jetbrains.com/pycharm/download/?source=google&medium=cpc&campaign=14124132468&term=pycharm&gclid=Cj0KCQjwhY-aBhCUARIsALNIC06jnnDew_6mwQGLQDgbvmGrW6EJDVBA7xjgQYcZqNDrnObX8R0firMaAjCqEALw_wcB#section=mac))
ce este Pycharm? - e ca un Word, dar mai avansat care ne ajuta sa scriem codul python
unde se pune, by default, dupa instalare? - pe C:\Program Files\JetBrains\Pycharm Community Edition 202x.y
Important la instalare:
    * bifam casuta "Add 'bin' folder to the PATH" - environment variables;
    * creeam asociere cu extensia .py (bifam si casuta aceasta)
    * create desktop shortcut - Pycharm Comunity Edition (bifam si casuta aceasta)
    * update context menu: "Add Open Folder as Project" (daca bifam si aceasta casuta vom avea o optiune in context menu, atunci cand dam click dreapta pe folderul cu proiectul)
=> am instalat python (acesta este limbajul de programare cu care vom opera) (www.python.org/downloads)(luam ultima versiune)
    * bifam ambele optiuni din partea de jos ('Add python 3.10 to PATH' si 'Install launcher for all users (recomanded)')
    * folosim varianta Install now (recomandata)
=> am creeat un nou proiect
    * i-am dat un nume proiectului
    * la python interpreter am lasat default Virtualenv
    * la location default
    * la base Interpreter ne asiguram ca alegem din drop-down ultima versiune de python - adica cea mai noua)
=> am vazut structura proiectului
=> am aflat ce este acel VENV din partea stanga: Virtual environment (prin VENV ni se ofera o modalitate de a avea o instalare locala python
care este izolata de toate celelalte instalari viitoare sau precedente)
=> am creeat un python file 'Hello Word'
    * am vazut regula de numire a unui fisier python: scriem cu litere mici numele fisierului si separam cuvintele, daca e cazul cu bara jos _
    * spre deosebire de java, unde se foloseste regula camel case, in Python folosim snake_case - asa se numeste scrierea cu litere mici si bara jos in numele fisierelor
    * am vazut ca in momentul adaugarii unui nou python file, acesta este gol
    * am vazut ca in partea stanga sunt numerotate liniile de cod, pentru a ne ajuta sa ne referim cu usurinta la o noua linie de cod
    * python face parte din top 4 limbaje de programare, alaturi de java, java script si c#
=> am vazut unde e consola, ce este aceasta si ce se afiseaza in ea
=> am vazut unde e terminalul si ce este acesta (locul din care putem sa instalam pachete si sa rulam framework-uri)
=> am aflat ce se intampla atunci cand noi rulam codul scris
    * codul se ruleaza linie cu linie (ii mai spunem si secvential)
    * codul se compileaza, adica se traduce din limbaj python (in cazul nostru) in byte code (adica insiruire de 0 si 1)
"""

"""
********* CURS 1 *************

1. Comentarii & print('Hello World')

    A. Comentarii
- Comentariile sunt bucati de cod care trebuie sa fie ignorate de catre sistem
- In general codul pe care il scriem noi este ca un limbaj gramatical pe care sistemul trebuie sa il interpreteze
- Daca noi scriem linii care nu corespund limbajului gramatical inteles de python, atunci sistemul va fi confuz, si ca rezultat va returna eroare
- Ca sa evitam situatia asta putem sa ne folosim de comentarii, astfel incat sa ii spunem sistemului ca nu vrem sa ii transmitem instructiuni
ci vrem sa adaugam niste note personale care nu sunt de interes pentru rulare;
- Daca tiparim text invalid/necomentat, ni se va returna eroarea: SyntaxError: invalid syntax
Exista doua tipuri de comentarii:
1. Comentarii multi line, reprezentate de trei ghilimele simple sau duble
e.g.:
"""

''' 
    cod de comentat 2
    cod de comentat 2
    cod de comentat 3
    ...
    cod de comentat n
'''
""" 
    cod de comentat 2
    cod de comentat 2
    cod de comentat 3
    ...
    cod de comentat n
"""

"""
2. Comentarii single line, reprezentate de semnul #
e.g.:
# comentariu 1
# comentariu 2
# ...
# comentariu n

Note: !!!!! Scurtatura pentru comentariile single line este CTRL + / (pe windows) sau COMMAND + / (pe mac)
!!!!!Putem sa comentam mai multe randuri cu single line comment in acelasi timp daca
le selectam pe toate si apoi folosim scurtatura pentru comentariile single line;
"""

#   B. PRINT function - print('Hello World')
# **** CE ESTE O FUNCTIE? *****
# - o functie este o logica de cod predefinita care face ceva;
# - are sintaxa nume_functie() ;
# - in paranteze punem date de intrare/iesire => vom vedea mai incolo ca aceste date se mai numesc si parametrii
# !!!! vom studia conceptul de FUNCTII si parametrii in detaliu, in capitolele care urmeaza (la cursul 5 daca bine tin minte)
# ****************************************************************************************************************************

# **** PRINT FUNCTION ****
# - orice instructiune de scriere in consola se va face prin intermediul instructiunii print(), care este, de fapt o FUNCTIE cu parametrii
# - avem nevoie sa scriem intre paranteze informatia pe care vrem sa o printam, care este, de fapt, in cazul nostru, parametrul;
# - ca sa rulam codul, putem sa dam click dreapta oriunde in program si sa apasam butonul "Run"

# - atunci cand apelam functia fara niciun parametru, atunci ea prineaza doar "newline" char, adica \n si nimic altceva
print()
# - in cazul acesta avem un parametru, si anume stringul vid "", iar functia returneaza acelasi lucru ca si mai sus
print("")
print('Grupa 30')
print('o----/')
print(' ||||')
print('*' * 20)
print("Hello world")
print("Hello world on planet 'earth' ")
print('Hello world on planet "earth" ')

# - grupul de caractere '\n' este folosit pentru a adauga o linie noua goala
# - by default, dupa functia print se trece la linie noua direct, asa cum am explicat mai sus
print('Hello word! \n Ce mai faceti azi?')

# - caracterul \ pus inaintea unui caracter cu functie specifica schimba comportamentul acelui caracter
# si il marcheaza ca fiind necesar sa fie afisat pe eccran;
print('Hello world on planet \'earth\' ')

# functia print() poate sa foloseasca parametrii 'sep' si 'end':
# - 'sep', pentru a separa argumentele intr-o maniera dorita
# - 'end', pentru a marca pozitia de dupa ultimul argument cu un element dorit
print('1. Hello', 'My', 'World', sep='*', end='!')
print('Am printat?!')
print('2. Hello', 'My', 'World', sep='-', end='\n')
print('Am printat?!')

"""
 ********************** 2. VARIABILE **************************
- o variabila este o adresa de memorie in care putem stoca informatii;
- adresa de memorie este reprezentata de numele variabilei;
- in momentul in care incercam sa printam o variabila pe ecran, in consola, de fapt incercam sa gasim adresa de memorie care poarta numele variabilei       
si sa scoatem informatia de acolo cu scopul afisarii ei;
- Ca si echivalent puteti sa va ganditi ca o variabila este o casa aflata la o anumita adresa (adresa de memorie), 
care poate fi locuita azi, de familia Popescu (informatia/valoarea) si peste o anumita perioada, de familia Bitanescu (noua informatie/valoare <=> suprascriere)
- ii spunem variabila pentru ca valoarea de la adresa de memorie pe care o reprezinta se poate schimba;
Reguli de baza pentru numirea variabilelor:
1. Trebuie sa inceapa cu litera mica
2. Trebuie sa nu aiba spatii => nu se poate e.g. ~my var~
e.g. Daca numele variabilei este format din mai multe cuvinte, atunci numele variabilei poate urma formatul camelCase sau snake_case:
 - myVar, myNewVar
3. Numele unei variabile poate contine simbolul _, insa nu ca si caracter de inceput
- my_var, my_new_var
4. Trebuie sa nu inceapa cu numere, insa pot sa contina numere in interior sau la sfarsit,
- myNewVar_curs1, myNewVar_curs2 
5. Trebuie sa nu inceapa cu caractere speciale
- *myName
"""

# importam libraria keyword la inceputul fisierului .py cu comanda
# import keyword
# apoi listam toate keyword-urile din python
print('The list of Python Keywords is: ')
print(keyword.kwlist)

# ************** 3. DECLARAREA SI INITIALIZAREA UNEI VARIABILE | TIPURI DE DATE| CONCATENARE ****************

# - DECLARAREA reprezinta alocarea adresei de memorie reprezentata de numele specificat
# - INITIALIZAREA reprezinta stocarea unei informatii/valori la adresa de memorie rezervata anterior
# EXEMPLE:
suntLaCurs = 'DA'
print(
    suntLaCurs)  # => Daca nu folosim variabila inainte sa o redefinim primim un warning: Redeclared 'suntLaCurs' defined above without usage

# - nu putem declara o variabila in python fara sa o initializam
# python e loosely type, adica tipul de data este definit de valoarea pe care o atribuim
# deci, daca nu specificam valoarea, atunci sistemul nu va sti cu ce tip de data trebuie sa lucreze
# print(nuSuntLaCurs)

# Variabilele se pot suprascrie (SUPRASCRIERE = momentul in care schimbam valoarea de la adresa de memorie identificata prin numele variabilei)
# - spunem ca suprascriem o variabila atunci cand aceluiasi variabile folosite ulterior
# ii atribuim o noua valoare, repezentand acelasi tip de data sau un tip de data diferit
suntLaCurs = 12
print(suntLaCurs)

# - putem face si initializari multiple, adica pot sa enumar mai multe nume de variabile, si sa le atriburi valori, totul intr-o singura linie
suntLaCurs, imi_place_la_curs, simtCaInvat, automationDaNota = True, "meh", "y", 10

# - putem sa atribuim aceiasi valoare mai multor variabile, totul intr-o singura linie
imi_place_la_curs = simtCaInvat = automationDaNota = "Cursul1"

# - daca dorim sa printam in consola, cu aceiasi functie print() doua sau mai mule tipuri de date STRING, provenite din 'surse' diferite, atunci
# => vorbim despre notiunea de CONCATENARE
# CONCATENARE = 'adunarea' sau punerea impreuna a doua sau mai multe stringuri
# CONCATENAREA se face utilizand semnul '+'
myConcat1 = 'Adela'
myConcat2 = 'Alexa'
print('My name is: ' + myConcat1 + ' ' + myConcat2)

# - daca incercam sa concatenam tipul de date STRING cu alt tip de date, cum ar fi BOOL, atunci se va returna eroare:
# TypeError: can only concatenate str (not "int") to str
# => eroarea este returnata pentru ca nu putem sa concatenam (sa lipim) o informatie de tip boolean cu o informatie de tip string
myConcat1 = 'Adela'
myConcat2 = 'Alexa'
myConcat3 = 33
# print('My name is: ' + myConcat1 + ' ' + myConcat2 + ' si am ' + myConcat3 + ' ani!')
print('My name is: ' + myConcat1 + ' ' + myConcat2 + ' si am ' + str(myConcat3) + ' ani!')

# Ca sa rezolvam problema/eroarea, avem doua solutii:
#       a. TYPE CASTING
#       b. print cu FORMATARE

myConcat1 = 'Adela'
myConcat2 = 'Alexa'
myConcat3 = 33
myConcat4 = 1.67
myConcat5 = False
# a. TYPE CASTING => schimbam tipul de date
# cum facem asta?! => tipul_de_data_dorit(tipul_de_data_de_convertit)
print('Adela')
print(str('Adela'))
print(str(myConcat1))
print(33)
print(str(33))
print(str(myConcat3))
print("Prenumele meu este: " + myConcat1)
print("Numele meu este: " + myConcat2)
print("Varsta mea este: " + str(myConcat3))
print("Inaltimea mea este: " + str(myConcat4))
print("Sunt pozitiva COVID: " + str(myConcat5))
print('Numele meu este: ' + myConcat1 + ' ' + myConcat2 + ' , am ' + str(myConcat3) + ' ani si inaltimea: ' + str(
    myConcat4) + ' si sunt pozitiva COVID: ' + str(myConcat5))

# - daca tot suntem la type CASTING, sa mai luam un exemplu
# Expunem urmatoarea situatie:
# - avem un tip de data string care contine pretul unui kg de banane
# - avem un tip de data int care contine pretul unui kg de cartofi
# => vrem sa aflam pretul final de plata la casa, pentru 1 kg de cartofi si 1 kg de banane
pretBanane = '5'
pretCartofi = 4
print(int(pretBanane) + pretCartofi)
sumaDePlata = int(pretBanane) + pretCartofi
print(sumaDePlata)

# Alte EXEMPLE de TYPE CASTING: bool(), float()
# - BOOL() instructiunea va printa pe ecran cifra 1 pentru ca boolean-ul True / False poate sa mai fie reprezentat sub forma de 1 si 0
variabila_bool_True = True
variabila_bool_False = False
print(int(variabila_bool_True))
print(int(variabila_bool_False))

# - FLOAT() conversia de la float la int se face cu pierdere de date (elimina zecimalele)
variabila_float = 1.67
variabila_int = 13
print(float(variabila_int))
print(int(variabila_float))

# STRING to INT
# instructiunea aceasta va returna eroare pentru ca castingul de la string la int este incompatibil
# Vom avea eroarea ValueError: invalid literal for int() with base 10: 'Suntem la curs'
variabila_string = 'Suntem la curs'
# print(int(variabila_string))


# ************************************************************************************************************

# b. Print cu FORMATARE => 'formatam' continutul pe care vrem sa il printam folosindu-ne de print(f''), acolade {} si variabilele
# care contin valoarea pe care noi vrem sa o afisam in consola
print(
    f'Numele meu este {myConcat1} {myConcat2} , am {myConcat3} ani, inaltimea: {myConcat4} si sunt pozitiva COVID?!: {myConcat5}')

"""
 ********************************************* TIPURI DE DATE **************************************************************
Un tip de data este o proprietate prin intermediul careia putem sa informam sistemul cu privire la ce tip de informatie 
este salvat la adresa de memorie in cauza
In Python exista urmatoarele tipuri de date:
A. Numeric
    1. int = stocheaza numai numere intregi (pozitive sau negative)
    2. float = stocheaza numai numere zecimale -> 2 va fi transformat in 2.0
    3. complex = stocheaza numai numere complexe -> 2+3j

B. Boolean
boolean = stocheaza numai valori True sau False

C. Sequence Type => o colectie ordonata de tipuri de date similare sau diferite
    1. String = o colectie de unul sau mai multe caractere, pusa intre ghilimele (simple '' sau duble "")
e.g. In Java exista doua tipuri de stocare a textului:
1. cu tipul de data char (care este un tip de data primitiv) -> poate sa stocheze un singur caracter - caracterul trebuie pus intre apostroafe
2. cu tipul de data String (care este un tip de data neprimitiv) -> Poate sa stocheze mai multe caractere - caracterul trebuie pus intre ghilimele
In pyhton nu exista diferenta asta, adica nu avem char vs string. Indiferent daca punem textul intre ghilimele sau apostroafe, tipul va fi tot string

    2. List =  colectie ordonata de tipuri de date diferite sau de acelasi fel, puse intre paranteze patrate []
e.g.:
myList = ['Hello', 'H', 23, True, [23.07, -2 + 7j], 'python', False]

    3. Tuple = colectie ordonata de tipuri de date diferite sau de acelasi fel, puse intre paranteze rotunde ()
!!!! Diferenta dintre Liste si Tuple este ca tuple-le nu mai pot fi modificate dupa ce se creeaza, deci sunt imutabile/neschimbabile 
e.g.:
myTuple = ('Hello', 'H', 23, True, (23.07, -2 + 7j), 'python', False) 

D. Set - o colectie NEORDONATA de tipuri de date, iterabila si mutabila, care nu suporta elemente duplicate
e.g. mySet = set([77, 13.09,'PYTHON', True, 'True', True, 'magic', 'python', 13.09, False, 2 - 7j, -77])

E. Dictionary - o colectie neordonata de elemente pereche de tipul KEY - VALUE
e.g.: 
myDict = {
            'Nume': 'Alexa', 
            'Prenume': 'Adela', 
            'Varsta': 33, 
            'Casatorita': True, 
            'Inaltime': 1.67, 
            'Gen': 'f', 
            'Optiuni': [1, 2, 3, 4],
            1: 'Invat python',
            2: 'Invat testare automata'
        }
Cum accesez elementele?
print(myDict['Optiuni'])
print(myDict[2])
print(myDict['Casatorita'])
"""

variabila_int = 123
variabila_float = 12.3  # ATENTIE! limitarea de zecimala se face cu caracterul ".", nu cu caracterul ","
variuabila_complex = 2 + 4j
variabila_bool_true, variabila_bool_false = True, False
variabila_string = "Suntem la curs!?"
variabila_list = ['Hello', 'H', 23, True, [23.07, -2 + 7j], 'python', False]
variabila_tuplu = ('Hello', 'H', 23, True, (23.07, -2 + 7j), 'python', False)
variabila_set = set([77, 13.09, 'PYTHON', True, 'True', True, 'magic', 'python', 13.09, False, 2 - 7j, -77])
variabila_dict = {
    'Nume': 'Alexa',
    'Prenume': 'Adela',
    'Varsta': 33,
    'Casatorita': True,
    'Inaltime': 1.67,
    'Gen': 'f',
    'Optiuni': [1, 2, 3, 4],
    1: 'Invat python',
    2: 'Invat testare automata'
}

"""
************************* FUNCTIA TYPE() **********************************
- Functia type este o functie care returneaza tipul de data al unei variabile. 
- Analizeaza tipul de data al unei variabile si il trimite catre exterior
- Type casting inseamna o modalitate prin care putem sa schimbam tipul de data al unei variabile
- Type casting este TEMPORAR
"""

# Folosirea functiei type
print(type(variabila_string))
print(type(variabila_float))
print(type(variuabila_complex))
print(type(variabila_bool_false))
print(type(variabila_bool_true))
print(type(variabila_int))
print(type(variabila_list))
print(type(variabila_tuplu))
print(type(variabila_set))
print(type(variabila_dict))

# Folosirea unui type casting
print(type(str(variabila_float)))
print(type(str(variabila_int)))
print(type(int(variabila_float)))
print(type(int(variabila_bool_false)))
print(type(int(variabila_bool_true)))
print(type(str(variabila_bool_true)))
print(type(str(variabila_bool_false)))

"""
******************************* ASSERT ****************************************************
Assert este o modalitate prin care putem sa facem comparatii si sa decidem daca un rezultat este asteptat sau nu
Assert este un cuvant care este tradus ca EVALUARE
Daca comparatia returneaza True, atunci sistemul va merge mai departe cu executarea urmatoarei instructiuni
Daca comparatia returneaza False, atunci sistemul va opri executia programului curent si va returna eroare: AssertionError
Componentele unui ASSERT:
- variabila care se compara
- operatorul de comparatie (==)
- variabila cu care se compara
- mesajul de eroare in cazul in care comparatia nu returneaza True (optional)
!!!!Atentie, comparatia tine cont de tipul de data
"""

imi_place_la_curs = True
assert imi_place_la_curs == True, "Error, error: studenti plictisiti"
print("Test passed, yeey, fac treaba buna la curs!")

# imi_place_la_curs = False
# assert imi_place_la_curs==True,"Error, error: studenti plictisiti"
# print("Test passed, yeey, fac treaba buna la curs!")

"""
7. Funcția input()
Functia input este o modalitate prin care putem sa introducem valori de la tastatura
Daca nu dam niciun parametru functiei, atunci nu ni se va afisa nimic pe ecran
Optiunea aceasta NU este recomandata pentru ca utilizatorul nu va sti ce sa faca
Daca vrem sa dam parametri, trebuie specificati intre ghilimele sau apostroafe
By default, tipul de date al unei valori date de la tastatura va fi string. 
!!! Atentie la incompatibilitati in caz de adunare 
"""
# Exercitiu: vrem sa calculam suma a doua numere date de la tastatura si sa afisam suma numerelor pe ecran

# a = int(input("Introduceti primul numar: "))
# b = int(input("Introduceti al doilea numar: "))
# print('Suma celor doua numere introduse de la tastatura este: ', a+b)

# a = float(input("Introduceti primul numar: "))
# b = int(input("Introduceti al doilea numar: "))
# print('Suma celor doua numere introduse de la tastatura este: ', a+b)

# a = str(input("Introduceti primul numar: "))
# b = int(input("Introduceti al doilea numar: "))
# print('Suma celor doua numere introduse de la tastatura este: ', a+b)

# => instructiunea va da eroare pentru ca nu poate sa adune int si string
# Eroarea va fi returnata pentru ca semnul "+" are o semnificatie diferita pentru int vs string
# La int inseamna ADUNARE, la string inseamna CONCATENARE

"""
Avem o aplicatie bancara
Vrem sa verificam daca la logare, parola este corecta
Utilizatorul va fi indentificat pe baza de CNP. 
"""

# parola_asteptata = "pass123"
# utilizatorul_asteptat = "anton_batman"
# cnp_asteptat = "5960123784521"
# parola_introdusa = input("Va rugam sa introduceti parola: ")
# cnp_introdus = input("Va rugam sa introduceti cnp-ul: ")
# if(cnp_asteptat == cnp_introdus):
#     utilizatorul_introdus =  utilizatorul_asteptat
#     assert parola_asteptata == parola_introdusa, "Error: parola introdusa nu este corecta! Va rugam sa incercati din nou!"
# else:
#     input("CNP-ul dumneavoastra nu a fost gasit! Va rugam sa introduceti utilizatorul: ")
#     assert parola_asteptata == parola_introdusa, "Error: parola introdusa nu este corecta! Va rugam sa incercati din nou!"


'''
************************ STRING (index, len(), slicing, metode) ******************************************
Fiecare caracter dintr-un string, are un număr asociat (index), începând de la 0.
● Funcția LEN() ne spune câte caractere are stringul.
● Slicing - putem accesa ‘felii’ din string folosind următoarea sintaxă:
 => My_str[start_pos, end_pos, pas]
● După my_str dacă punem . ajungem la funcții ajutătoare:
    - Upper, 
    - lower, 
    - replace, 
    - count etc.
Note: Accesați descrierea lor apăsând CTRL+Click pe numele lor.

'''
prop = 'Numele meu este Alexa Adela!'
print(len(prop))  # => 28
print(prop[0])  # => N
print(prop[6])  # => aici returneaza spatiu, adica nu se vede nimic in consola
print(prop[9])  # => u
print(prop[27])  # => !
# print(prop[28])  # => returneaza eroare pentru ca indexul incepe de la 0
print(prop[0:3])  # => Num
print(prop[::-1])  # parcurgere si printare inversa
print(prop.upper())  # printeaza tot continutul cu litere mari
