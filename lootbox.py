import rewards
from rewards import get_new_skin
rare = 0
common = 0
epic = 0 
legendary = 0
for x in range(5):
    y = get_new_skin()
    if y.casefold() == "common":
        common += 1
    elif y.casefold() == "rare":
        rare += 1
    elif y.casefold() == "epic":
        epic += 1
    else:
        legendary += 1
if common != 0:
    print(f"{common}x COMMON")
if rare != 0:
    print(f"{rare}x RARE")
if epic != 0:
    print(f"{epic}x EPIC")
if legendary != 0:
    print(f"{legendary}x LEGENDARY")
