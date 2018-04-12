class Player():
    # name = []
    # score = []

    # __init__ => Behave like constructor
    # Will be called automatically whenever object is created
    def __init__(self):
        self.name = []
        self.score = []

    def show_details(self,p_name,p_score):
        self.name.append(p_name)
        self.score.append(p_score)
        print(self.name)
        print(self.score)

p_1 = Player()
p_1.show_details('Sachin',100)

p_2 = Player()
p_2.show_details('Dhoni',50)