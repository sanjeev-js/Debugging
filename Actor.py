class Actor:
	actor_number=0
	raised_amount=1.05
	def __init__(self, fname, lname, raised_pay):
		self.fname=fname
		self.lname=lname
		self.raised_pay=raised_pay
		self.actor_number+=1
	def fullname(self):
		return '{} {}'.format(self.fname,self.lname)
	def raised(self):
		self.raised_pay = int(self.raised_pay * self.raised_amount)
		return self.raised_pay

act_1 = Actor("Rahul","yadav",50000)
act_2 = Actor("kedar", "jadhav", 60000)
Actor.raised_amount=1.04
act_1.raised_amount=1.04
print (Actor.__dict__)