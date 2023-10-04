import requests
import json
import concurrent
from concurrent.futures import ThreadPoolExecutor

root = "https://api.hypixel.net/skyblock/auctions?page="


# grabs the JSON data from the Hypixel API and returns it as a python dictionary
def getPageData(currentPage):
    pageContent = requests.get(f"{root}{str(currentPage)}").text
    return json.loads(pageContent)


# checks if the auction is a good flip
def checkAuction(auctionToCheck):
    hotPotatoBooked = "§e(+20)" in auctionToCheck["item_lore"] and "§e(+10)" not in auctionToCheck["item_lore"]
    fumingPotatoBooked = "§e(+30)" in auctionToCheck["item_lore"]
    recombobulated = "§k" in auctionToCheck["item_lore"]
    if "Fishing Speed" in auctionToCheck["item_lore"] and "Attribute Shard" in auctionToCheck["item_name"]:
        return True
    else:
        return False


# get the total number of pages from
firstPageData = getPageData("0")
totalPages = firstPageData["totalPages"]
print(totalPages)
# create list to contain all auction data
auctions = []

# iterates through every page and adds the auction data to the auction data list
with ThreadPoolExecutor(max_workers=totalPages) as executor:
    future1 = {executor.submit(getPageData, page)
               for page in range(0, totalPages)}
    for future in concurrent.futures.as_completed(future1):
        fullPageData = future.result()
        auctions.extend(fullPageData["auctions"])


for auction in auctions:
    binAuction = auction["bin"]

    if checkAuction(auction):
        print(f"item: {auction['item_name']}   /viewauction {auction['uuid']}   cost = {auction['starting_bid']}")
print("done")
