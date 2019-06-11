from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def films():
  '''
  return the films page
  '''
  return render_template('films.html')

@app.route("/images")
def images():
  '''
  returns the images page
  '''
  return render_template('images.html')

@app.route("/about")
def about():
  '''
  return the about page
  '''
  return render_template('about.html')

@app.route("/connect")
def connect():
  '''
  return the connect page
  '''
  return render_template('connect.html')


if __name__ == '__main__':
  app.run()