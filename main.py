import random

class GuessPc:
    
    def __init__(self):
        self.upper = int(input(f'Please enter an positive integer as upper bound of this guessing game: '))
        self.lower = 1
        self.guess = 0
        self.feedback = ''
    
    def guess_num(self, l, u):
        self.guess = int((l+u)/2)

    def get_guess(self):
        return self.guess
    
    def set_upper(self, num):
        self.upper = num
    
    def set_lower(self, num):
        self.lower = num

    def play(self):
        
        self.guess_num(self.lower, self.upper)

        while self.feedback != 'C':

            print(f"guess: {self.guess}, up:{self.upper}, low:{self.lower}")
            
            self.feedback = input(f'Is {self.get_guess()} is Too High (H), Too Low(L), or Correct Answer(C)?: ')

            if self.upper - self.lower <= 1:
                print("I think I got the right answer! Don't cheat!")
                self.feedback = input(f'Is {self.get_guess()} is Too High (H), Too Low(L), or Correct Answer(C)?: ')
            
            old_guess = self.get_guess()
            
            if self.feedback == 'H':
                self.set_upper(old_guess)
                self.guess_num(self.lower, self.upper)
                

            elif self.feedback == 'L':
                self.set_lower(old_guess)
                self.guess_num(self.lower, self.upper)
            
            elif self.feedback != 'C':
                print(f'Invalid Value, Please Enter again!')
                continue

        print(f'I am a computer! This is way too easy for me! Try harder!')
    

if __name__ == '__main__':
    
    game1 = GuessPc()
    print(game1.get_guess())
    game1.play()




                
