import pandas
import locale
import numpy

locale.setlocale(1,('Hungarian_Hungary','850'))

csv = 'GordonRamsayRestorants.csv'

with open(f'{csv}', 'r', encoding='utf8') as file:
    clear_data = []
    for i in file.readlines():  # file beolvasása listába
        clear_data.append(i.strip().split("\t"))


dict_data = {}
index = 0
for i in clear_data[0]:
    dict_data[i] = []
    for j,data in enumerate(clear_data[1:]):
        clear_data[j+1][3] = int(clear_data[j+1][3])
        clear_data[j+1][4] = int(clear_data[j+1][4])
        clear_data[j+1][5] = int(clear_data[j+1][5])
        clear_data[j+1][6] = int(clear_data[j+1][6])
        clear_data[j+1][7] = int(clear_data[j+1][7])
        dict_data[i].append(data[index])
    index += 1

test_data = pandas.DataFrame(dict_data)
'''
#------------------------------------------------------------
print()
bezart = test_data["Bezaras"] > 0
#print(len(test_data))
#print(len(test_data.loc[bezart]))

print(f'4. feladat:\n{(len(test_data.loc[bezart]) / len(test_data)) * 100:.2f}'     # 4. feladat
                    f' % zárt be az adatfelvételig.')
#------------------------------------------------------------
print()
csillag_nelkul = (test_data['Michelinstar '] == 0) & (test_data["Bezaras"] > 0) &\
                 (test_data["Bezaras"] - test_data["Nyitas"] == 1)                      #6. feladat adatkinyerése

print(test_data.loc[csillag_nelkul])                                                #6. feladat kiíratás
#------------------------------------------------------------
print()
print(sorted(set(test_data['Orszag']), key=locale.strxfrm))                         # 8 feladat
#------------------------------------------------------------
print()
print(f'Jelenleg működő éttermek száma: {len(test_data[test_data["Bezaras"] == 0])}db') # 3. feladat
#------------------------------------------------------------
print()
print(f'KApott már csillagot:\n {test_data[test_data["Michelinstar "] > 0][["Etterem","Varos"]]}') # 5. feladat +csv-be íratás
feladat_5 = test_data[test_data["Michelinstar "] > 0][["Etterem","Varos"]]
feladat_5.to_csv('5-feladat.csv')
#------------------------------------------------------------

print() #  7. feladat megoldása
legtobb_csillag = (test_data["Michelinstar "] == max(test_data["Michelinstar "])) & (test_data["Bezaras"] == 0)
print(test_data.loc[legtobb_csillag])
'''
#------------------------------------------------------------
#9. feladat
'''
ujranyitott = pandas.pivot_table(test_data, index=['Varos','Etterem'], values=['Nyitas'], aggfunc='count')

print(ujranyitott)
print()
ujranyitott.to_csv('ismetlodes.csv')
with open(f'ismetlodes.csv', 'r', encoding='utf8') as ism:
    adat = []
    for i,j in enumerate(ism.readlines()[1:]):
        adat.append(j.strip().split(','))
        if int(adat[i][2]) == 2:
            keres = (test_data['Etterem'] == adat[i][1]) & (test_data['Varos'] == adat[i][0])
            print(test_data.loc[keres,'Etterem':'Bezaras'])
'''