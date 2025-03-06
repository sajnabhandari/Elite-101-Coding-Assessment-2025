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
                free_tables.append(restaurant_tables[0][column])
            column += 1
        row += 1
    return free_tables
# lvl 2. find 1 free table for the given amt of people to be seated & return that table (mybe the ID)
# Lvl 3. based off the party size, return all free tables that can seat that many ppl
# lvl 4. if single table can't seat the group, check if 2 adjacent together can-& return the list of all table combos (single or paired)
# also maybe print it out in a string for the user

