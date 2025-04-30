def create_city_grid(filename):
    file = open(filename, 'r');
    text=file.readlines()
    city_grid=[]
    grid=[]
    for lines in text:
        lines = lines.split()
        for i in range(len(lines)):
            lines[i] = int(lines[i])
        grid.append(lines)
    city_grid = grid[2:len(grid)]
    return city_grid  
    
def display_city_grid(city_grid):
    print('\nMetropolis Skyline Building Heights:')
    for row in city_grid:
        a_row=''
        for col in row:
            a_row = a_row+str(col)+(' '*3)
        print(' '*3+a_row)
        
def find_skyscrapers(city_grid, height_threshold):
    skyscrapers=[]
    for row in range(len(city_grid)):
        for col in range(len(city_grid[row])):
            if city_grid[row][col] >= height_threshold:
                location = city_grid[row][col]
                list1=[row,col,location]
                skyscrapers.append(list1)
    return(skyscrapers)

def create_classification_grid(city_grid):
    classified_grid=[]
    for row in range(len(city_grid)):
        total_row=0
        grid=[]
        total_row = sum(city_grid[row])
        average_row= total_row/len(city_grid[row])
        for col in range(len(city_grid[row])):       
            if int(average_row) == city_grid[row][col]:
                grid.append(0)
            elif int(average_row) > city_grid[row][col]:
                grid.append(-1)
            elif int(average_row) < city_grid[row][col]:
                grid.append(1)
        classified_grid.append(grid)
    return classified_grid
    
def extract_columns(classified_grid):
    i=0  #setting index to be 0
    columns=[] #intialsing outer layer of the 2d list
    while i != len(classified_grid): #while loop that continues as long as the index is not equal to the length of the columns
        col=[]    #intialising inner list of the 2d list
        for row in classified_grid: #for loop that goes through the rows
            col.append(row[i]) # appends inner list with values of the columns
        columns.append(col) #appending the outer list of the 2d list
        i+=1 #updating the index
    return columns

def is_same(columns):
    for row in range(len(columns)): #nested loop that goes through the rows
        same=True #initalisng the same variable to be boolean
        start_element= columns[row][0] #getting the first element of the 2d lists
        for col in range(len(columns[row])): #loop that goes through the columns
            if start_element != columns[row][col]: #checks if the elements are the same as the first element
                same = False
        return same
    
def main():
    filename=input("Enter filename: ")
    city_grid=create_city_grid(filename)
    display_city_grid(city_grid)
    height_threshold= int(input("\nEnter a height threshold: "))
    print(f"\nSkyscrapers taller than {height_threshold}m:")
    skyscrapers= find_skyscrapers(city_grid, height_threshold)
    for i in range(len(skyscrapers)): #for loop that goes through the outer list of the 2d list to print the output
        print(f"Row: {skyscrapers[i][0]}, Column: {skyscrapers[i][1]}, Height: {skyscrapers[i][2]}m")
    print("\nClassified Grid:")
    classified_grid=create_classification_grid(city_grid)
    print(classified_grid)
    print("\nColumns:")
    columns = extract_columns(classified_grid)
    print(columns)
    check = is_same(columns)
    if check == True:
        print("Has visual appeal.")
    else:
        print("Does not have visual appeal.")
    
main()