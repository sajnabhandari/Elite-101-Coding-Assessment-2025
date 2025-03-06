# goal: free table tracking software: 
# lvl 1. list all free tables ('o') & output the list of free table IDs
def list_free_tables(restaurant_tables):
    free_tables = []  # use this to store the list of free tables
    row = 1  # not 0, cuz at 0 is the label of how many spots are at the table
    # loop thru rows 
    while row < len(restaurant_tables):
        column = 1  # for column
        while column < len(restaurant_tables[row]):  # loops thru columns
            if restaurant_tables[row][column] == 'o':  # if table = o, which indicates it being free
                free_tables.append(restaurant_tables[0][column])  # adds the table to the list
            column += 1
        row += 1
    return free_tables

# lvl 2. find 1 free table for the given amt of people to be seated & return that table (maybe the ID)
def findparty_table(restaurant_tables, party_size):
    row = 1
    while row < len(restaurant_tables):
        column = 1
        while column < len(restaurant_tables[row]):
            table_info = restaurant_tables[0][column]
            table_seats = int(table_info[table_info.index('(')+1:table_info.index(')')])  # extract number of seats
            if restaurant_tables[row][column] == 'o' and table_seats >= party_size:
                return restaurant_tables[0][column]  # returns table ID
            column += 1
        row += 1

# lvl 3. based off the party size, return all free tables that can seat that many ppl
def findall_freetables(restaurant_tables, party_size):
    free_tables = []  # list of free tables
    row = 1
    while row < len(restaurant_tables):
        column = 1
        while column < len(restaurant_tables[row]):
            table_info = restaurant_tables[0][column]
            table_seats = int(table_info[table_info.index('(')+1:table_info.index(')')])  # extract number of seats
            if restaurant_tables[row][column] == 'o' and table_seats >= party_size:
                free_tables.append(restaurant_tables[0][column])  # adds to list
            column += 1
        row += 1
    return free_tables

# lvl 4. if single table can't seat the group, check if 2 adjacent together can & return the list of all table combos (single or paired)
def findtable_pair(restaurant_tables, party_size):
    pair_free_tables = []  # list of free tables
    row = 1
    while row < len(restaurant_tables):
        column = 1
        while column < len(restaurant_tables[row]):
            table_info = restaurant_tables[0][column]
            table_seats = int(table_info[table_info.index('(')+1:table_info.index(')')])  # extract number of seats
            if restaurant_tables[row][column] == 'o' and table_seats >= party_size:
                pair_free_tables.append(restaurant_tables[0][column])  # adds to list
                # check if the next table can be used to seat the party
                if column+1 < len(restaurant_tables[row]):  # so it doesn't go out of range
                    next_table_info = restaurant_tables[0][column+1]
                    next_table_seats = int(next_table_info[next_table_info.index('(')+1:next_table_info.index(')')])  # extract number of seats of next table
                    if restaurant_tables[row][column] == 'o' and restaurant_tables[row][column+1] == 'o' and table_seats + next_table_seats >= party_size:  # checks if combined seats meet the party size
                        pair_free_tables.append(restaurant_tables[0][column])  # adds 1st table
                        pair_free_tables.append(restaurant_tables[0][column+1])  # adds 2nd table
            column += 1
        row += 1
    return pair_free_tables

# test
restaurant_tables = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'x',      'o',      'o',      'o',      'o',      'x'],
    [2,        'o',      'x',      'o',      'o',      'x',      'o'],
    [3,        'x',      'x',      'o',      'x',      'o',      'o'],
    [4,        'o',      'o',      'o',      'x',      'o',      'x'],
    [5,        'o',      'x',      'o',      'x',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'x',      'o']
]


# Running the test cases
print("Level 1: List all free tables")
free_tables = list_free_tables(restaurant_tables)
print(free_tables)  #  output: ['T1', 'T3', 'T4']

print("\nLevel 2: Find 1 free table for party size = 2")
party_size = 2
table = findparty_table(restaurant_tables, party_size)
print(table)  # output: 'T1' or 'T3'

print("\nLevel 3: Find all free tables that can seat at least 2 people")
party_size = 2
free_tables = findall_freetables(restaurant_tables, party_size)
print(free_tables)  #  output: ['T1', 'T3', 'T4']

print("\nLevel 4: Check if a single or paired table can seat a party of size 5")
party_size = 5
pair_free_tables = findtable_pair(restaurant_tables, party_size)
print(pair_free_tables)  #  output: ['T4', 'T5']
