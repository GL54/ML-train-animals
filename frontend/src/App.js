import logo from "./logo.svg";
import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import MainPage from "./components/MainPage";
import Test from "./components/Test";

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/test" element={<MainPage />} />
          <Route path="/" element={<Test />} />
        </Routes>
      </Router>
    </>
  );
}
export default App;
