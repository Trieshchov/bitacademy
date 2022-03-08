stem_Zah = 0
stem_Dom = 0
while True:
    stem = input("Op wie wil je stemmen?" )
    if stem.lower() == "dominique":
        stem_Dom = stem_Dom + 1
    elif stem.lower() == "zacharia":
        stem_Zah = stem_Zah + 1
    elif stem.upper() == "UITSLAG":
        break

if stem_Dom > stem_Zah:
    print("Dominique heeft gewonnen")
elif stem_Dom < stem_Zah:
    print("Zacharia heeft gewonnen")
else:
    print("Dominique en Zacharia hebben gelijk aantal samen")
