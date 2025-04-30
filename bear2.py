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
    item=input("Enter item: ") #prompt user for input
    for key in inventory.keys(): #.keys to loop through the keys of dictionary
        if item in inventory: #conditonal statement that checks if entered item is in the inventory
            print(f"{item} already exists") 
            break
        else:
            cost=float(input("Enter cost: ")) #prompt to enter cost
            stock=int(input("Enter availability: ")) #prompt to enter quantity
            value_list=[cost,stock] #creates list
            inventory[item] = value_list #adds list in dictionary
            print(f"Added {item}")
            break

                  
def delete_item(inventory):
    item = input("Enter item: ") #prompt user for input
    for key in inventory.keys(): #.keys to loop through the keys of dictionary
        if item in inventory:  #conditonal statement that checks if entered item is in the inventory
            inventory.pop(item) #.pop to remove the specificed key and its coressponding value
            print(f"Deleted {item}")
            break
        else:
            print(f"{item} not found")
            break       
            
def main():
    filename=input("Enter the file: ")
    inventory=read_inventory(filename)
    i=True
    while i==True:
        print("\nMENU:")
        print("1. Display inventory\n2. Exit\n3 .Add item\n4. Delete item")
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
        else:
            print("Invalid choice")
main()