from flask import Flask, request, jsonify, make_response, abort
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lilekov.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app=app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=20), nullable=False)
    surname = db.Column(db.String(length=20), nullable=False)
    phone = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Users %r>' % self.id

    def get_user_info(self):
        return {
            'id': self.id,
            'user_name': self.name,
            'user_surname': self.surname,
            'user_phone': self.phone
        }


@app.route('/users', methods=['POST'])
def add_user():
    if not request.json:
        abort(400)

    new_user = Users(name=request.json['name'],
                     surname=request.json['surname'], phone=request.json['phone'])
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'result': True}), 201
    except:
        abort(400)


@app.route('/users', methods=['GET'])
def all_users():
    users = [user.get_user_info() for user in Users.query.all()]
    return jsonify({'users': users})


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    find_id = Users.query.get_or_404(user_id)

    try:
        db.session.delete(find_id)
        db.session.commit()
        return jsonify({'result': True})
    except:
        abort(400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


if __name__ == '__main__':
    if not os.path.exists('lilekov.db'):
        db.create_all()

    app.run(debug=True, host='0.0.0.0',  port='80')
