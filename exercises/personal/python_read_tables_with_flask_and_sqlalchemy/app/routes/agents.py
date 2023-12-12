from flask import Blueprint, render_template
from flask import jsonify

from app.models.agent import Agent

agents_bp = Blueprint('agents', __name__)


@agents_bp.route('/agents/')
def list_agents():
    agents = Agent.query.all()
    agents_list = []

    for agent in agents:
        agents_list.append({
            'agentid': agent.agentid,
            'name': agent.name,
        })

    return jsonify({
        "agents": agents_list,
    })
