from flask import *
from models.service import Service
import mlab

mlab.connect()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    services = Service.objects()
    return render_template('admin.html', services = services)

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects().with_id(service_id)
    if service_to_delete is None:
        return "Not found"

    service_to_delete.delete()
    return redirect(url_for('admin'))

@app.route('/new-service', methods = ['GET', 'POST'])
def create():
    if request.method == "GET":
        return render_template('new-service.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        height =form['height']
        gender = form['gender']
        measure1 = int(form['measure1'])
        measure2 = int(form['measure2'])
        measure3 = int(form['measure3'])
        set_measure = [measure1, measure2, measure3]
        new_service = Service(name=name,
                            yob = yob,
                            phone = phone,
                            gender = gender,
                            address = "Ha Noi",
                            status = False,
                            height = height,
                            description= "Xinh gai, de thuong, ca tinh",
                            image = image_link,
                            measurements = measurements)
        new_service.save()
        return redirect(url_for('admin'))

@app.route('/update/<service_id>', methods = ['GET', 'POST'])
def update(service_id):
    service_to_update = Service.objects().with_id(service_id)
    if request.method == "GET":
        return render_template('update.html', service_to_update = service_to_update)
    elif request.method == "POST":
        form = request.form
        measure1 = int(form['measure1'])
        measure2 = int(form['measure2'])
        measure3 = int(form['measure3'])
        set_measure = [measure1, measure2, measure3]
        service_to_update.update(set__name = form['name'],
                                set__yob = form['yob'],
                                set__height = form['height'],
                                set__address = form['address'],
                                set__phone = form['phone'],
                                set__status = 'True' if form['status'] == True else 'False' , #tuong tu nhu gender nen de mac dinh luon
                                set__gender = 'Male' if form['gender'] == 1 else 'Female',
                                set__description = form['description'],
                                set__measurements = set_measure)
    return render_template('update.html')

if __name__ == '__main__':
  app.run(debug=True)
