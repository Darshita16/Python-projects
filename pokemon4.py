import random
class pokemon:
    def __init__ (self,name,attack,defense,max_health,current_health):
        self.name=name
        self.attack=attack
        self.defense=defense
        self.max_health=max_health
        self.current_health=current_health
        
    def __str__(self):
        return f'{self.name} (health: {self.current_health}/{self.max_health})'
    
    def lose_health(self,amount):
        if amount < self.current_health:
            self.current_health=self.current_health-amount
        elif amount >= self.current_health:
            self.current_health=0
            
    def is_alive(self):
        if self.current_health>0:
            return True
        else:
            return False
    
    def revive(self):
        self.current_health = self.max_health
        print(f"{self.name} has been revived!")
    
    def getname(self):
        return self.name
    
    def getattack(self):
        return self.attack
    
    def getmax_health(self):
        return self.max_health
    def getcurrent_health(self):
        return self.current_health
    def attempt_attack(self,other):
        luck=random.choice([0.7,0.8,0.9,1.0,1.1,1.2,1.3]) #picks random number
        damage=round(luck*self.attack) #calculates damage
        if damage > other.defense: #checks if damage greater than defense
            difference=damage-other.defense
            other.lose_health(difference) #updates current health value
            attack=True
        elif damage <= other.defense:
            attack=False
        return_list=[damage,attack]
        return return_list
        
def read_pokemon_from_file(filename):
    object_list=[]
    file=open(filename, "r", encoding="utf-8")
    lines=file.readlines()[1:]
    for i in lines:
        i.strip()
        i=i.split("|")
        name= i[0]
        attack = int(i[1])
        defense=int(i[2])
        health=int(i[3])
        objects=pokemon(name,attack,defense,health,health)
        object_list.append(objects)
    return object_list
            
        
def main():
        filename=input("Enter filename: ")
        seed_val=input('Enter seed value: ')
        random.seed(seed_val)
        pokemon1 = None
        pokemon2 = None
        # NOW IMPLEMENT STEPS b-f (BELOW) HERE
        object_list=read_pokemon_from_file(filename)
        while pokemon1==pokemon2:
            pokemon1 = random.choice(object_list) #picks random pokemons
            pokemon2=random.choice(object_list)
        print(f"\nWelcome {pokemon1} and {pokemon2}!")
        rounds=1 #intialisng rounds
        win1=False #bollean to know which pokemon won
        win2=False
        while pokemon1.is_alive() and pokemon2.is_alive() and rounds <=10:
            print(f"\nRound {rounds} begins! {pokemon1} and {pokemon2}!")
            damage=pokemon.attempt_attack(pokemon1,pokemon2) #gets damage afge first pokemon attacks
            print(f"{pokemon1.getname()} attacks {pokemon2.getname()} for {damage[0]} damage!")
            if damage[1] == False: #conditoanl statment that checks effect of attack
                print("Attack is blocked!")
                fight=True
            else:
                print(f"Attack is successful! {pokemon2.getname()} has {pokemon2.getcurrent_health()} health remaining!")
                alive=pokemon.is_alive(pokemon2) #checks if pokemon is alive or dead
                if alive == True:
                    fight= True    
                else:
                    if random.choice([True, False]) == True:
                        pokemon.revive(pokemon2)
                        fight = True
                    else:
                        fight = False
                        win1= True
                        break
            if fight == True:
                damage2=pokemon.attempt_attack(pokemon2,pokemon1)
                print(f"{pokemon2.getname()} attacks {pokemon1.getname()} for {damage2[0]} damage!") 
                if damage2[1] == False:
                    print("Attack is blocked!")
                    rounds=rounds+1
                else:
                    print(f"Attack is successful! {pokemon1.getname()} has {pokemon1.getcurrent_health()} health remaining!")
                    alive2=pokemon.is_alive(pokemon1)
                    if alive2 ==True:
                        rounds=rounds+1
                    else:
                        if random.choice([True, False]) == True:
                            pokemon.revive(pokemon1)
                            rounds=rounds+1
                        else:
                            win2=True
                            break                   
        if win1 == True:
            print(f"\n{pokemon1.getname()} (health: {pokemon1.getcurrent_health()}/{pokemon1.getmax_health()}) has won in {rounds} rounds!")
        elif win2 == True:
            print(f"\n{pokemon2.getname()} (health: {pokemon2.getcurrent_health()}/{pokemon2.getmax_health()}) has won in {rounds} rounds!")
        else:
            print(f"\nIt's a tie between {pokemon1.getname()} (health: ({pokemon1.getcurrent_health()}/{pokemon1.getmax_health()}) and {pokemon2.getname()} (health: ({pokemon2.getcurrent_health()}/{pokemon2.getmax_health()})!")
                
main()
 