import sqlite3
from datetime import datetime

def add_user(name, age, phone, addr, email, uname, pword):
	con = sqlite3.connect("./db/stocks")
	cur = con.cursor()
	insert_element = [name, 10000, 0, age, addr, phone, email, uname, pword, 'user']
	cur.execute("INSERT INTO Users (usr_name, usr_amount, usr_stocks, usr_age, usr_address, usr_phone, usr_email, usr_user_name, usr_password, usr_status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", insert_element)
	con.commit()
	print("The details have been entered!!")
	con.close()

def check_username(uname):
	con = sqlite3.connect("./db/stocks")
	cur = con.cursor()
	uname = [uname]
	cur.execute("SELECT * FROM Users WHERE usr_user_name=?",uname)
	re = cur.fetchone()
	return re

def avail_uname(uname):
	con = sqlite3.connect("./db/stocks")
	cur = con.cursor()
	cur.execute("SELECT usr_user_name FROM Users;")
	res = cur.fetchall()
	for u in range(len(res)):
		if(res[u][0] == uname):
			return True
	return False

def portfolio(uid):
	con = sqlite3.connect("./db/stocks")
	cur = con.cursor()
	u = [uid]
	cur.execute("SELECT * FROM Transactions WHERE trn_user_id = ?;", u)
	result = cur.fetchall()
	cur.execute("SELECT usr_name, usr_amount FROM Users WHERE usr_id = ?", u)
	re = cur.fetchone()
	cur.execute("SELECT * FROM Stocks WHERE stk_usr_id = ?", u)
	res = cur.fetchall()
	return re, result, res
	con.close()

def get_details(uname):
	con = sqlite3.connect("./db/stocks")
	cur = con.cursor()
	uname = [uname]
	option = avail_uname(uname)
	if(option):
		cur.execute("SELECT * FROM Users WHERE usr_user_name = ?;", uname)
		result = cur.fetchone()
		con.commit()
		con.close()
		return(result[0], result[9])
	else:
		return(None, None)

def buy_shares(sym, no, last, total, uid):
	con = sqlite3.connect("./db/stocks")
	cur = con.cursor()
	cur.execute("SELECT usr_amount FROM Users WHERE usr_id=?", [uid])
	result = cur.fetchone();
	if(total > result[0]):
		return(False)
	else:
		insert = [uid, sym, no, last, total, datetime.now(), "BUY"]
		cur.execute("INSERT INTO Transactions (trn_user_id, trn_symbol, trn_stocks, trn_stock_last_price, trn_total, trn_timestamp, trn_status) VALUES (?, ?, ?, ?, ?, ?, ?);", insert)
		cur.execute("UPDATE Users SET usr_amount=usr_amount-? WHERE usr_id = ?;", [total, uid])
		cur.execute("SELECT * FROM Stocks WHERE stk_usr_id =? AND stk_symbol = ?;", [uid, sym])
		res = cur.fetchone()
		if(res is None):
			cur.execute("INSERT INTO Stocks (stk_usr_id, stk_symbol, stk_stocks) VALUES (?, ?, ?)", [uid, sym, no])
		else:
			cur.execute("UPDATE Stocks SET stk_stocks = stk_stocks + ? WHERE stk_usr_id =? AND stk_symbol = ?;", [no, uid, sym])
		con.commit()
		con.close()
		return (True)
	
def sell_shares(sym, no, last, total, uid):
	con = sqlite3.connect("./db/stocks")
	cur = con.cursor()
	cur.execute("SELECT stk_symbol, stk_stocks FROM Stocks WHERE stk_usr_id = ? AND stk_symbol= ?", [uid, sym])
	stock_result = cur.fetchone()
	if(stock_result is None):
		return False
	elif(stock_result[1] >= no):
		insert = [uid, sym, no, last, total, datetime.now(), "SELL"]
		cur.execute("INSERT INTO Transactions (trn_user_id, trn_symbol, trn_stocks, trn_stock_last_price, trn_total, trn_timestamp, trn_status) VALUES (?, ?, ?, ?, ?, ?, ?);", insert)
		cur.execute("UPDATE Users SET usr_amount=usr_amount+? WHERE usr_id = ?;", [total, uid])
		cur.execute("UPDATE Stocks SET stk_stocks = stk_stocks - ? WHERE stk_usr_id = ? AND stk_symbol= ?", [no, uid, sym])
		con.commit()
		con.close()
		return True
	else:
		return False
	

