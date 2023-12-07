from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://coderhouse:coderhouse@db_postgres:5432/coderhouse'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Agent(db.Model):
    __tablename__ = 'agents'
    agentid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


@app.route('/')
def index():
    agents = Agent.query.filter(
        or_(
            func.lower(Agent.name).startswith('m'),
            func.lower(Agent.name).endswith('o')
        )
    ).all()
    agents_list = [{'agentid': agent.agentid, 'name': agent.name}
                   for agent in agents]

    return jsonify(agents_list)


@app.route('/agents')
def agents():
    query = Agent.query
    print(str(query))
    agents = query.all()
    agents_list = [{'agentid': agent.agentid, 'name': agent.name}
                   for agent in agents]

    return jsonify(agents_list)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', port=5000, debug=True)
