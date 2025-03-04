export interface TrackingInfo {
  stage: string;
  status: string;
  created_at: string;
}

export interface Material {
  id: number;
  name: string;
  type: string;
  expiration_date: string;
  serial: string;
  tracking_info: TrackingInfo[];
}

export interface TrackingCreate {
  material_id: number;
  stage: string;
  status: string;
}