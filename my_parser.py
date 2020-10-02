import sys
from json import loads
from re import sub

columnSeparator = "|"

# Dictionary of months used for date transformation
MONTHS = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',\
        'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

"""
Returns true if a file ends in .json
"""
def isJson(f):
    return len(f) > 5 and f[-5:] == '.json'

"""
Converts month to a number, e.g. 'Dec' to '12'
"""
def transformMonth(mon):
    if mon in MONTHS:
        return MONTHS[mon]
    else:
        return mon

"""
Transforms a timestamp from Mon-DD-YY HH:MM:SS to YYYY-MM-DD HH:MM:SS
"""
def transformDttm(dttm):
    dttm = dttm.strip().split(' ')
    dt = dttm[0].split('-')
    date = '20' + dt[2] + '-'
    date += transformMonth(dt[0]) + '-' + dt[1]
    return date + ' ' + dttm[1]

"""
Transform a dollar value amount from a string like $3,453.23 to XXXXX.xx
"""

def transformDollar(money):
    if money == None or len(money) == 0:
        return money
    return sub(r'[^\d.]', '', money)

"""
Parses a single json file. Currently, there's a loop that iterates over each
item in the data set. Your job is to extend this functionality to create all
of the necessary SQL tables for your database.
"""
def parseJson(json_file):
    #Initialize lists that store all of the json information
    item_table = []
    bid = []
    user = []
    location = []
    country = []
    rating = []
    lineItem = []
    category = []

    bidsID = 0 # Keeps track of the bidsID

    #Reads through all of the json files
    with open(json_file, 'r') as f:
        items = loads(f.read())['Items'] # creates a Python dictionary of Items for the supplied json file
        for item in items:
            #Adds to item table
            item_table.append(
                item["ItemID"] + columnSeparator + item["Name"] + columnSeparator + item["First_Bid"] + columnSeparator + item["Number_of_Bids"] + columnSeparator
                + item["Currently"] + columnSeparator + transformDttm(item["Started"]) + columnSeparator + transformDttm(item["Ends"])
            )
            if item["Bids"] is not None:
                for bids in item["Bids"]:
                    #Adds to bids table
                    bid.append(
                        str(bidsID) + columnSeparator + bids["Bid"]["Bidder"]["UserID"]  + columnSeparator + transformDttm(bids["Bid"]["Time"])
                    + columnSeparator + bids["Bid"]["Amount"]
                    )
                    bidsID += 1 #Increments the bid ID

            #Adds to user table
            user.append(item)

            #Adds to location table
            location.append(item["Location"])

            #Adds to country table
            country.append(item["Country"])
            #rating.append()
            #lineItem.append()
            #category.append()

    #Writes to item.dat
    with open("item.dat", 'w') as f:
        for line in item_table:
            f.write(line + "\n")

    #Writes to bit.dat
    with open("bid.dat", 'w') as f:
        for line in bid:
            f.write(line + "\n")

    #Writes to user.dat
    """with open("user.dat", 'w') as f:
        for line in user:
            f.write(line + "\n")"""

    #Writes to location.dat
    with open("location.dat", 'w') as f:
        for line in location:
            f.write(line + "\n")

    #Writes to country.dat
    with open("country.dat", 'w') as f:
        for line in country:
            f.write(line + "\n")

    """with open("rating.dat", 'w') as f:
        for line in rating:
            f.write(line + "\n")
    with open("lineItem.dat", 'w') as f:
        for line in lineItem:
            f.write(line + "\n")
    with open("category.dat", 'w') as f:
        for line in category:
            f.write(line + "\n")"""

"""
Loops through each json files provided on the command line and passes each file
to the parser
"""
def main(argv):
    if len(argv) < 2:
        print('Usage: python skeleton_json_parser.py <path to json files>')
        sys.exit(1)
    # loops over all .json files in the argument
    for f in argv[1:]:
        if isJson(f):
            parseJson(f)
            print ("Success parsing " + f)

if __name__ == '__main__':
    main(sys.argv)
