from flask import Flask, url_for, render_template, send_file, current_app
import os

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

@app.route("/download_resume")
def download_resume():
  '''
  download resume
  '''
  current_path = os.path.join(current_app.static_folder, 'images')
  path = os.path.join(current_path, 'toth_casey_resume.pdf')
  return send_file(path, as_attachment=True)


if __name__ == '__main__':
  app.run(port=5000)