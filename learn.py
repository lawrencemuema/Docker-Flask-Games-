#python has alot of applications

#FLASK - library

from flask import Flask
#pip install flask

#instansiate flask: start 
myfirstwebapp = Flask('__name__')

#routes
@myfirstwebapp.route('/')
def test():
    return 'Hello World'

@myfirstwebapp.route('/azubi')
def test2():
    return 'Azubi'

# if __name__ == '__main__':

myfirstwebapp.run()