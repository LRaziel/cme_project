import axios from 'axios';
import { Material, TrackingCreate } from '../interfaces/interfaces';

const api = axios.create({
  baseURL: 'http://localhost:8080',
});

export const getAllUsers = async () => {
  try {
    const response = await api.get('/users');
    return response.data;
  } catch (error) {
    console.error('Error fetching users:', error);
    throw error;
  }
};

export const createUser = async (user: { name: string; email: string; password: string; role: string }) => {
  try {
    const response = await api.post('/users', user);
    return response.data;
  } catch (error) {
    console.error('Error creating user:', error);
    throw error;
  }
};

export const getAllMaterials = async () => {
  try {
    const response = await api.get('/materials');
    return response.data as Material[];
  } catch (error) {
    console.error('Error fetching materials:', error);
    throw error;
  }
};

export const getAllMaterialsWithTracking = async () => {
  try {
    const response = await api.get('/materials/with-tracking');
    return response.data as Material[];
  } catch (error) {
    console.error('Error fetching materials with tracking:', error);
    throw error;
  }
};

export const createMaterial = async (material: { name: string; type: string; expiration_date: string }) => {
  try {
    const response = await api.post('/materials', material);
    return response.data;
  } catch (error) {
    console.error('Error creating material:', error);
    throw error;
  }
};

export const createTracking = async (tracking: TrackingCreate) => {
  try {
    const response = await api.post('/tracking', tracking);
    return response.data;
  } catch (error) {
    console.error('Error creating tracking:', error);
    throw error;
  }
};

export default api;