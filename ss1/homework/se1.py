from flask import Flask, render_template
app = Flask(__name__)


@app.route('/matherfucker/<int:height>/<int:mass>')
def matherfucker(height, mass):
    BMI = round(mass / ((height**2)/10000))

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

    return render_template('bmi.html', st = st, BMI = BMI, height = height, mass = mass )

if __name__ == '__main__':
  app.run(debug=True)
