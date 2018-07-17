"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""
    #adding a link to the html returned by the / route so that 
    #when you click the link, you’re taken to /hello.
    return "<!doctype html><html><a href='/hello'>Hello click me</a></html>"

# @app.route('/m')
# def start_here_2():
#     """Home page."""

#     return "<!doctype html><html>THINGSSSS STUFF BLAJ</html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>blahhhhhh</title>
      </head>
      <body>
        <h1>the hello page is being served!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"><br>
          Are you<input type="radio" name="compliment" value="pretty">pretty
          <input type="radio" name="compliment" value="intelligent">intelligent<br><br>
          Would you like a compliment?
          <input type="checkbox" name="sec_compl" value="yes">yes
          <input type="checkbox" name="sec_compl" value="no">no
          <br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""
    # get the compliment via request.args and display the compliment in the view.
    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
