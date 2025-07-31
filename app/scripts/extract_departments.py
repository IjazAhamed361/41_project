from app import create_app, db
from app.models import Product, Department

app = create_app()

with app.app_context():
    unique_depts = set(product.department for product in Product.query.all())
    for name in unique_depts:
        if name:
            existing = Department.query.filter_by(name=name).first()
            if not existing:
                dept = Department(name=name)
                db.session.add(dept)
    db.session.commit()
    print("Departments inserted.")
