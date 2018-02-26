from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<user_name>')
def user(user_name):
    profiles = {

        "Phuc":
        {
        'name': 'ngoc phuc do',
        'gender': 'male',
        'hobbies':'sleep, basketball',
        'age':21
        },
        "Bach":
        {
        'name':'do ngoc bach',
        'gender':'male',
        'hobbies':'nutsquizer',
        'age': 19
        },
        "Minh":
        {
        'name':'tran nguyet minh',
        'gender':'female',
        'hobbies':'makeup',
        'age':25
        }
    }
    if  user_name in profiles:
        user_info = profiles[user_name]
        return render_template('user.html', user_info = user_info)
    else:
        return ("not found")

if __name__ == '__main__':
  app.run(debug=True)
