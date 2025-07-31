# app/routes/department_routes.py
from flask import Blueprint, jsonify
from app.models import db, Department, Product

department_bp = Blueprint('departments', __name__, url_prefix='/api/departments')

@department_bp.route('', methods=['GET'])
def get_departments():
    departments = Department.query.all()
    result = []
    for dept in departments:
        result.append({
            'id': dept.id,
            'name': dept.name,
            'product_count': len(dept.products)
        })
    return jsonify({'departments': result}), 200

@department_bp.route('/<int:id>', methods=['GET'])
def get_department(id):
    dept = Department.query.get(id)
    if not dept:
        return jsonify({'error': 'Department not found'}), 404
    return jsonify({
        'id': dept.id,
        'name': dept.name
    }), 200

@department_bp.route('/<int:id>/products', methods=['GET'])
def get_department_products(id):
    dept = Department.query.get(id)
    if not dept:
        return jsonify({'error': 'Department not found'}), 404
    if not dept.products:
        return jsonify({'message': 'No products in this department'}), 200
    products_list = [{
        'id': p.id,
        'name': p.name,
        'price': p.price,
        'description': p.description
    } for p in dept.products]
    return jsonify({
        'department_id': dept.id,
        'department_name': dept.name,
        'products': products_list
    }), 200
