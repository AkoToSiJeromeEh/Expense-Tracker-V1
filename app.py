from flask import Flask, render_template , request , session , url_for , redirect
from flask_session import Session
import mysql.connector 




app = Flask(__name__)
app.secret_key = '1111112324214124'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


connection = mysql.connector.connect(

        host = 'localhost',
        user = 'root',
        password = '',
        database = 'expense'
)

def insert_data( expenseid , category , expenseamounnt , date) :
    cursor = connection.cursor()
    cursor.execute('INSERT INTO expense (expenseid , category, price , date) VALUES (%s, %s, %s, %s)', (expenseid, category, expenseamounnt, date))
    connection.commit()
    
    
def insert_reminder(reminderid , title , content , price , date) :
    cursor = connection.cursor()
    cursor.execute('INSERT INTO reminder (reminderid , title , content , price , date) VALUES (%s, %s, %s, %s , %s)' , (reminderid, title, content, price, date))
    connection.commit()

    
def fetch_expenses() : 
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM expense')
    expenses = cursor.fetchall()
    connection.commit()
    return expenses

def fetch_reminders() : 
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM reminder')
    reminder = cursor.fetchall()
    connection.commit()
    return reminder

def sum_expenses() :
    cursor = connection.cursor()
    cursor.execute('SELECT price FROM expense ')
    rows = cursor.fetchall()
    connection.commit()
    total = sum(row[0] for row in rows)
    
    return total

def high_expense():
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM expense WHERE price >= 500 ORDER BY price DESC')
    highexpenses = cursor.fetchall()
    connection.commit()
    return highexpenses

def new_expense():
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM expense ORDER BY date ASC')
    newexpense = cursor.fetchall()
    connection.commit()
    return newexpense


    
@app.route('/delete_reminder/<reminderid>')
def delete_reminder(reminderid):
    cursor = connection.cursor()
    data = (reminderid,)  
    cursor.execute('DELETE FROM reminder WHERE reminderid=%s', data)
    connection.commit()
    return  redirect(url_for('listexpense'))


@app.route('/delete_expenses/<expenseid>')
def delete_expense(expenseid):
    cursor = connection.cursor()
    data = (expenseid,)
    cursor.execute('DELETE FROM expense WHERE expenseid=%s' , data)
    connection.commit()
    return redirect(url_for('listexpense'))

@app.route('/update_reminder/<reminderid>', methods=['GET'])
def update_reminder(reminderid):
    cursor = connection.cursor()
    data = (reminderid,)
    cursor.execute('SELECT * FROM reminder WHERE reminderid=%s', data)
    result = cursor.fetchone() 

    if result:
        sucessremind = 'Update Now'
        return render_template('updatelist.html', reminder=result , sucessremind=sucessremind)

        
@app.route('/update_reminder', methods=['POST'])
def updatereminder():
    if request.method == 'POST':
        reminderid = request.form['reminderid']
        title = request.form['title']
        content = request.form['content']
        price = request.form['price']
        date = request.form['date']
        cursor = connection.cursor()
        cursor.execute('UPDATE reminder SET title = %s, content = %s, price = %s, date = %s WHERE reminderid = %s', (title, content, price, date, reminderid))
        connection.commit()  
        return redirect(url_for('listexpense'))       
     
    
    
@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == "POST":
        expenses =  fetch_expenses()
        sumexpenses = sum_expenses()
        username = request.form['username']
        password = request.form['password']
        loginError = 'Incorrect username or password'
        mycursor = connection.cursor()
        sql = "SELECT * FROM users WHERE username=%s AND password=%s"
        data = (username, password)
        mycursor.execute(sql, data)
        myresult = mycursor.fetchone() 

        if myresult:
            username = myresult[0] 
            monthlyIncome = myresult[2]  
            session['username'] = username
            session['monthlyIncome'] = monthlyIncome
            return render_template('/home.html', username=username, monthlyIncome=monthlyIncome , expenses=expenses , sumexpenses = sumexpenses)

        else:
            return render_template('login.html', loginError=loginError)
    else:
        return render_template('login.html')



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
     username = session.get('username')
     monthlyIncome = session.get('monthlyIncome')
     expenses =  fetch_expenses()
     sumexpenses = sum_expenses()
     if username and monthlyIncome :
         return render_template('home.html' , username=username , monthlyIncome=monthlyIncome , expenses=expenses , sumexpenses=sumexpenses )
     else :
         return render_template('login.html')
     
    
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))



@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/cardbalance')
def cardbalance():
    monthlyIncome = session['monthlyIncome'] 
    sumexpenses = sum_expenses()
    highexpenses = high_expense()
    newexpenses = new_expense()
    if monthlyIncome :
        return render_template('cardbalance.html' , monthlyIncome=monthlyIncome , sumexpenses=sumexpenses , highexpenses=highexpenses , newexpenses=newexpenses)
    else :
         return render_template('login.html')


@app.route('/addexpense')
def addexpense():
    return render_template('addexpense.html')



@app.route('/updatelist')
def updatelist():
    return render_template('updatelist.html')


@app.route('/addreminder' , methods=['POST'])
def addreminder():
    
    if session.get('username') == session['username']:
        if(request.method == 'POST') :
            successremind = 'Success Inserted'
            reminderid = request.form['reminderid']
            title = request.form['title']
            content = request.form['content']
            price = request.form['price']
            date = request.form['date']
            insert_reminder(reminderid , title , content , price , date)
            return render_template('addexpense.html', successremind=successremind)

@app.route('/insertexpenses', methods=['POST'])
def insertexpenses():
    if session.get('username') == session['username']:
        if request.method == 'POST' :
            sucessInsert = 'Success Inserted'
            expenseid = request.form['expenseid']
            category = request.form['category']
            expenseamount = request.form['expenseamount']  
            date = request.form['date']
            insert_data(expenseid, category, expenseamount, date)
            return render_template('addexpense.html' , sucessInsert=sucessInsert)
    else :
              return render_template('login.html')


@app.route('/listexpense')
def listexpense():
    expenses = fetch_expenses()
    reminders = fetch_reminders()
    summaryOfExpense =  sum_expenses()
    return render_template('listexpense.html' , expenses=expenses , reminders=reminders , summaryOfExpense=summaryOfExpense)


if __name__ == '__main__':
    app.run(debug=True)