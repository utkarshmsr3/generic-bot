from flask import Flask,redirect,url_for,request,session,render_template
from backend.businessOwnerDA import BusinessOwnerDA
from backend.customerDA import CustomerDA
from backend.qaDA import QaDA
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = "bot project"
socketio = SocketIO(app)

@app.route('/botdashboard')
def botdashboard():
    if "emailid" in session and "usertype" in session:
        if session["usertype"]=="businessowner":
            """
            session["bot"] = Bot(data with businessownerid)
            
            """
            return "Business Owner logged in"
        elif session["usertype"]=="customer":
            return "Customer logged in"
    return redirect(url_for('login'))

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    """
    if not bot in session:
        if emailid not in session
        bot = Bot()
    
    
    """
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

@app.route('/login',methods=['POST','GET'])
def login():
    """
    logic:
     if no logins in session :
         check login credintials
         if request method==post:
             if type == "businessowner":
               businessownerda.authenticate(emailid,password)
             else:
               customerDA.authenticate(emailid,password)
         else:
             redirect to login page
     else:
         to logged in page
    
    """
    if "emailid" in session:
        return redirect(url_for('botdashboard'))
    else:
        if request.method=='POST':
            userType = request.form['usertype']
            emailid = request.form['emailid']
            password = request.form['password']
            da = BusinessOwnerDA()   
            if userType == "customer":
                da = CustomerDA()
            res = da.authenticate(emailid,password)
            if res :
                session['emailid'] = emailid
                session['usertype']= userType
                return redirect(url_for('botdashboard'))
    return render_template("login.html",error="Invalid username.please log in again")


@app.route('/')
def index():
    return render_template('login.html',error='')



if __name__=="__main__":
    app.run(debug=True)