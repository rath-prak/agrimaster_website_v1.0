export interface Stat {
  value: string;
  label: string;
  dark?: boolean;
}

export const capacityStats: Stat[] = [
  { value: '1,500', label: 'Tons / month aquafeed plant' },
  { value: '10,000', label: 'Tons new silo storage', dark: true },
  { value: '4', label: 'Feed categories' },
];

export const qualityStats = [
  {
    value: '30,000',
    label: 'tons per month at 100% full operation',
  },
  {
    value: '360,000',
    label: 'tons annual production capacity',
  },
  {
    value: '1,500',
    label: 'tons/month aquafeed plant (2020)',
  },
  {
    value: '10,000',
    label: 'tons storage in new silos (2023–2026)',
  },
];
