import React, { useState } from 'react';
import './FieldEntry.css';
import { getVehicleCustomers, submitEntry } from '../api';

const FieldEntry = () => {
  const [form, setForm] = useState({
    vehicle: '', customer: '', date: '', bulk: 'N', material: '',
    quantity: '', unit: 'Cubic Feet', memo: ''
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleBlur = async (e) => {
    let data;
    if (e.target.name === 'customer') {
      data = await getVehicleCustomers(e.target.value, '');
      if (data?.vehicle_number) {
        setForm({ ...form, vehicle: data.vehicle_number });
      }
    } else if (e.target.name === 'vehicle') {
      data = await getVehicleCustomers('', e.target.value);
      if (data) {
        setForm({ ...form, customer: data.customer_name });
      }
    }


  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    await submitEntry(form)
    alert('Entry submitted');
  };

  return (
    <div className="entry-container">
      <h2>Field Entry</h2>
      <form className="entry-form" onSubmit={handleSubmit}>
        <label>
          Vehicle Number
          <input name="vehicle" onChange={handleChange} value={form?.vehicle} onBlur={handleBlur} required />
        </label>

        <label>
          Customer Name
          <input name="customer" onChange={handleChange} value={form?.customer} onBlur={handleBlur} required />
        </label>

        <label>
          Date & Time
          <input name="date" type="datetime-local" onChange={handleChange} required />
        </label>

        <label>
          Bulk / Retail
          <select name="bulk" onChange={handleChange}>
            <option value="N">Retail</option>
            <option value="Y">Bulk</option>
          </select>
        </label>

        <label>
          Material
          <input name="material" onChange={handleChange} required />
        </label>

        <label>
          Quantity
          <input name="quantity" type="number" onChange={handleChange} required />
        </label>

        <label>
          Measurement Unit
          <select name="unit" onChange={handleChange}>
            <option value="Cubic Feet">Cubic Feet</option>
            <option value="Metric Ton">Metric Ton</option>
          </select>
        </label>

        <label>
          Delivery Memo Number
          <input name="memo" onChange={handleChange} />
        </label>

        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default FieldEntry;
