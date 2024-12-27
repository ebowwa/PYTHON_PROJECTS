from flask import Flask, jsonify, request
from fetch import fetch_institution_agreements, fetch_agreements_categories, fetch_agreements, fetch_articulation_agreements

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/api/institution_agreements/<int:institution_id>' , methods=['GET'])
def institution_agreements(institution_id):
    data = fetch_institution_agreements(institution_id)
    return jsonify(data)

@app.route('/api/agreements_categories' , methods=['GET'])
def agreements_categories():
    receiving_institution_id = request.args.get('receivingInstitutionId')
    sending_institution_id = request.args.get('sendingInstitutionId')
    academic_year_id = request.args.get('academicYearId')
    data = fetch_agreements_categories(receiving_institution_id, sending_institution_id, academic_year_id)
    return jsonify(data)

@app.route('/api/agreements' , methods=['GET'])
def agreements():
    receiving_institution_id = request.args.get('receivingInstitutionId')
    sending_institution_id = request.args.get('sendingInstitutionId')
    academic_year_id = request.args.get('academicYearId')
    category_code = request.args.get('categoryCode')
    data = fetch_agreements(receiving_institution_id, sending_institution_id, academic_year_id, category_code)
    return jsonify(data)

@app.route('/api/articulation_agreements/<path:key>' , methods=['GET'])
def articulation_agreements(key):
    data = fetch_articulation_agreements(key)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=False)
