from flask import Flask
app = Flask(__name__)


# @app.route('/')
# def index():
#     return redirect(url_for('BMI'))


@app.route('/bmi/<weight>/<height>')
def BMI(weight, height):
    BMI = float(weight) / (float(height) ** 2)

    if BMI < 16:
        stm = 'severely underweight'
    elif BMI < 18.5:
        stm = 'underweight'
    elif BMI < 25:
        stm = 'Normal'
    elif BMI < 30:
        stm = 'Overweight'
    else:
        stm = 'Obese'
    Info = {
        'weight': weight,
        'height': height,
        'BMI': str(BMI)[:5],
        'Statement': stm
        }
    return ("BMI " + str(BMI)[:5] + ': ' + stm)
    # return render_template('BMIinfo.html', Info = Info)


if __name__ == '__main__':
  app.run(debug=True)
