def read_inventory(filename):
    file = open(filename,"r")
    text=file.readlines()
    inventory={}
    for lines in text:
        line=lines.strip()
        comma=line.find(",")
        key=line[0:comma]
        comma2=line.find(",",comma+1,len(line))
        value1 = line[comma+1:comma2]
        value2=line[comma2+1:len(line)]
        value_list=[float(value1),int(value2)]
        inventory[key]=value_list
    return inventory

def display_inventory(inventory):
    print("INVENTORY:")
    for key,value in inventory.items():
        print(f"{key} ${value[0]} Qty:{value[1]}")
        
def add_item(inventory):
    item=input("Enter item: ")
    for key in inventory.keys():
        if item in inventory:
            print(f"{item} already exists")
            break
        else:
            cost=float(input("Enter cost: "))
            stock=int(input("Enter availability: "))
            value_list=[cost,stock]
            inventory[item] = value_list
            print(f"Added {item}")
            break

                  
def delete_item(inventory):
    item = input("Enter item: ")
    for key in inventory.keys():
        if item in inventory: 
            inventory.pop(item)
            print(f"Deleted {item}")
            break
        else:
            print(f"{item} not found")
            break 
        
def update_cost(inventory):
    item = input("Enter item: ") #prompt user for input
    for key in inventory.keys(): #.keys to loop through the keys of dictionary
        if item in inventory: #conditonal statement that checks if entered item is in the inventory
            percent=float(input("Enter percentage increase: "))  #asks by what percentage should the increase happens
            num_list=inventory[item] #gets the list of price and quantity
            new_price=(num_list[0]*(percent/100))+num_list[0] #updates price by increasing it by inputted percentage
            num_list[0]=round(new_price,2) #rounds the price to decimal places
            inventory[item]=num_list #updates the dictionary with the new price
            print(f"Updated {item}")
            break
        else:
            print(f"{item} not found")
            break
        
def above_avg_cost(inventory):
    total = 0
    i = 0
    for value in inventory.values(): #loops through the values of the dictionary
        total = total + value[0] #add the quantities to each other to calculate the average
        i=i+1 #updates number of items in the list
    average = total/i # calculates average
    print(f"Average Cost: {average}")
    print("ITEMS ABOVE AVERAGE COST:")
    for key,value2 in inventory.items(): #.items to go through keys and values
        if value2[0]>average: #checks if price is above average
            print(f"{key} - {value2[0]}") 
def main():
    filename=input("Enter the file: ")
    inventory=read_inventory(filename)
    i=True
    while i==True:
        print("\nMENU:")
        print("1. Display inventory\n2. Exit\n3. Add item\n4. Delete item\n5. Update cost\n6. Items above average cost")
        choice=(input("Enter choice: "))
        if choice=="1":
            display_inventory(inventory)
        elif choice == "2":
            i=False
            print("Goodbye")
        elif choice =="3":
            add_item(inventory)
        elif choice =="4":
            delete_item(inventory)
        elif choice=="5":
            update_cost(inventory)
        elif choice=="6":
            above_avg_cost(inventory)
        else:
            print("Invalid choice")
main()