// src/components/ProtectedRoute.js
import React from 'react';
import { Navigate } from 'react-router-dom';

const ProtectedRoute = ({ element }) => {
  const token = localStorage.getItem('access_token');
  
  // If no token, redirect to login page
  if (!token) {
    return <Navigate to="/" />;
  }

  // If token exists, allow access to the protected route
  return element;
};

export default ProtectedRoute;
