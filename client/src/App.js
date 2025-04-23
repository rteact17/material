// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/Login';
import FieldEntry from './components/FieldEntry';
import AdminDashboard from './components/AdminDashboard';
import ProtectedRoute from './components/ProtectedRoute'; // Import ProtectedRoute

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        
        {/* Protect these routes */}
        <Route 
          path="/field-entry" 
          element={<ProtectedRoute element={<FieldEntry />} />} 
        />
        <Route 
          path="/admin-dashboard" 
          element={<ProtectedRoute element={<AdminDashboard />} />} 
        />
      </Routes>
    </Router>
  );
}

export default App;
