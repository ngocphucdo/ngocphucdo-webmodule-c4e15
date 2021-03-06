from flask import Flask, render_template
from models.customer import Customer
from faker import Faker
from random import choice, randint
import mlab

mlab.connect()
fake = Faker()

app = Flask(__name__)

@app.route('/customer')
def index():
    return render_template('se.html')

@app.route('/male')
def male():
    all_customers = Customer.objects()
    male_customer = Customer.objects(gender = 1)[:10]
    return render_template('male_customer.html', male_customer=male_customer)


if __name__ == '__main__':
  app.run(debug=True)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
