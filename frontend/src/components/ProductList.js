import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function DepartmentList() {
  const [departments, setDepartments] = useState([]);

  useEffect(() => {
    fetch("/api/departments")
      .then((res) => res.json())
      .then((data) => setDepartments(data.departments));
  }, []);

  return (
    <div>
      <h3>Departments</h3>
      <ul>
        {departments.map((dept) => (
          <li key={dept.id}>
            <Link to={`/departments/${dept.id}`}>{dept.name} ({dept.product_count})</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default DepartmentList;
