from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return "Hello C4e15"

@app.route('/sum/<int:num1>/<int:num2>')
def sum(num1,num2):
    return str(num1 + num2)

@app.route('/html')
def heading():
    return "<h1>whatever</h1>"

@app.route('/blog')
def blog():
    posts = [
        {"content" : "Ngoc Phuc Do",
        "author" : "abc"},
        {"content" : "Black Panther",
        "author" : "xyz"},
        {"content" : "Captain America",
        "author" : "qwe"}
    ]
    article_name = "My Blog"
    return render_template('blog.html', article_title = article_name,
    posts = posts)





if __name__ == '__main__':
  app.run(debug=True)
