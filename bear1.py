def read_inventory(filename):
    file = open(filename,"r") #open file in read mode
    text=file.readlines()#read line by line
    inventory={}#intialise dictionary
    for lines in text:
        line=lines.strip() #remove white spaces
        comma=line.find(",") #gets location of first comma
        key=line[0:comma] #identifying the key
        comma2=line.find(",",comma+1,len(line)) #location of seconf comma
        value1 = line[comma+1:comma2] 
        value2=line[comma2+1:len(line)] #identifying the quantity and price
        value_list=[float(value1),int(value2)] #placing quantity and price in list
        inventory[key]=value_list #defining dictionary
    return inventory

def display_inventory(inventory):
    print("INVENTORY:")
    for key,value in inventory.items(): #using .items to display the inventory
        print(f"{key} ${value[0]} Qty:{value[1]}")
        
def main():
    filename=input("Enter the file: ")
    inventory=read_inventory(filename)
    i=True
    while i==True: #using while loop to iterate the menu option
        print("\nMENU:")
        print("1. Display inventory")
        print("2. Exit")
        choice=(input("Enter choice: "))
        if choice=="1":
            display_inventory(inventory)
        elif choice =="2":
            i=False
            print("Goodbye")
        else:
            print("Invalid choice")
main()