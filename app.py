import json
from flask import Flask, jsonify, render_template, request, Response


app = Flask(__name__)


with open('employees.json') as json_data:
    d = json.load(json_data)
    list_of_employees = []
    for data in d['employees']:
    	list_of_employees.append(data)


@app.route('/', methods =['GET'])
def home():
	return render_template("index.html")

@app.route('/employees', methods =['GET'])
def all_employees():
	return render_template("index.html",list_data=list_of_employees)

@app.route('/employees/<string:emp_id>', methods =['GET'])
def employee_by_id(emp_id):
	emp = [employees for employees in list_of_employees if employees['employeeId'] == emp_id]
	return render_template("index.html",list_data=emp)

if __name__ == '__main__':
	 app.run(host='0.0.0.0')