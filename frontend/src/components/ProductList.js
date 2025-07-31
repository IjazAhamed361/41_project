import React, { useEffect, useState } from 'react';
import { getProducts } from '../api';
import { Link } from 'react-router-dom';

const ProductList = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    getProducts().then(data => setProducts(data));
  }, []);

  return (
    <div>
      <h2>Product List</h2>
      <ul className="list-group">
        {products.map(product => (
          <li className="list-group-item" key={product.id}>
            <Link to={`/product/${product.id}`}>
              {product.name} - ₹{product.price}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProductList;
