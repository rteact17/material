
import { useEffect, useState } from 'react';
import API from '../api';

const Dashboard = () => {
  const [msg, setMsg] = useState('');

  useEffect(() => {
    API.get('/dashboard').then(res => setMsg(res.data.message));
  }, []);

  return <h1>{msg}</h1>;
};

export default Dashboard;
