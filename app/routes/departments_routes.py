from flask import Blueprint, jsonify
from app.models import db, Department, Product

department_bp = Blueprint("department", __name__)

@department_bp.route("/api/departments")
def get_departments():
    departments = Department.query.all()
    result = []
    for dept in departments:
        result.append({
            "id": dept.id,
            "name": dept.name,
            "product_count": len(dept.products)
        })
    return jsonify({"departments": result})

@department_bp.route("/api/departments/<int:dept_id>")
def get_department(dept_id):
    dept = Department.query.get_or_404(dept_id)
    return jsonify({"id": dept.id, "name": dept.name})

@department_bp.route("/api/departments/<int:dept_id>/products")
def get_products_by_department(dept_id):
    dept = Department.query.get_or_404(dept_id)
    products = Product.query.filter_by(department_id=dept.id).all()
    product_data = [{"id": p.id, "name": p.name, "price": p.price} for p in products]
    return jsonify({"products": product_data})
