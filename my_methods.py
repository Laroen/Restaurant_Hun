def read(document):                                        # 1. feladat
    with open(f'{document}','r',encoding='utf8') as file:
        clear_data = []
        restaurant_nrp = {}
        country_nrp = set()
        for i in file.readlines()[1:]:                                      # file beolvasása listába
            clear_data.append(i.strip().split("\t"))
        for i in clear_data:                               #Ez fogja az éttermeket városok alapján kinyerni, ismétlődés nélkül
            if i[1] not in restaurant_nrp:                 #2. feladathoz
                restaurant_nrp[i[1]] = set()
                restaurant_nrp[i[1]].add(i[0])
            else:
                restaurant_nrp[i[1]].add(i[0])
            country_nrp.add(i[2])                             # Országok gyűjtése halmazba, ismétlődések elkerülése miatt (8. feladat)
        return clear_data, restaurant_nrp, country_nrp      # Visszatérés az adatokkal

def still_open(clear_data):                                 # még nyitott üzletek adatainak kinyerése listába ( 3. feladat)
    not_closed = []
    for i in clear_data:
        if int(i[4]) == 0:
            not_closed.append(i)
        else:
            continue
    return not_closed

def closed(clear_data):                                     #A bezárt éttermek adatainak kinyerése, ismétlődés vizsgálattal
    restaurant_closed = []                                  #4. feladathoz
    for i in clear_data:
        if int(i[4]) != 0:
            if i[0] in restaurant_closed and i[1] in restaurant_closed:
                continue
            else:
                restaurant_closed.append(i)
    return restaurant_closed

def got_michelin(clear_data):                               #Eddigi összes michelin csillagot kapott éttermek kinyerése
    rst_michelin = {}                                       #5. feladathoz
    for i in clear_data:
        if int(i[5]) > 0:
            if i[1] not in rst_michelin:
                rst_michelin[i[1]] = set()
                rst_michelin[i[1]].add(i[0])
            else:
                rst_michelin[i[1]].add(i[0])
        else:
            continue
    return rst_michelin

def highest_michelin(not_closed):                   # letöbb csillaggal rendelekző éttermek meghatározása
    rst_best_index = []                             # amik még működnek (7. feladat)
    stars = []
    for i,data in enumerate(not_closed):
        if int(data[5]) > 0:
            stars.append(int(data[5]))
    for index,data2 in enumerate(not_closed):
        if int(data2[5]) == max(stars):
            rst_best_index.append(index)
    return rst_best_index

def reopen(rst_closed,clear_data):                  # újranyitott üzlet / üzletek meghatározása 9. feladat
    rst_reopened = []
    for i in rst_closed:
        for j in clear_data:
            if int(j[4]) == 0 and i[1] in j and i[0] in j:
                rst_reopened.append(j)
            else:
                continue
    return rst_reopened

def unsuccesful(clear_data):            # legkevésbé siekresek meghatározása ,amik már bezártak, csillag nélkül
    index = []                          #6. feladat
    min_year=[]
    rst_unsucces = []
    for i,data in enumerate(clear_data):
        if int(data[5]) == 0 and int(data[4]) > 0:
            index.append(i)
            min_year.append(abs(int(data[4]))-int(data[3]))
        else:
            continue
    for i,data2 in enumerate(min_year):
        if data2 == min(min_year):
            rst_unsucces.append(clear_data[index[i]])
    return rst_unsucces