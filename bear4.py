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
    item = input("Enter item: ")
    for key in inventory.keys():
        if item in inventory: 
            percent=float(input("Enter percentage increase: "))
            num_list=inventory[item]
            new_price=(num_list[0]*(percent/100))+num_list[0]
            num_list[0]=round(new_price,2)
            inventory[item]=num_list
            print(f"Updated {item}")
            break
        else:
            print(f"{item} not found")
            break  
        
def above_avg_cost(inventory):
    total = 0
    i = 0
    for value in inventory.values():
        total = total + value[0]
        i=i+1
    average = total/i
    print(f"Average Cost: {average}")
    print("ITEMS ABOVE AVERAGE COST:")
    for key,value2 in inventory.items():
        if value2[0]>average:
            print(f"{key} - {value2[0]}")
            
def sell_item(inventory):
    item=input("Enter item: ") #prompt user for input
    for key in inventory.keys(): #.keys to loop through the keys of dictionary
        if item in inventory: #conditonal statment that checks if input is in the dictionary
            value = inventory[item] #gets values list
            quantity=int(input("Enter quantity: ")) #gets integer quantity to be sold
            if value[1] == 0: # checks if theres 0 qunatity avaialable
                print(f"{item} not available")
            elif quantity<value[1]: #if the quantity sold is less than stock
                original_quantity=value[1]
                difference = value[1] - quantity #calculate how much left
                value[1]=difference
                inventory[item] = value
                cost = value[0] * quantity
                print(f"{quantity} out of {original_quantity} units sold for ${cost:.2f}, with {difference} units remaining")
            elif value[1] <= quantity: #if quantity sold is greater than stock
                sell = value[1]
                cost=sell*value[0]
                value[1] = 0
                inventory[item] = value
                print(f"{sell} out of {sell} units sold for ${cost:.2f}, with 0 units remaining")
            break
        else:
            print(f"{item} not found")
            break             

def out_of_stock(inventory):
    print("OUT OF STOCK:")
    i=False
    for key,value in inventory.items(): #.itms loops through the keys and values
        if value[1] == 0: #checks if quantity is 0
            print(f"{key}")
            i=True
    if i == False:
        print("All items are in stock")
            
                
def main():
    filename=input("Enter the file: ")
    inventory=read_inventory(filename)
    i=True
    while i==True:
        print("\nMENU:")
        print("1. Display inventory\n2. Exit\n3. Add item\n4. Delete item\n5. Update cost\n6. Items above average cost\n7. Sell item\n8. Out of stock")
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
        elif choice=="7":
            sell_item(inventory)
        elif choice =="8":
            out_of_stock(inventory)
        else:
            print("Invalid choice")
main()