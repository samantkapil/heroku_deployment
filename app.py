from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load(r'dib_79.pkl')
print('[INFO] model loaded')

@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/predict' , methods = ['post'])
def predict():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    output = model.predict([[int(preg),int(plas),int(pres),int(skin),int(test),int(mass),int(pedi),int(age)]])
    if output[0]==1:
        ans = 'dibatic'
    else:
        ans = 'not dibatic'
    return render_template('predict.html', predict= f'the person is {ans}' )



@app.route('/hello')    
def hello():
    return 'reach hello url page'

@app.route('/welcome')    
def welcome():
    return render_template('welcome.html')

@app.route('/contact')    
def contact():
    return render_template('contact.html')  

@app.route('/blog')    
def blog():
    return render_template('blog.html')  

@app.route('/gallary')    
def gallery():
    return render_template('gallary.html')  

if __name__ == '__main__'
    app.run(debug=True)
