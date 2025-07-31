from app import create_app, db
from app.models import Product, Department

app = create_app()

with app.app_context():
    for product in Product.query.all():
        dept = Department.query.filter_by(name=product.department).first()
        if dept:
            product.department_id = dept.id
    db.session.commit()
    print("Products updated with department_id.")
