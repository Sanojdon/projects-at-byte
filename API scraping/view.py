import controller

def register():
	name = input("Enter your name : ")
	age = int(input("Enter age : "))
	phone = int(input("Enter phone number : "))
	addr = input("Enter address : ")
	email = input("Enter your email : ")
	uname = input("Enter username : ")
	pword = input("Enter your password : ")
	controller.registration(name, age, phone, addr, email, uname, pword)

def login():
	username = input("Enter the username : ")
	password = input("Enter the password : ")
	uid, pw = controller.login(username, password)
	if(uid is None and pw is None):
		print("Wrong Username or Password!! Please check the username and password again..")
		return (None, None)
	else:
		if(pw != password):
			pw = None
		return uid, pw

def view_portfolio():
	uid, pw = login()
	if(pw is None):
		start()
	re, result, res = controller.view_portfolio(uid)
	print("Name : ", re[0])
	print("Available Balance : " , re[1])
	print("Symbol----Number of shares----Last Price-----Total Cost------Date and time of Transaction--------Status")
	for i in range(len(result)):
		print(" ",result[i][2], "--------", result[i][3], "-------------", result[i][4], "--------", result[i][5], "--------", result[i][6],"--------",result[i][7])
	print("The stocks that you currently have are : ")
	for i in range(len(res)):
		print("Company Symbol : ", res[i][2])
		print("Number of shares : ", res[i][3])
		print("--------------------------------------------------------------------")

def company_search():
	company = input("Enter the company that you want to search : ")
	data = controller.company_search(company)
	print("Name of the company : ", data[0]['Name'])
	print("Symbol of the company : ", data[0]['Symbol'])
	print("Exchange of the company : ", data[0]['Exchange'])
	print("\n\n\n\n")

def get_quote():
	sym = input("Enter the symbol of the company to view quote : ")
	data = controller.get_quote(sym)
	for k,v in data.items():
		print(k, " : ", v)
	print("\n\n\n\n")

def buy_shares():
	uid, pword = login()
	if(pword is None):
		start()
	sym = input("Enter the required company symbol : ")
	no = int(input("Enter the number of shares you want to buy : "))
	total, last, option = controller.buy_shares(sym, no, uid)
	if(option is True):
		print("Last Price of the share : ", last)
		print("You have bought",no, "shares for the price of $",total)
		print("\n\n\n\n")
	elif(option == "Connect"):
		print("Please check your connection")
	else:
		print("The total shares cost exceeds your limit... Try buying less shares... Please check the portfolio to know the limit you have..!")

def sell_shares():
	uid, pword = login()
	if(pword is None):
		start()
	sym = input("Enter the required company symbol : ")
	no = int(input("Enter the number of shares you intend to sell : "))
	total, last, opt = controller.sell_shares(sym, no, uid)
	if(opt is True):
		print("Last Price of the share : ", last)
		print("You have sold",no, "shares for the price of $",total)
		print("\n\n\n\n")
	elif(opt == "Connect"):
		print("Please check your connection")
	else:
		print(opt)
		print("Sale Failed..")
		print("Please check if you have the shares of the above mentioned company")
		print("Please check the number of shares you are planning to sell..")
		print("\n\n\n\n")

def start():
	opt = "3"
	while(opt != 8):
		print("Choose your option : ")
		print("1. Register User")
		print("2. Login")
		print("3. View Portfolio")
		print("4. Buy Shares")
		print("5. Sell Shares")
		print("6. Company Search")
		print("7. Get Quote")
		print("8. Exit")
		opt = input("Enter your option - ")
		if(opt == "1"):
			register()
		elif(opt == "2"):
			uid, pw = login()
			if(uid is not None and pw is not None):
				if(pw is not None):
					print("Successfully Logged In..")
					print("\n\n\n\n")
				else:
					print("Wrong Password or Username!! Please Login again!!")
					print("\n\n\n\n")
				
		elif(opt == "3"):
			view_portfolio()
		elif(opt == "4"):
			buy_shares()
		elif(opt == "5"):
			sell_shares()
		elif(opt == "6"):
			company_search()
		elif(opt == "7"):
			get_quote()
		elif(opt == "8"):
			break
		else:
			print("Wrong Input")

start()
