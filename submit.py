from flask import Flask,request, render_template,session,redirect
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('C:\\Users\\hdoub\\OneDrive\\Documents\\programming\\barry-server\\submit\\cookie-clicker-d8a58-firebase-adminsdk-ehau2-5792e0a48d.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
app = Flask(__name__)
app.secret_key = 'jefdhysjs#[d[so]]'
@app.route('/password',methods = ['POST'])
def check():
    if request.form.get('pass') == 'admin223':
        session['admin'] = True
        return redirect('/control')
    return render_template('password.html')
@app.route('/complete')
def complete():
    if not session.get('admin'):
        return render_template('password.html')
    data = {
        "completed":True,
    }
    try:
        document = db.collection('jobs').document(request.args.get("key"))
        document.update(data)
    except Exception as e:
        return 'Error updating job.'
    return render_template('admin.html')
@app.route('/control')
def control():
    if not session.get('admin'):
        return render_template('password.html')
    return render_template('admin.html')
@app.route('/getall')
def get():
    if not session.get('admin'):
        return render_template('password.html')
    jobs_ref = db.collection('jobs')
    docs = jobs_ref.stream()
    data = []
    for doc in docs:
        dc = doc.to_dict()
        dc['id'] = doc.id
        data.append(dc)
    return data
@app.route('/')
def mk():
    return render_template('index.html')
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/control')
@app.route('/enter')
def sb():
    if not session.get('admin'):
        return render_template('password.html')
    data = {
        "completed":False,
        "description":request.args.get('desc'),
        "email":request.args.get('email')
    }
    try:
        document = db.collection('jobs').document()
        document.set(data)
    except Exception as e:
        return 'Error adding values to database.'
    return render_template('complete.html')
if __name__ == '__main__':
    app.run()