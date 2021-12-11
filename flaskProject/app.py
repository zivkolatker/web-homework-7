from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():  # put application's code here
    return 'Hello, welcome to main page!'

@app.route('/firstroute')
def hello_route():  # put application's code here
    return 'first route :)!'

@app.route('/secoundroute')
def hello_secound_route():  # put application's code here
    return redirect(url_for('page_unavailable'))

@app.route('/underconstracion')
def page_unavailable():  # put application's code here
    return 'the page is under constraction plase go back :( '

if __name__ == '__main__':
    app.run()
