from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "Hello This is Osama"

#@app.route('/profile/osama')
#def profile():
 #   return "Hi My name Is Osama Khawaja"

@app.route('/profile/<name>')
def index2(name):
    return '<h1>Hello, %s!</h1>' % name

@app.route('/post/<int:id>')
def index3(id):
    return 'The ID is {}'.format(id)

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')