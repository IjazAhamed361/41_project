import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import ProductCard from "./ProductCard";

function DepartmentPage() {
  const { id } = useParams();
  const [department, setDepartment] = useState(null);
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch(`/api/departments/${id}`)
      .then((res) => res.json())
      .then((data) => setDepartment(data));

    fetch(`/api/departments/${id}/products`)
      .then((res) => res.json())
      .then((data) => setProducts(data.products || []));
  }, [id]);

  if (!department) return <p>Loading...</p>;

  return (
    <div>
      <h2>{department.name} ({products.length} products)</h2>
      <Link to="/">← Back to All Products</Link>
      <div className="product-grid">
        {products.map((p) => (
          <ProductCard key={p.id} product={p} />
        ))}
      </div>
    </div>
  );
}

export default DepartmentPage;
