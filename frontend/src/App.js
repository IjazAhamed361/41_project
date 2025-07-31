import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import DepartmentPage from "./components/DepartmentPage";
import Home from "./pages/Home";
import NotFound from "./pages/NotFound";
import DepartmentList from "./components/DepartmentList";

function App() {
  return (
    <Router>
      <div className="layout">
        <DepartmentList />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/departments/:id" element={<DepartmentPage />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
