import React, { useState, useEffect } from 'react';
import { getTax, getPayments } from '../api';

const AdminDashboard = () => {
  const [taxRate, setTaxRate] = useState('');
  const [payments, setPayments] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const taxData = await getTax();
      setTaxRate(taxData.gst_rate);

      const paymentData = await getPayments({});
      setPayments(paymentData);
    }
    fetchData();
  }, []);

  return (
    <div>
      <h2>Admin Dashboard</h2>
      <div>
        <h3>Current Tax Rate: {taxRate}</h3>
        <h3>Payments</h3>
        <table>
          <thead>
            <tr>
              <th>Customer Name</th>
              <th>Payment Mode</th>
              <th>Amount</th>
            </tr>
          </thead>
          <tbody>
            {payments.map((payment) => (
              <tr key={payment.id}>
                <td>{payment.customer_name}</td>
                <td>{payment.mode}</td>
                <td>{payment.amount}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default AdminDashboard;
