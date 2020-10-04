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
    bidder = []
    seller = []
    location = []
    country = []
    lineItem = []
    categories = []
    compare_cate = []
    compare_loc = []
    compare_country = []
    bidderIDs = []
    sellerIDs = []

    bidsID = 0 # Keeps track of the bidsID
    categoryID = 0 # Keeps track of the categoryID
    locationID = 0 # Keeps track of the locationID
    countryID = 0 # Keeps track of te countryID
    temp = ""

    #Reads through all of the json files
    with open(json_file, 'r') as f:
        items = loads(f.read())['Items'] # creates a Python dictionary of Items for the supplied json file
        for item in items:

            #Adds seller locations to the location table
            if item["Location"] not in compare_loc:
                compare_loc.append(item["Location"])
                location.append(
                    str(locationID) + columnSeparator + item["Location"]
                )
                locationID += 1
            
            #Adds bid locations to the location table
            if item["Bids"] is not None:
                for bids in item["Bids"]:
                    if "Location" in bids["Bid"]["Bidder"]:
                        if bids["Bid"]["Bidder"]["Location"] not in compare_loc:
                            compare_loc.append(bids["Bid"]["Bidder"]["Location"])
                            location.append(
                                str(locationID) + columnSeparator + bids["Bid"]["Bidder"]["Location"]
                            )
                            locationID += 1 #Increments the locationID
            
            #Adds seller countries to the country table
            if item["Country"] not in compare_country:
                compare_country.append(item["Country"])
                country.append(
                    str(countryID) + columnSeparator + item["Country"]
                )
                countryID += 1

            #Adds bidder countries to the country table
            if item["Bids"] is not None:
                for bids in item["Bids"]:
                    if "Country" in bids["Bid"]["Bidder"]:
                        if bids["Bid"]["Bidder"]["Country"] not in compare_country:
                            compare_country.append(bids["Bid"]["Bidder"]["Country"])
                            country.append(
                                str(countryID) + columnSeparator + bids["Bid"]["Bidder"]["Country"]
                            )
                            countryID += 1 #Increments the countryID"""

            if '"' in item["Name"]:
                temp = item["Name"]
                temp = temp.replace('"', '""', 20)
            else:
                temp = item["Name"]
            #Adds to item table
            item_table.append(
                item["ItemID"] + columnSeparator + str(compare_loc.index(item["Location"])) + columnSeparator + '"' + temp + '"' + columnSeparator + transformDollar(item["First_Bid"]) + columnSeparator 
                + item["Number_of_Bids"] + columnSeparator + transformDollar(item["Currently"]) + columnSeparator + transformDttm(item["Started"]) + 
                columnSeparator + transformDttm(item["Ends"])
            )

            #Adds to bids table
            if item["Bids"] is not None:
                for bids in item["Bids"]:
                        bid.append(
                            str(bidsID) + columnSeparator + bids["Bid"]["Bidder"]["UserID"]  + columnSeparator + transformDttm(bids["Bid"]["Time"])
                        + columnSeparator + transformDollar(bids["Bid"]["Amount"])
                        )
                        bidsID += 1 #Increments the bid ID

            #Adds bidders to user table
            if item["Bids"] is not None:
                for bids in item["Bids"]:
                    if "Country" in bids["Bid"]["Bidder"]:
                            if "Location" in bids["Bid"]["Bidder"]:
                                if bids["Bid"]["Bidder"]["UserID"] not in bidderIDs:
                                    bidderIDs.append(bids["Bid"]["Bidder"]["UserID"])
                                    bidder.append(
                                        bids["Bid"]["Bidder"]["UserID"] + columnSeparator + str(compare_loc.index(bids["Bid"]["Bidder"]["Location"])) + columnSeparator 
                                        + str(compare_country.index(bids["Bid"]["Bidder"]["Country"])) + columnSeparator + bids["Bid"]["Bidder"]["Rating"]
                                        )

            #Adds sellers to the user table
            if item["Seller"]["UserID"] not in sellerIDs:
                sellerIDs.append(item["Seller"]["UserID"])
                seller.append(
                    item["Seller"]["UserID"] + columnSeparator + str(compare_loc.index(item["Location"])) + columnSeparator 
                    + str(compare_country.index(item["Country"])) + columnSeparator + item["Seller"]["Rating"]
                )

            #Adds to category table
            for category in item["Category"]:
                if category not in compare_cate:
                    compare_cate.append(category)
                    categories.append(
                        str(categoryID) + columnSeparator + category
                    )
                    categoryID += 1
            
            #Adds to lineItem table
            for category in item["Category"]:
                lineItem.append(
                    str(compare_cate.index(category)) + columnSeparator + str(item["ItemID"])
                )

            

    #Writes to item.dat
    with open("item.dat", 'w') as f:
        for line in item_table:
            f.write(line + "\n")

    #Writes to bid.dat
    with open("bid.dat", 'w') as f:
        for line in bid:
            f.write(line + "\n")

    #Writes to seller.dat
    with open("seller.dat", 'w') as f:
        for line in seller:
            f.write(line + "\n")

    #Writes to bidder.dat
    with open("bidder.dat", 'w') as f:
        for line in bidder:
            f.write(line + "\n")

    #Writes to category.dat
    with open("category.dat", 'w') as f:
        for line in categories:
            f.write(line + "\n")

    #Writes to location.dat
    with open("location.dat", 'w') as f:
        for line in location:
            f.write(line + "\n")

    #Writes to country.dat
    with open("country.dat", 'w') as f:
        for line in country:
            f.write(line + "\n")

    #Writes to lineItem.dat
    with open("lineItem.dat", 'w') as f:
        for line in lineItem:
            f.write(line + "\n")

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
