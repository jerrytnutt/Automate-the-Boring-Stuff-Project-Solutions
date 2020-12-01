# Fantasy Game Inventory
# Write a function named displayInventory() that displays any possible “inventory”
# Write a function named addToInventory(inventory, addedItems)
# inventory is a dict representing the player’s inventory and addedItems is additional inventory 
# inventory will receive the new items from addedItems dict 

playersInventory = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby','ruby']

def displayInventory(dict):
    print("Inventory:")
    item_total = 0
    for keys,values in dict.items():
        print(dict[keys],keys)
        item_total += dict[keys]
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, addedItems):
    for items in addedItems:
        if items in inventory:
            inventory[items] += 1
        else:
            inventory[items] = 1
addToInventory(playersInventory,dragonLoot)
displayInventory(playersInventory)

