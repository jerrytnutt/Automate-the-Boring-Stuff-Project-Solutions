# Fantasy Game Inventory
# Create a display_inventory function that displays any possible “inventory”
# Create an add_to_Inventory function that appends items to players inventory

players_inventory = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby','ruby']

def display_inventory(dict):
    print("Inventory:")
    item_total = 0
    for keys,values in dict.items():
        print(dict[keys],keys)
        item_total += dict[keys]
    return "Total number of inventory items: " + str(item_total)


def add_to_Inventory(inventory, addedItems):
    for items in addedItems:
        if items in inventory:
            inventory[items] += 1
        else:
            inventory[items] = 1
    return display_inventory(inventory)

if __name__ == '__main__':
  print( add_to_Inventory(players_inventory,dragon_loot) )
  

