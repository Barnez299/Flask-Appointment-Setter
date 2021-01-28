from flask import Flask



app = Flask(__name__)

# view all appointments
@app.route('/appointments/')
def appointment_list():
    return 'Listing of all appointments we have.'



# create an appointment
@app.route('/appointments/create/', methods=['GET', 'POST'])
def appointment_create():
    return 'Form to create a new appointment.'



# view single appointment
@app.route('/appointments/<int:appointment_id>/')
def appointment_detail(appointment_id):
    return 'Detail of appointment #{}.'.format(appointment_id)


# edit an appointment
@app.route('/appointments/<int:appointment_id>/edit/', methods=['GET', 'POST'])
def appointment_edit(appointment_id):
    return 'Form to edit appointment #.'.format(appointment_id)




# delete an appointment
@app.route('/appointments/<int:appointment_id>/delete/', methods=['DELETE'])
def appointment_delete(appointment_id):
    raise NotImplementedError('DELETE')




if __name__=='__main__':
    app.run(debug=True)
