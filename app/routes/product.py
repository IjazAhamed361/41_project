from flask import Blueprint, jsonify
from app.models import Product

products_bp = Blueprint('products', __name__)

@products_bp.route('/products')
def get_products():
    products = Product.query.all()
    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "department": p.department.name if p.department else None
        }
        for p in products
    ])
