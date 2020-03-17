def split(split_list, cost):
    split_factor = len(split_list) # amount to split by
    split_dict = {}
    for el in split_list: # add each person to dict with price to pay
        split_dict[el] = cost / split_factor
    return split_dict

def float_check(input_string):
    while True:
        num = input(input_string)
        try: # check for float
            num = float(num)
            break
        except ValueError:
            print("Invalid input. Try again.\n")
    return num

def main():
    # initialize values
    m_total = 0.0
    e_total = 0.0
    n_total = 0.0
    x_total = 0.0
    total_people = 0
    tax = 0.0
    cost = 1.0

    print("--Welcome to grocery calculator--\n")
    print("-Enter in cost and enter keywords for how to split")
    print("-Input a cost of 0 to quit\n")
    print("-Keyword ex: 'enm' splits between eric, noah, and moeez")
    print("-Possible keywords: | m:moeez | e:eric | n:noah | x:xtra")

    while cost != 0:
        to_split_list = [] # holds people to split
        cost = float_check("Cost: ") # gets cost input and checks if float
        if cost == 0: # end loop check
            continue
        to_split_str = input("How to split?: ")
        to_split_str = to_split_str.lower() # convert string to all lower
        # output inputs
        print(to_split_str)
        print(cost)

        # add people who are splitting to list
        if 'm' in to_split_str:
            to_split_list.append('m')
        if 'e' in to_split_str:
            to_split_list.append('e')
        if 'n' in to_split_str:
            to_split_list.append('n')
        if 'x' in to_split_str:
            to_split_list.append('x')
        if not to_split_list: # checks if list is empty
            print("No valid keywords in input\n")
            continue

        # returns a dict with keywords and values
        split_dict = split(to_split_list, cost)

        # adds to totals
        for key, value in split_dict.items():
            if key == 'm':
                m_total += value
            elif key == 'e':
                e_total += value
            elif key == 'n':
                n_total += value
            elif key == 'x':
                x_total += value

    # calculates total people
    if m_total:
        total_people += 1
    if e_total:
        total_people += 1
    if n_total:
        total_people += 1
    if x_total:
        total_people += 1

    tax = float_check("Tax: ") # gets tax input and checks if float
    tax = tax / total_people
    print("\n--All values are after tax--\n")
    # adds tax, rounds, and prints
    if m_total:
        m_total += tax
        m_total = round(m_total, 2)
        print("Moeez's total: ", m_total)
    if e_total:
        e_total += tax
        e_total = round(e_total, 2)
        print("Eric's total: ", e_total)
    if n_total:
        n_total += tax
        n_total = round(n_total, 2)
        print("Noah's total: ", n_total)
    if x_total:
        x_total += tax
        x_total = round(x_total, 2)
        print("Extra total: ", x_total)

    grand_total = m_total + e_total + n_total + x_total
    grand_total = round(grand_total, 2)
    print("Grand total: ", grand_total)
        
if __name__ == "__main__":
    main()
