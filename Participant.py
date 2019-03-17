import numpy as np 

class Participant:
	
	def __init__(self,ID):
		self.ID = ID

	def decide(self,chance):
		return (np.random.randint(chance) == 1)
