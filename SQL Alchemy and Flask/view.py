from flask import Flask,redirect, url_for, request,render_template
import controller

app = Flask(__name__, template_folder='/home/sanojmv/bytedev/week7/SQLAlchemy/Flask_Prj Reloaded/webpages')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login',methods=['GET', 'POST'])
def login():
	if(request.method == 'POST'):
		uname = request.form["usr_user_name"]
		pword = request.form["usr_password"]
		uid, name, pw = controller.login(uname, pword)
		if(uid is None and pw is None):
			return "Wrong Username or Password!! Please check the username and password again.."
		else:
			if(pw != pword):
				pw = None
				return "Wrong Username or Password!! Please check the username and password again.."
			else:
				return render_template("homepage.html", name=name, uid=uid)

	return render_template("login.html")


@app.route('/register',methods=['GET', 'POST'])
def register():
	if(request.method== 'POST'):
		name = request.form["usr_name"]
		age = request.form["usr_age"]
		phone = request.form["usr_phone"]
		address = request.form["usr_address"]
		email = request.form["usr_email"]
		uname = request.form["usr_user_name"]
		pword = request.form["usr_password"]
		status = controller.registration(name, age, phone, address, email, uname, pword)
		if(status == "Added"):
			return render_template("index.html")
		else:
			return "Username already exists.."

	return render_template('register.html')

@app.route('/view_portfolio')
def view_portfolio():
	if(request.method == 'GET'):
		usr = request.args.get('uid')
		re, result, res = controller.view_portfolio(usr)
		cs = round(re[1],2)
		print(cs)
		return render_template("view_portfolio.html", re=re, result=result,res=res, cs=cs, reslen=len(res), resultlen=len(result))

	return render_template('homepage.html')

@app.route('/buy_sell')
def buy_sell():
	if(request.method == 'GET'):
		usr = request.args.get('uid')
		status = request.args.get('status')
		return render_template("buy_sell.html", uid=usr, status=status)
	return render_template("homepage.html")

@app.route('/Buy',methods=['GET', 'POST'])
def buy():
	if(request.method == 'POST'):
		uid = request.form['uid']
		sym = request.form['comp_sym']
		no = float(request.form['number'])
		total, last, option = controller.buy_shares(sym, no, uid)
		if(option is True):
			return "Purchase has been Successful!!"
		elif(option == "Connect"):
			return "Check your connection!!"
		else:
			return "The total shares cost exceeds your limit... Try buying less shares... Please check the portfolio to know the limit you have..!"
	return render_template('homepage.html')

@app.route('/Sell',methods=['GET', 'POST'])
def sell_shares():
	if(request.method == 'POST'):
		uid = request.form['uid']
		sym = request.form['comp_sym']
		no = float(request.form['number'])
		total, last, opt = controller.sell_shares(sym, no, uid)
		if(opt is True):
			return "Sale has been Successful!!"
		elif(opt == "Connect"):
			return "Please check your connection"
		else:
			return "Sale Failed!!"

	return render_template("homepage.html")

@app.route('/company')
def company():
	if(request.method == 'GET'):
		action = request.args.get('action')
		return render_template("company.html", action=action)
	return render_template("company.html")

@app.route('/search',methods=['GET', 'POST'])
def search():
	if(request.method == 'POST'):
		name = request.form['name']	
		data = controller.company_search(name)
		return render_template("result.html", data=data, action="Search")
	return render_template("index.html")

@app.route('/quote',methods=['GET', 'POST'])
def quote():
	if(request.method == 'POST'):
		sym = request.form['name']
		data = controller.get_quote(sym)
		return render_template("result.html", data=data, action="Quote")
	return render_template("index.html")



if __name__ == '__main__':
	print("Running Online Trade Depo..")
	app.run(debug = True)
