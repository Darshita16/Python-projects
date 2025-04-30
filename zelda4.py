POSSIBLE_MOVES=["up","down","left","right"] #intialisng list of possible moves
def read_dungeon(filename):
    file = open(filename, "r")
    text=file.readlines()
    grid=[]
    dungeon=[]
    for lines in text:
        line=lines.strip()
        grid.append(line)
    for i in grid:
        list1=[]
        for j in i:
            list1.append(j)
        dungeon.append(list1)
    return dungeon

def display_dungeon(dungeon):
    for row in dungeon:
        a_row=''
        for col in row:
            char = col
            cols=get_emoji(char)
            a_row=a_row+cols+' '
        print(a_row.strip())
        
def find_link(dungeon):
    link=()
    for row in range(len(dungeon)):
        for col in range(len(dungeon[row])):
            if dungeon[row][col] == "L":
                link =link+(row,)
                link=link+(col,)
                return link

def get_emoji(char):
    if char == 'L':
        char=char.replace(char,'🧝')
    elif char == '#':
        char=char.replace(char, '🗿')
    elif char == '*':
        char=char.replace(char,'🌿')
    elif char == 'E':
        char=char.replace(char,'🚪')
    return char
    
def find_exit(dungeon):
    exit=()
    for row in range(len(dungeon)):
        for col in range(len(dungeon[row])):
            if dungeon[row][col]=='E':
                exit = exit+(row,)
                exit=exit+(col,)
                return exit
            
def get_valid_moves(dungeon,pos):
    valid_moves=[]
    valid_movesr=[]
    valid_movesc=[]
    rows=len(dungeon)
    cols=len(dungeon[0])
    x=pos[0]
    y=pos[1]
    for j in range(y-1,y+2):      
        for i in range(x-1, x+2):
            moves_row=()
            moves_col=()
            if i == x and j == y:
                continue
            if i<0 or i>+ rows or j<0 or j>= cols:
                continue       
            if j == y and dungeon[i][j] != "#":
                moves_col=moves_col+(i,)
                moves_col=moves_col+(j,)
                valid_movesc.append(moves_col)
            if i ==x and dungeon[i][j] != '#':
                moves_row=moves_row+(i,)
                moves_row=moves_row+(j,)
                valid_movesr.append(moves_row)
    valid_moves= valid_movesc+valid_movesr
    return valid_moves

def get_move(valid_moves,pos): 
    game= True
    while game == True: #while loop to run if the move isnt valid
        move=input("Enter move: ")
        move=move.strip() #removes white spaces
        move=move.lower()
        while move not in POSSIBLE_MOVES: #checks if input isnt in the list
            move=input("Invalid move. Enter move: ")
            move=move.strip()
            move=move.lower()             
        new_move=()
        move_list=[]
        if move == "up": #condiotnal statment that tells how the position changes based on the instructuions
            move_list=list(pos) #converts tuple to list for easier mutability
            move_list[0] = move_list[0]-1
            new_move=tuple(move_list)
        elif move =="down":
            move_list=list(pos)
            move_list[0] = move_list[0]+1
            new_move=tuple(move_list)
        elif move=="left":
            move_list=list(pos)
            move_list[1] = move_list[1]-1
            new_move=tuple(move_list)
        elif move=="right":
            move_list=list(pos)
            move_list[1] = move_list[1]+1
            new_move=tuple(move_list)
        for i in valid_moves: #checks if the move is in valid moves
            if new_move == i:
                game=False
                converted_move=new_move
                return converted_move
            else:
                x=1
        if x == 1:
            print("Invalid move. ",end="")
          
def move_link(dungeon, pos, converted_move):
    move_list = list(converted_move) #converst from tuple to list
    row = move_list[0] #gets row and col coordinates
    col = move_list[1]
    pos_list=list(pos)
    intial_row=pos_list[0]
    intial_col=pos_list[1]
    dungeon[intial_row][intial_col]="*" #swaps the link position with *
    dungeon[row][col]="L" #moves the link position
    return dungeon                 
                    
def main():
    filename=input("Enter filename: ")
    dungeon= read_dungeon(filename)
    display_dungeon(dungeon)
    pos=find_link(dungeon)
    exit_pos = find_exit(dungeon)
    valid_moves= get_valid_moves(dungeon,pos)
    end=False
    while end==False:
        converted_move=get_move(valid_moves,pos)
        move_link(dungeon,pos,converted_move)
        display_dungeon(dungeon)
        pos= find_link(dungeon)
        valid_moves=get_valid_moves(dungeon,pos)
        if pos == exit_pos:
            print("You have reached the exit!")
            end=True
main()