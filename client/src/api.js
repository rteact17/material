import axios from 'axios';

const API_URL = 'http://localhost:8000'; // Update this with your backend URL

const api = axios.create({
  baseURL: API_URL,
});


api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export const loginUser = async (username, password) => {
  const response = await api.post('/login', { username, password });
  return response.data;
};

export const submitEntry = async (entryData) => {
  const response = await api.post('/entry', entryData);
  return response.data;
};

export const submitPayment = async (paymentData) => {
  const response = await api.post('/payment', paymentData);
  return response.data;
};

export const getTax = async () => {
  const response = await api.get('/tax');
  return response.data;
};

export const getPayments = async (filters) => {
  const response = await api.get('/payments', { params: filters });
  return response.data;
};

export const getVehicleCustomers = async (cust,veh) => {
  const response = await api.get('/vehicleCustomer', { params: { cust, veh } });
  return response.data;
}
