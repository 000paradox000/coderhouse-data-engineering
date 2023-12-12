from flask import Blueprint
from flask import jsonify

from app.models.customer import Customer

customers_bp = Blueprint('customers', __name__)


@customers_bp.route('/customers/')
def list_customers():
    customers = Customer.query.all()
    customers_list = []

    for customer in customers:
        customers_list.append({
            'customerid': customer.customerid,
            'name': customer.name,
            'occupation': customer.occupation,
            'email': customer.email,
            'company': customer.company,
            'phonenumber': customer.phonenumber,
            'age': customer.age,
        })

    return jsonify({
        "customers": customers_list,
    })
