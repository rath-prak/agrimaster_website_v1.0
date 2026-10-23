// PLACEHOLDER availability data. These are NOT real distributors.
// Replace with real data (e.g. fetched from Strapi) before launch.
export type BrandName = 'Master' | 'Super' | 'Echo' | 'Vital' | 'Golden' | 'Diamond';

export interface AvailabilitySpot {
  id: string;
  province: string;
  lat: number;
  lng: number;
  label: string;
  brands: BrandName[];
  kind?: 'distributor' | 'feedmill';
  placeholder: boolean;
}

export const FEEDMILL: AvailabilitySpot = {
  id: 'feedmill', province: 'Kandal', lat: 11.43, lng: 104.82,
  label: 'Agri Master feedmill', brands: ['Master', 'Super', 'Echo', 'Vital', 'Golden', 'Diamond'],
  kind: 'feedmill', placeholder: true,
};

const P = 'Distributor (placeholder)';
export const availability: AvailabilitySpot[] = [
  { id: 'pp', province: 'Phnom Penh', lat: 11.56, lng: 104.92, label: P, brands: ['Master', 'Super', 'Golden', 'Diamond'], placeholder: true },
  { id: 'btb', province: 'Battambang', lat: 13.1, lng: 103.2, label: P, brands: ['Master', 'Echo', 'Golden'], placeholder: true },
  { id: 'sr', province: 'Siem Reap', lat: 13.36, lng: 103.86, label: P, brands: ['Super', 'Vital', 'Diamond'], placeholder: true },
  { id: 'kc', province: 'Kampong Cham', lat: 12.0, lng: 105.46, label: P, brands: ['Master', 'Super', 'Echo'], placeholder: true },
  { id: 'tk', province: 'Takeo', lat: 10.99, lng: 104.78, label: P, brands: ['Master', 'Vital'], placeholder: true },
  { id: 'kp', province: 'Kampot', lat: 10.61, lng: 104.18, label: P, brands: ['Echo', 'Golden'], placeholder: true },
  { id: 'pv', province: 'Prey Veng', lat: 11.48, lng: 105.33, label: P, brands: ['Master', 'Super', 'Diamond'], placeholder: true },
  { id: 'svr', province: 'Svay Rieng', lat: 11.09, lng: 105.8, label: P, brands: ['Super', 'Golden'], placeholder: true },
  { id: 'bmc', province: 'Banteay Meanchey', lat: 13.59, lng: 102.97, label: P, brands: ['Master', 'Echo'], placeholder: true },
  { id: 'kt', province: 'Kampong Thom', lat: 12.71, lng: 104.89, label: P, brands: ['Vital', 'Diamond'], placeholder: true },
  { id: 'pst', province: 'Pursat', lat: 12.54, lng: 103.92, label: P, brands: ['Master', 'Golden'], placeholder: true },
  { id: 'krt', province: 'Kratie', lat: 12.49, lng: 106.03, label: P, brands: ['Super', 'Echo'], placeholder: true },
];
