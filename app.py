from flask import Flask,render_template,request,redirect,url_for,session
from dbconnector import connection

app = Flask(__name__)

app.secret_key='fasil'

#Opening first page
@app.route('/')
def loginhome():
    if 'sname' in session:
        return redirect(url_for('home'))
    else:
        return redirect(url_for('loginpage'))





# ===========================Routing=====================



#Opening Login page
@app.route('/loginpage')
def loginpage():
    return render_template('Login.html')

# Opening home page
@app.route('/home')
def home():
    return render_template('home.html')

# Opening registration page
@app.route('/reg')
def regis():
    return render_template('Registration.html')

# Opening Profile Page
@app.route('/profile')
def profile():
    return render_template('Profile.html')

# Opening Statement Page
@app.route('/statement')
def statements():
    return render_template('Statments.html')

# Opening Credit Page
@app.route('/credit')
def credit():
    return render_template('Credit.html')

# Opening Debt Page
@app.route('/debt')
def debt():
    return render_template('Debt.html')

# Opening Expenses Page
@app.route('/expenses')
def expenses():
    return render_template('Expenses.html')




# ================================================================







# ==========================Data Managing==========================


# Login process
@app.route('/login',methods=['post'])
def login():
    name=request.form['uname']
    pssword=request.form['pword']
    con,cur=connection()
    squery="select username,password from registration where username='"+name+"' and password='"+pssword+"';"
    cur.execute(squery)
    unamedata=cur.fetchone()
    if unamedata is None:
        return '''<script>alert("invalid user");window.location="/"</script>'''
    else:
        x=[i for i in unamedata]
        session['sname']=x[0]
        return redirect(url_for('loginhome'))

# Registration process
@app.route('/register',methods=['post'])
def registor():
    fname=request.form['fname']
    email=request.form['email']
    runame=request.form['runame']
    rpword=request.form['rpword']
    image=request.files['filename']

    image.save("C:/Users/febin/Documents/GitHub/SystemUser/static/pics/" + image.filename)
    path = "/static/pics/" + image.filename

    con, cur=connection()
    inquery="insert into registration (fullname,email,username,password,imgpath) values ('"+fname+"','"+email+"','"+runame+"','"+rpword+"','"+path+"');"
    myquery=cur.execute(inquery)
    con.commit()

    return redirect(url_for('loginhome'))

# Logout process
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('loginhome'))


# =====================================================================

if __name__ == '__main__':
    app.run(debug=True)
