import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { loginUser } from '../api';
import './Login.css';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const data = await loginUser(username, password);
      localStorage.setItem('access_token', data.access_token);
      navigate('/field-entry');
    } catch (err) {
      setError('Invalid credentials!');
    }
  };

  return (
    <div className="login-background">
      <div className="overlay" />
      <div className="login-container">
        <form className="login-form" onSubmit={handleLogin}>
          <h2>Welcome to Shri Govind</h2>
          <input
            type="text"
            name="username"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
          <input
            type="password"
            name="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          {error && <div style={{ color: 'red' }}>{error}</div>}
          <button type="submit">Login</button>
        </form>
        
      </div>
    </div>
  );

};

export default Login;
