#goal: free table tracking software: 
# lvl 1. list all free tables ('o') & output the list of free table IDs
def list_free_tables(restaurant_tables):
    free_tables = [] # use this to store the list of free tables
    row = 1 # not 0, cuz at 0 is the label of how many spots are at the table
    #loop thru rows 
    while row < len(restaurant_tables):
        column = 1 # for column
        while column < len(restaurant_tables[row]): #loops thru columns
            if restaurant_tables[row][column] == 'o': # if table = o, which indicates it being free
                free_tables.append(restaurant_tables[0][column]) # adds the table the list 
            column += 1
        row += 1
    # end of the loop
    return free_tables
# Lvl 2.Find 1 free table for the given amount of people to be seated & return that table (maybe the ID)
def findparty_table(restaurant_tables, party_size):
    row = 1 
    while row < len(restaurant_tables):
        column = 1
        while column < len(restaurant_tables[row]):
            # Extract seat number from the table ID, e.g., 'T1(2)' -> 2
            table_seats = int(restaurant_tables[0][column].split('(')[1].split(')')[0])  # Correct extraction
            if restaurant_tables[row][column] == 'o' and table_seats >= party_size:
                return restaurant_tables[0][column]  # returns table id
            column += 1
        row += 1

# Lvl.3: Find all free tables that can seat at least 'party_size' people
def findall_freetables(restaurant_tables, party_size):
    free_tables = []  # list of free tables
    row = 1
    while row < len(restaurant_tables):
        column = 1
        while column < len(restaurant_tables[row]):
            table_seats = int(restaurant_tables[0][column].split('(')[1].split(')')[0])  # Correct extraction
            if restaurant_tables[row][column] == 'o' and table_seats >= party_size:
                free_tables.append(restaurant_tables[0][column])  # Adds to list
            column += 1
        row += 1
    return free_tables

# lvl 4. if single table can't seat the group, check if 2 adjacent together can-& return the list of all table combos (single or paired)
#def findtable_pair (restaurant_tables, party_size):
 #   pairfree_tables = [] # list of free tables
  #  row = 1
   # while row < len(restaurant_tables):
    #    column = 1
     #   while column < len(restaurant_tables[row]):
      #      table_seats = int(restaurant_tables[0][column][3:5])
       #     if restaurant_tables[row][column] == 'o' and table_seats>=party_size:
        #        pairfree_tables.append(restaurant_tables[0][column]) #adds to list
         #       #checks if the next table can be used to seat the party
          #  if column+1 < len (restaurant_tables[row]): # so it doesn't go out of range
           #     table_seats2 = int(restaurant_tables[0][column+1][3:5]) # get seats of next table
            #    if restaurant_tables[row][column] == 'o' and restaurant_tables[row][column+1] == 'o' and table_seats+table_seats2>=party_size: # checks if combined seats meets the party size
             #       pairfree_tables.append(restaurant_tables[0][column]) # adds 1st table
              #      pairfree_tables.append(restaurant_tables[0][column+1]) #adds 2nd table 
    #return pairfree_tables
# also maybe print it out in a string for the user (didnt do it in this prgrm)


# test
# ------------------------------------------------------------------------------------
# This second layout serves as a test case where some tables ('x') are already occupied.
# Use this for testing your logic to:
#   - Find free tables (marked 'o')
#   - Check if those tables meet a certain capacity (from the header row, e.g. 'T1(2)')
#   - Potentially combine adjacent tables if one alone isn't enough for a larger party.
# ------------------------------------------------------------------------------------

restaurant_tables = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'x',      'o',      'o',      'o',      'o',      'x'],
    [2,        'o',      'x',      'o',      'o',      'x',      'o'],
    [3,        'x',      'x',      'o',      'x',      'o',      'o'],
    [4,        'o',      'o',      'o',      'x',      'o',      'x'],
    [5,        'o',      'x',      'o',      'x',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'x',      'o']
]

print("Level 1: List all free tables")
free_tables = list_free_tables(restaurant_tables)
print(free_tables)  

print("\nLevel 2: Find 1 free table for party size = 2")
party_size = 2
table = findparty_table(restaurant_tables, party_size)
print(table)  

print("\nLevel 3: Find all free tables that can seat at least 2 people")
party_size = 2
free_tables = findall_freetables(restaurant_tables, party_size)
print(free_tables) 
