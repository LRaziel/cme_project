import React from 'react';
import FormUser from './FormUser';
import FormMaterial from './FormMaterial';
import FormTracking from './FormTracking';
import TrackingTable from './TrackingTable';

const Home: React.FC = () => {
  const mainsGrid: React.CSSProperties = {
    display: 'grid',
    gridTemplateColumns: 'repeat(5, 1fr)',
    gridTemplateRows: 'repeat(5, 1fr)',
    gap: '8px',
  };

  const divStyle: React.CSSProperties = {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    border: '1px solid black',
  };

  const title: React.CSSProperties = {
    ...divStyle,
    gridColumn: 'span 5 / span 5',
  };

  const content: React.CSSProperties = {
    ...divStyle,
    gridColumn: 'span 5 / span 5',
    gridRow: 'span 4 / span 4',
    gridRowStart: 2,
  };

  const formTracking: React.CSSProperties = {
    margin: '2%',
  }

  return (
    <div style={mainsGrid}>
      <div style={title}><h1>TESTE - SISTEMA CME</h1></div>
      <div style={content}>
        <div className="container">
          <div className="row justify-content-center">
            <div className="accordion col-6" id="groupFormUSer">
              <div className="accordion-item">
                <h2 className="accordion-header" id="headingOne">
                  <button className="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                    Cadastro de Usuários
                  </button>
                </h2>
                <div id="collapseOne" className="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
                  <div className="accordion-body">
                    <FormUser />
                  </div>
                </div>
              </div>
            </div>

            <div className="accordion col-6" id="groupFormMaterial">
              <div className="accordion-item">
                <h2 className="accordion-header" id="headingTwo">
                  <button className="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                    Cadastro de Materiais
                  </button>
                </h2>
                <div id="collapseTwo" className="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#accordionExample">
                  <div className="accordion-body">
                    <FormMaterial />
                  </div>
                </div>
              </div>
            </div>

            <div className="col" style={formTracking}>
              <FormTracking />
            </div>

            <div>
              <TrackingTable />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;