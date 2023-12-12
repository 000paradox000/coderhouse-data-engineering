from flask import Blueprint, render_template
from flask import jsonify

from app.models.call import Call

calls_bp = Blueprint('calls', __name__)


@calls_bp.route('/calls/')
def list_calls():
    calls = Call.query.all()
    calls_list = []

    for call in calls:
        calls_list.append({
            'callid': call.callid,
            'agentid': call.agentid,
            'customerid': call.customerid,
            'pickedup': call.pickedup,
            'duration': call.duration,
            'productsold': call.productsold,
        })

    return jsonify({
        "calls": calls_list,
    })
