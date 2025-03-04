// Interface para informações de rastreamento
export interface TrackingInfo {
  stage: string;
  status: string;
  created_at: string;
}

// Interface para materiais
export interface Material {
  id: number;
  name: string;
  type: string;
  expiration_date: string;
  serial: string;
  stage: string;
  status: string;
}

// Interface para criação de rastreamento
export interface TrackingCreate {
  material_id: number;
  stage: string;
  status: string;
}