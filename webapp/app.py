from flask import Flask,render_template
application=Flask(__name__,template_folder='templates')

@application.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
   app.run()
