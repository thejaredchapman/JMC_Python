class BankAccount: #Parent class

	#Initialize Account
	def __init__(self, initial_balance):
		self.__balance = initial_balance

	#Get Balance
	def get_balance(self):
		return self.__balance

	#Deposit Money
	def deposit (self,amount):
		self.__balance += amount

	#Withdraw Money
	def withdraw (self,amount):
		self.__balance -= amount

class SavingsAccount(BankAccount): #Child class from BankAccount

	#Inherit attribute and start account
	def __init__(self,initial_balance):
		BankAccount.__init__(self, initial_balance)

	#Transfer function of bank account
	def transfer(self, account_obj, amount):
		if amount <= account_obj.get_balance():
			account_obj.withdraw(amount)
			self.deposit(amount)
			print('Transferred $', amount, "into your savings account, \n")
		else:
			print("Inefficient Funds!!!\n")

class CheckingAccount(BankAccount): # child class of Bank Account

	def __init__(self, initial_balance):
		BankAccount.__init__(self, initial_balance)

		
def main():
	


#Run program

main()
