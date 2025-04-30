def store(filename): #store function creation with variable filename
    file=open(filename,'r'); #opening the file in read form
    text=file.readline() #reading the content of the text file
    comma=text.find(",") #using . find to find the position of the fist comma
    comma2=text.find(",",comma+1,len(text)); #finding the positon of the second comma
    list1=[]; #intialisng list
    list1.append(text[0:comma]); #appending the list with the first part of the text
    list1.append(text[comma+1:comma2]); #appending the list with the seconf part of the text
    list1.append(text[comma2+1:len(text)]); #appending the list with the third part of the text
    return list1; #returning the list with the elements of the text file separated

def main():
    filename=input("Enter filename: ");
    info = store(filename);
    height = info[0];
    growth_rate = info[1];
    raw_dna = info[2];
    print(f"HEIGHT: {height} GROWTH RATE: {growth_rate}\nRAW DNA: {raw_dna[:30]}...");
main();
    
    
    
    
    