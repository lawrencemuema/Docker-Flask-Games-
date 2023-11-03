#python has alot of applications
#Flask, render_template, request, redirect, url_for, jsonify  are all libraries
#libraries are collections of code that are already written for you to use
#libraries are also called modules or packages

#Flask is a web framework, that helps you create web applications
#render_template is a function that renders a template (html file)
#request is a function that gets data from the user (form data)
#redirect is a function that redirects the user to another route (url)
#url_for is a function that gets the url for a certain route (path)
#jsonify is a function that converts a dictionary to json format (json is a format for sending data over the internet)


from flask import Flask #importing the flask library
#pip install flask

#instansiate flask: start 
myfirstwebapp = Flask('__name__') #name of the app

#routes, are the paths that the user can take to get to a certain page
@myfirstwebapp.route('/')
def test():
    return 'Hello World' #returning a string to the user

@myfirstwebapp.route('/azubi')
def test2():
    return 'Azubi'

@myfirstwebapp.route('/<name>') 
#<name> is a variable that can be used in the function
# sample url http://x/myname, will return Hello myname
def test3(name):
    return f'Hello {name}'


#run the app

#__main__ is the name of the file that is being run
# __ is called dunder, double underscore. used for special functions
# __name__ is the name of the file that is being run

if __name__ == '__main__':
    myfirstwebapp.run() #run the app