import model
import wrapper

def registration(name, age, phone, addr, email, uname, pword):
	res = model.check_username(uname)
	if (res is "Valid"):
		status = model.add_user(name, age, phone, addr, email, uname, pword)
		return status
	else:
		return "Exist"

def login(uname, pword):
	uid, name, pw = model.get_details(uname)
	if(uid is not None and pw is not None):
		return uid, name, pw
	else:
		return (None, None, None)

def view_portfolio(uid):
	re, result, res = model.portfolio(uid)
	return re, result, res


def company_search(comp):
	check = wrapper.Markit()
	data = check.company_search(comp)
	if(data is not None):
		return data
	else:
		return (False)

def get_quote(sym):
	quote = wrapper.Markit()
	data =  quote.get_quote(sym)
	if(data is not None):
		return data
	else:
		return (False)

def buy_shares(sym, no, uid):
	data = get_quote(sym)
	if(data == False):
		return (0, 0, "Connect")
	last_price = data["LastPrice"]
	total = no * last_price
	option = model.buy_shares(sym, no, last_price, total, uid)
	return(total, last_price, True)

def sell_shares(sym, no, uid):
	data = get_quote(sym)
	if(data == False):
		return (0, 0, "Connect")
	last_price = data["LastPrice"]
	total = no * last_price
	opt = model.sell_shares(sym, no, last_price, total, uid)
	return (total, last_price, True)
