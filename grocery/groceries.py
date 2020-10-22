# Returns valid float input
def FloatCheck(input_string):
    while True:
        num = input(input_string)
        try: # check for float
            num = float(num)
            break
        except ValueError:
            print("Invalid input. Try again.\n")
    return num

# Displays computed totals
def DisplayBalances(balances, tax):
    grandTotal = 0
    print("\n--All values are after tax--\n")
    for name in balances: # add tax to each person's balance
        if balances[name] > 0:
            balances[name]+=tax
            print(name, "'s total: ", round(balances[name], 2), sep='')
            grandTotal+=balances[name]
            
    print("Grand total:", round(grandTotal, 2))

# Get valid names
def GetNames():
    tempNames = set()
    names = set(input("How to split?: ").lower())
    # only take valid names
    if 'm' in names: tempNames.add('m')
    if 'e' in names: tempNames.add('e')
    if 'n' in names: tempNames.add('n')
    if 'x' in names: tempNames.add('x')

    if 'a' in names: 
        tempNames.add('m')
        tempNames.add('e')
        tempNames.add('n')
                
    return tempNames

def main():
    names, allNames = (set() for i in range(2)) # sets of people
    balances = {'m':0,'e':0,'n':0,'x':0} # keeps track of balances

    print("--Welcome to grocery calculator--\n")
    print("-Enter in cost and enter keywords for how to split")
    print("-Input a cost of 0 to quit\n")
    print("-Keyword ex: 'enm' splits between eric, noah, and moeez")
    print("-Possible keywords: | m:moeez | e:eric | n:noah | x:xtra | a:all except xtra")

    cost = 1.0
    while cost != 0:
        cost = FloatCheck("Cost: ") # gets cost input and checks if float
        if cost == 0: # end loop if cost entered is 0
            continue
        
        # ask for input and remove duplicates
        names = GetNames() 
        allNames = allNames.union(names)
        if not names: # check if no valid names
            print("No valid keywords in input\n")
            continue   

        for name in names:
            balances[name] += cost/len(names) # compute balances

    tax = FloatCheck("Tax: ") / len(allNames) # computes tax for each
    DisplayBalances(balances, tax)  

if __name__ == "__main__":
    main()