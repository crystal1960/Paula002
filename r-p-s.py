import random

class rpsGame:
    
    def __init__(self):
        
        self.gameOptions = ["r", "p", "s"]
    
    def computer(self):
        
        computerPlay = random.choice(self.gameOptions)
        return computerPlay
    
    def playGame(self):
        
        print("Rock Paper Scissors")
        print("Game Started")
        print("R - Rock | P - Paper | S - Scissors")
        print("\n")
        print("RULES")
        print("Rock beats Scissors")
        print("Scissors beats Paper")
        print("Paper beats Rock")
        
        while True:
            the_computer = self.computer()

            gamePlay = input("Pick your choice.. R, P or S: ").lower()

            if gamePlay in self.gameOptions:
                if gamePlay == "r" and the_computer == "s":
                    print("Player (Rock) : CPU (Scissors)")
                    print("The winner is Player")
                    break

                elif gamePlay == "r" and the_computer == "s":
                    print("Player (Rock) : CPU (Paper)")
                    print("The winner is CPU")
                    break

                elif gamePlay == "r" and the_computer == "r":
                    print("Player (Rock) : CPU (Rock)")
                    print("It is a tie")

                elif gamePlay == "p" and the_computer == "s":
                    print("Player (Paper) : CPU (Scissors)")
                    print("The winner is CPU")
                    break

                elif gamePlay == "p" and the_computer == "p":
                    print("Player (Paper) : CPU (Paper)")
                    print("It is a tie")

                elif gamePlay == "p" and the_computer == "r":
                    print("Player (Paper) : CPU (Rock)")
                    print("The winner is Player")
                    break

                elif gamePlay == "s" and the_computer == "s":
                    print("Player (Scissors) : CPU (Scissors)")
                    print("It is a tie")

                elif gamePlay == "s" and the_computer == "p":
                    print("Player (Scissors) : CPU (Paper)")
                    print("The winner is Player")
                    break

                elif gamePlay == "s" and the_computer == "r":
                    print("Player (Scissors) : CPU (Rock)")
                    print("The winner is CPU")
                    break
            
            else:
                print("Invalid input. Please try again.")
                print("\n")

game = rpsGame()
game.playGame()
