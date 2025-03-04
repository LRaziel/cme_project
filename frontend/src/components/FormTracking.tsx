import React, { useState, useEffect } from 'react';
import { getAllMaterials, createTracking } from '../services/api';
import { Material, TrackingCreate } from '../interfaces/interfaces';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCheck } from '@fortawesome/free-solid-svg-icons';

const FormTracking: React.FC = () => {
  const [materials, setMaterials] = useState<Material[]>([]);
  const [materialId, setMaterialId] = useState<number | ''>('');
  const [stage, setStage] = useState('');
  const [status, setStatus] = useState('');

  // Função para buscar todos os materiais
  useEffect(() => {
    const fetchMaterials = async () => {
      try {
        const data = await getAllMaterials();
        setMaterials(data);
      } catch (error) {
        console.error('Error fetching materials:', error);
      }
    };

    fetchMaterials();
  }, []);

  // Função para lidar com o envio do formulário
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const trackingData: TrackingCreate = {
        material_id: materialId as number,
        stage,
        status,
      };
      await createTracking(trackingData);
      setMaterialId('');
      setStage('');
      setStatus('');
    } catch (error) {
      console.error('Error creating tracking:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="row">
        <div className="col-md-3 mb-3">
          <label htmlFor="material" className="form-label">Material</label>
          <select
            className="form-control"
            id="material"
            value={materialId}
            onChange={(e) => setMaterialId(Number(e.target.value))}
            required
          >
            <option value="">Select Material</option>
            {materials.map((material) => (
              <option key={material.id} value={material.id}>
                {material.name}
              </option>
            ))}
          </select>
        </div>
        <div className="col-md-3 mb-3">
          <label htmlFor="stage" className="form-label">Stage</label>
          <select
            className="form-control"
            id="stage"
            value={stage}
            onChange={(e) => setStage(e.target.value)}
            required
          >
            <option value="">Select Stage</option>
            <option value="recebimento">Recebimento</option>
            <option value="lavagem">Lavagem</option>
            <option value="esterilizacao">Esterilização</option>
            <option value="distribuicao">Distribuição</option>
          </select>
        </div>
        <div className="col-md-3 mb-3">
          <label htmlFor="status" className="form-label">Status</label>
          <select
            className="form-control"
            id="status"
            value={status}
            onChange={(e) => setStatus(e.target.value)}
            required
          >
            <option value="">Select Status</option>
            <option value="pendente">Pendente</option>
            <option value="concluido">Concluído</option>
            <option value="falha">Falha</option>
          </select>
        </div>
        <div className="col-md-3 mb-3 d-flex align-items-end">
          <button type="submit" className="btn btn-primary w-25">
            <FontAwesomeIcon icon={faCheck} />
          </button>
        </div>
      </div>
    </form>
  );
};

export default FormTracking;