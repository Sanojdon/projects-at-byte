import markit


def add_user(name, age, phone, addr, email, uname, pword):
	v = markit.add_user(name, age, phone, addr, email, uname, pword)
	if(v == True):
		return "Added"

def check_username(uname):
	v = markit.get_username(uname)
	if not v:
		return "Valid"
	else:
		return "Exists"
	
def portfolio(uid):
	v,w,x = markit.portfolio(uid)
	return v, w, x
	

def get_details(uname):
	v = markit.get_details(uname)
	return(v.usr_id, v.usr_name, v.usr_password)

def buy_shares(sym, no, last, total, uid):
	v = markit.buy_shares(sym, no, last, total, uid)
	return(v)


def sell_shares(sym, no, last, total, uid):
	v = markit.sell_shares(sym, no, last, total, uid)
	return(v)