import random

class GuessPc:
    
    def __init__(self):
        self.guess = 0
        self.upper = int(input(f'Please enter an positive integer as upper bound of this guessing game: '))
        self.feedback = ''

    def guess(self):
        return random.randint(1, self.upper)
    
    def set_upper(self, new_upper):
        self.upper = new_upper
    
    def new_upper_num(self, num):
        if num % 2 == 0:
            self.set_upper(num/2)
        else:
            self.set_upper((num+1)/2)

    def play(self):
        while self.feedback != 'C':
            self.guess = self.guess()
            self.feedback = input(f'Is {self.guess} is Too High (H), Too Low(L), or Correct Answer(C)? ')
            if self.feedback == 'H':
                self.new_upper_num
                self.guess() # fix this because its randint from 1 to upper bound

                
