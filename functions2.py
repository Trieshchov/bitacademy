def small_letters(string):                           #create function
    total_small_letters = 0
    for character in string:
        if "a" <= character <= "z":
            total_small_letters +=1
    return total_small_letters

woord = ["Bit", "Academy", "Bit-Academy", "bit", "-","AcAdEmY"] #list word
for n in woord:                                #loop
    aantal = small_letters(n)          # execute the function from line 1
    print(f"Er zitten {aantal} kleine letters in {n}")
def counts_total(woord):
    total = 0
    for n in woord:
        aantal = small_letters(n)
        total = aantal + total
    print(total)
counts_total(woord)         #execute the function from line 12

# We can calculate the number of small letters for each word
# But now we want the sum of all those letters
# We need to make a function for this.
# We can copy what we already did (calculating each word) and alter it


# symbol = input("Tot welke getal? ")
# y = range(1,int(symbol))
# for n in y:
#     print(n)
# x = range(int(symbol),0,-1)
# for n in x:
#     print(n)
