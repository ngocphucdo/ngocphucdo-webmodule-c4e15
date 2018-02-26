from flask import Flask, render_template
app = Flask(__name__)


@app.route('/BMI/<int:height>/<int:mass>')
def index(height,mass):
    BMI = float(mass) / (float(height) ** 2)  

    if BMI < 16 :
        st = "Severely underweight"
    elif 16 < BMI < 18.5:
        st = "Underweight"
    elif 18.5 < BMI < 25:
        st = "Normal"
    elif 25 < BMI < 30:
        st = "Overweight"
    else:
        st = "Obese"

    return (BMI, st)

if __name__ == '__main__':
  app.run(debug=True)
