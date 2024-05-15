"""
Bir Packets adinda folder(Paket) yaradin. Icinde samitler adinda bir file (modul) olsun.
Onunda icinde samitleri_al adinda bir funksiya olsun.

Nece calisacaq ?:
Bu folderden colde yerlesen main.py faylimizda bu methodu cagirmali ve icine bir deyer (cumle) gondermeliyik.

Numune cagrilma:
'Salam necesen ... '

netice:
{'s', 'l', 'm', 'n', 'c'} >> heresinden bir dene olsa kifayetdir
"""
def samitleri_al(cumle):
    samitler = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
    cumledeki_samitler = set()

    for char in cumle.lower():
        if char in samitler:
            cumledeki_samitler.add(char)

    return cumledeki_samitler


from Packets.samitler import samitleri_al

cumle = "Salam necesen ..."
sonuc = samitleri_al(cumle)
print(sonuc)