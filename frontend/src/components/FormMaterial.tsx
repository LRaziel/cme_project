import React, { useState } from 'react';
import { createMaterial } from '../services/api';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCheck } from '@fortawesome/free-solid-svg-icons';

const FormMaterial: React.FC = () => {
  const [name, setName] = useState('');
  const [type, setType] = useState('');
  const [expirationDate, setExpirationDate] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await createMaterial({ name, type, expiration_date: expirationDate });
      setName('');
      setType('');
      setExpirationDate('');
    } catch (error) {
      console.error('Error creating material:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="mb-3">
        <label htmlFor="name" className="form-label">Name</label>
        <input
          type="text"
          className="form-control"
          id="name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
      </div>
      <div className="row">
        <div className="col-md-6 mb-3">
          <label htmlFor="type" className="form-label">Type</label>
          <select
            className="form-control"
            id="type"
            value={type}
            onChange={(e) => setType(e.target.value)}
            required
          >
            <option value=""></option>
            <option value="Críticos">Críticos</option>
            <option value="Semicríticos">Semicríticos</option>
            <option value="Não críticos">Não críticos</option>
            <option value="Materiais de Uso Único">Materiais de Uso Único</option>
            <option value="Materiais de Consumo e Almoxarifado">Materiais de Consumo e Almoxarifado</option>
          </select>
        </div>
        <div className="col-md-6 mb-3">
          <label htmlFor="expirationDate" className="form-label">Expiration Date</label>
          <input
            type="date"
            className="form-control"
            id="expirationDate"
            value={expirationDate}
            onChange={(e) => setExpirationDate(e.target.value)}
            required
          />
        </div>
      </div>
      <button type="submit" className="btn btn-primary w-25">
        <FontAwesomeIcon icon={faCheck} />
      </button>
    </form>
  );
};

export default FormMaterial;