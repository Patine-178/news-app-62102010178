from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields, reqparse
from flask_basicauth import BasicAuth
from werkzeug.middleware.proxy_fix import ProxyFix
import loan, installment

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api = Api(app, version='1.0', title='Loan API', description='Loan API')

ns_loan = api.namespace('loan', description='LOAN operations')
ns_loan_installment = api.namespace('loan/installment', description='INSTALLMENT operations')
ns_loan_minimum_income = api.namespace('loan/income', description='INCOME operations')

@ns_loan.route('/')
class LoanLists(Resource):
    @ns_loan.doc('list_loan')
    def get(self):
        loan_name = request.args.get('loanName')
        bank_name = request.args.get('bankName')
        if loan_name or bank_name:
            # ส่งชื่อสินเชื่อและชื่อธนาคาร
            if loan_name != None and bank_name != None:
                data = loan.read_loan_json()
                loan_list = []
                for loan_dict in data:
                    if loan_dict['loan_name'].lower() == loan_name.lower() and loan_dict['bank_name'].lower() == bank_name.lower():
                        loan_list.append(loan_dict)
                        return loan_list, 200
                return {"status": 500, "message":"Loan not found."}, 500
            # ส่งเฉพาะชื่อธนาคาร
            elif bank_name != None:
                data = loan.read_loan_json()
                loan_list = []
                for loan_dict in data:
                    if loan_dict['bank_name'].lower() == bank_name.lower():
                        loan_list.append(loan_dict)
                if len(loan_list) == 0:
                    return {"status": 500, "message":"Loan not found."}, 500
                return loan_list, 200
            # ส่งเฉพาะชื่อสินเชื่อ
            elif loan_name != None:
                data = loan.read_loan_json()
                loan_list = []
                for loan_dict in data:
                    if loan_dict['loan_name'].lower() == loan_name.lower():
                        loan_list.append(loan_dict)
                if len(loan_list) == 0:
                    return {"status": 500, "message":"Loan not found."}, 500
                return loan_list, 200
        # แสดงสินเชื่อทั้งหมด
        return loan.read_loan_json(), 200

@ns_loan_installment.route('/')
class LoanInstallment(Resource):
    @ns_loan_installment.doc('calculate_installment')
    def get(self):
        amount = request.args.get('amount')
        rate = request.args.get('rate')
        year = request.args.get('year')
        if amount and rate and year:
            installment_amount = installment.cal_installment(int(amount), int(rate), int(year))
            return {"installment_amount": round(installment_amount, 2)}, 200
        else:
            return {"status": 500, "message":"We can't calculate installment amount because parameters not complete."}, 500

@ns_loan_minimum_income.route('/')
class LoanIncome(Resource):
    @ns_loan_minimum_income.doc('search_loan_by_minimum_income')
    def get(self):
        min = request.args.get('minIncome')
        if min:
            data = loan.read_loan_json()
            loan_list = []
            for loan_dict in data:
                if loan_dict['minimum_income'] <= int(min):
                    loan_list.append({"loan_name":loan_dict['loan_name'], "bank_name":loan_dict['bank_name'], "minimum_income":loan_dict['minimum_income']})
            return sorted(loan_list, key=lambda loan: loan['minimum_income']), 200
        else:
            return {"status": 500, "message":"Loan not found."}, 500
