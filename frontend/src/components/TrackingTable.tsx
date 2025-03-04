import React, { useState, useEffect } from 'react';
import { getAllMaterialsWithTracking } from '../services/api';
import { Material } from '../interfaces/interfaces';

const TrackingTable: React.FC = () => {
  const [materials, setMaterials] = useState<Material[]>([]);
  const [filteredMaterials, setFilteredMaterials] = useState<Material[]>([]);
  const [serialFilter, setSerialFilter] = useState('');
  const [statusFilter, setStatusFilter] = useState('');
  const [stageFilter, setStageFilter] = useState('');

  // Função para buscar todos os materiais com rastreamento
  useEffect(() => {
    const fetchMaterials = async () => {
      try {
        const data = await getAllMaterialsWithTracking();
        setMaterials(data);
        setFilteredMaterials(data);
      } catch (error) {
        console.error('Error fetching materials with tracking:', error);
      }
    };

    fetchMaterials();
  }, []);

  // Função para filtrar materiais
  useEffect(() => {
    filterMaterials();
  }, [serialFilter, statusFilter, stageFilter]);

  // Função para aplicar filtros nos materiais
  const filterMaterials = () => {
    let filtered = [...materials];

    if (serialFilter) {
      filtered = filtered.filter(material => material.serial.includes(serialFilter));
    }

    if (statusFilter) {
      filtered = filtered.filter(material => material.status === statusFilter);
    }

    if (stageFilter) {
      filtered = filtered.filter(material => material.stage === stageFilter);
    }

    setFilteredMaterials(filtered);
  };

  return (
    <div>
      <div className="row mb-3">
        <div className="col-md-4">
          <input
            type="text"
            className="form-control"
            placeholder="Filter by Serial"
            value={serialFilter}
            onChange={(e) => setSerialFilter(e.target.value)}
          />
        </div>
        <div className="col-md-4">
          <select
            className="form-control"
            value={statusFilter}
            onChange={(e) => setStatusFilter(e.target.value)}
          >
            <option value=""></option>
            <option value="pendente">Pendente</option>
            <option value="concluido">Concluído</option>
            <option value="falha">Falha</option>
          </select>
        </div>
        <div className="col-md-4">
          <select
            className="form-control"
            value={stageFilter}
            onChange={(e) => setStageFilter(e.target.value)}
          >
            <option value=""></option>
            <option value="recebimento">Recebimento</option>
            <option value="lavagem">Lavagem</option>
            <option value="esterilizacao">Esterilização</option>
            <option value="distribuicao">Distribuição</option>
          </select>
        </div>
      </div>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Expiration Date</th>
            <th>Serial</th>
            <th>Etapa</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {filteredMaterials.map((material, index) => (
            <tr key={`${material.id}-${index}`}>
              <td>{material.name}</td>
              <td>{material.type}</td>
              <td>{material.expiration_date}</td>
              <td>{material.serial}</td>
              <td>{material.stage}</td>
              <td>{material.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TrackingTable;