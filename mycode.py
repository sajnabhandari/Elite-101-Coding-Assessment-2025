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
# lvl 2. find 1 free table for the given amt of people to be seated & return that table (mybe the ID)
def findparty_table (restaurant_tables, party_size):
    row = 1 
    while row < len(restaurant_tables):
        column = 1
        while column < len(restaurant_tables[row]):
            table_seats = int(restaurant_tables[0][column][3:5])# gets the number of seats at the table
            if restaurant_tables[row][column] == 'o' and table_seats>=party_size:
                return restaurant_tables[0][column] # returns table id
            column += 1
        row += 1
# Lvl 3. based off the party size, return all free tables that can seat that many ppl
def findall_freetables (restaurant_tables, party_size):
    free_tables = [] # list of free tables
    row = 1
    while row < len(restaurant_tables):
        column = 1
        while column < len(restaurant_tables[row]):
            table_seats = int(restaurant_tables[0][column][3:5])
            if restaurant_tables[row][column] == 'o' and table_seats>=party_size:
                free_tables.append(restaurant_tables[0][column]) #adds to list
            column += 1
        row += 1
    return free_tables
# lvl 4. if single table can't seat the group, check if 2 adjacent together can-& return the list of all table combos (single or paired)
def findtable_pair (restaurant_tables, party_size):
    pairfree_tables = [] # list of free tables
    row = 1
    while row < len(restaurant_tables):
        column = 1
        while column < len(restaurant_tables[row]):
            table_seats = int(restaurant_tables[0][column][3:5])
            if restaurant_tables[row][column] == 'o' and table_seats>=party_size:
                pairfree_tables.append(restaurant_tables[0][column]) #adds to list
                #checks if the next table can be used to seat the party
            if column+1 < len (restaurant_tables[row]): # so it doesn't go out of range
                table_seats2 = int(restaurant_tables[0][column+1][3:5]) # get seats of next table
                if restaurant_tables[row][column] == 'o' and restaurant_tables[row][column+1] == 'o' and table_seats+table_seats2>=party_size: # checks if combined seats meets the party size
                    pairfree_tables.append(restaurant_tables[0][column]) # adds 1st table
                    pairfree_tables.append(restaurant_tables[0][column+1]) #adds 2nd table 
    return free_tables
# also maybe print it out in a string for the user (didnt do it in this prgrm)

