import my_methods
import locale
locale.setlocale(1,('Hungarian_Hungary','850'))


def menu():
    print("1. feladat: Olvassa be egy alkalmas adatszerkezetbe az állomány tartalmát!")
    print("2. feladat: Jelezze ki, összesen hány étteremmel került GR kapcsolatba!")
    print("3. feladat: Írja ki a jelenleg is működő éttermek számát!")
    print("4. feladat: Számolja ki, hány százalékuk zárt be az adatfelvétel időpontjáig!")
    print("5. feladat: Írja ki azokat az éttermeket és városaikat, amelyek kaptak már Michelin-csillagot")
    print("6. feladat: Melyik éttermek voltak a legkevésbé sikeresek (nem kaptak csillagot és a "
           "legrövidebb ideig voltak nyitva)?")
    print("7. feladat:  Melyikek a legjobb (a legtöbb csillaggal rendelkező) és még működő éttermek?")
    print("8. feladat: Sorolja fel névsorrendben, ismétlődés nélkül azokat az országokat, amelyekben "
          "működése alatt tevékenykedett a sztárszakács!")
    print("9. feladat: Volt-e újranyitott étterem ugyanabban a városban? Mikor és hol?")
    print("0: Kilépés !!\n")
    k = int(input('Melyik feladat megoldásait szeretné megtekinteni?\nKérem válasszon:\t'))
    return k

csv = 'GordonRamsayRestorants.csv'

my_clear_data,my_restaurant_nrp,my_country_nrp = my_methods.read(csv)

my_country_nrp = list(my_country_nrp)
print(sorted(my_country_nrp, key=locale.strxfrm))

my_not_closed = my_methods.still_open(my_clear_data)

my_restaurant_closed = my_methods.closed(my_clear_data)

my_rst_michelin = my_methods.got_michelin(my_clear_data)

my_rst_best_star = my_methods.highest_michelin(my_not_closed)

my_rst_reopened = my_methods.reopen(my_restaurant_closed,my_clear_data)

my_rst_unsucces = my_methods.unsuccesful(my_clear_data)

rst_counter = 0
for i in my_restaurant_nrp:
    rst_counter += len(my_restaurant_nrp[i])


while (k := menu()) > 0 or k < 9:
    print()
    if k == 1:
        with open(f"{k}.megoldás.txt", 'w', encoding="utf8") as write:
            print('Az első feladat megoldásához a my_methods-ból kellett meghívni az read nevű eljárást.')
            print('Az első feladat megoldásához a my_methods-ból kellett meghívni az read nevű eljárást.', file=write)
    elif k == 2:
        with open(f"{k}.megoldás.txt", 'w', encoding="utf8") as write:
            print(f'2. feladat:\n{rst_counter} db Étteremmel volt kapcsolatba')
            print(f'2. feladat:\n{rst_counter} db Étteremmel volt kapcsolatba\n', file=write)
    elif k == 3:
        with open(f"{k}.megoldás.txt", 'w', encoding="utf8") as write:
            print(f'3. feladat:\n{len(my_not_closed)} db Étterem működik jelenleg is.')
            print(f'3. feladat:\n{len(my_not_closed)} db Étterem működik jelenleg is.\n', file=write)
    elif k == 4:
        with open(f"{k}.megoldás.txt", 'w', encoding="utf8") as write:
            print(f'4. feladat:\n{len(my_restaurant_closed)/len(my_clear_data)*100:.2f}'
                    f' % zárt be az adatfelvételig.')
            print(f'4. feladat:\n{len(my_restaurant_closed) / len(my_clear_data) * 100:.2f}'
                    f' % zárt be az adatfelvételig.\n', file=write)
    elif k == 5:
        with open(f"{k}.megoldás.txt", 'w', encoding="utf8") as write:
            print(f'5. feladat:')
            print(f'5. feladat:', file=write)
            for i in my_rst_michelin.keys():
                print(f'{i}:', '; '.join(my_rst_michelin[i]))
                print(f'{i}:', '; '.join(my_rst_michelin[i]), file=write)
    elif k == 6:
        with open(f"{k}.megoldás.txt", 'w', encoding="utf8") as write:
            print('6. feladat')
            print('6. feladat', file=write)
            for i in my_rst_unsucces:
                print(*i,sep=' - ')
                print(*i,sep=' - ', file=write)
    elif k == 7:
        with open(f"{k}.megoldás.txt", 'w', encoding="utf8") as write:
            print('7. feladat:')
            print('7. feladat:',file=write)
            for i in my_rst_best_star:
                print(*my_not_closed[i],sep=" - ")
                print(*my_not_closed[i],sep=" - ",file=write)
    elif k == 8:
        with open(f"{k}.megoldás.txt", 'w', encoding="utf8") as write:
            print(f'8. feladat:\nEzekben az országokban tevékenykedett G.R.:\n '
                    f'{"; ".join(sorted(my_country_nrp, key=locale.strxfrm))} ',sep="; ")
            print(f'8. feladat:\nEzekben az országokban tevékenykedett G.R.:\n '
                  f'{"; ".join(sorted(my_country_nrp, key=locale.strxfrm))} ', sep="; ", file=write)
    elif k == 9:
        with open(f"{k}.megoldás.txt", 'w', encoding="utf8") as write:
            print('9. feladat')
            print('9. feladat',file=write)
            for i in my_rst_reopened:
                print(i[3], *i[:2], sep=' - ')
                print(i[3], *i[:2], sep=' - ', file=write)
    elif k == 0:
        break
    else:
        print('Rossz értéket adott meg!')
    print()
