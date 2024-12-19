from flask import Blueprint, request, jsonify
from models import Member
from database import db

member_routes = Blueprint('member_routes', __name__)

@member_routes.route('/', methods=['GET'])
def get_members():
    members = Member.query.all()
    return jsonify([{"id": member.id, "name": member.name, "email": member.email, "active": member.active} for member in members])

@member_routes.route('/', methods=['POST'])
def add_member():
    data = request.json
    member = Member(name=data['name'], email=data['email'], active=data.get('active', True))
    db.session.add(member)
    db.session.commit()
    return jsonify({"message": "Member added successfully"}), 201

@member_routes.route('/<int:id>', methods=['PUT'])
def update_member(id):
    data = request.json
    member = Member.query.get(id)
    if not member:
        return jsonify({"message": "Member not found"}), 404
    member.name = data.get('name', member.name)
    member.email = data.get('email', member.email)
    member.active = data.get('active', member.active)
    db.session.commit()
    return jsonify({"message": "Member updated successfully"})

@member_routes.route('/<int:id>', methods=['DELETE'])
def delete_member(id):
    member = Member.query.get(id)
    if not member:
        return jsonify({"message": "Member not found"}), 404
    db.session.delete(member)
    db.session.commit()
    return jsonify({"message": "Member deleted successfully"})