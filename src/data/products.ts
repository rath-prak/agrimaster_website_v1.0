export interface Product {
  id: string;
  name: string;
  image: string;
  description: string;
  features: string[];
}

export const products: Product[] = [
  {
    id: 'swine',
    name: 'Swine',
    image: 'stock-swine.webp',
    description:
      'Feed for all production stages — from piglet starter to finishing pig, gestation and sows.',
    features: ['Piglet starter', 'Grower &amp; finishing pig', 'Gestation', 'Sows'],
  },
  {
    id: 'poultry',
    name: 'Poultry',
    image: 'stock-poultry.webp',
    description:
      'Feed for native, layers and broilers — from chick starter to grower and finisher.',
    features: ['Native chicken', 'Layers', 'Broilers', 'Chick starter → grower → finisher'],
  },
  {
    id: 'ruminant',
    name: 'Ruminant',
    image: 'stock-cattle.webp',
    description:
      'Feed for cattle, goats and others — from young stock to adult and fattening.',
    features: ['Cattle', 'Goats', 'Young stock → adult', 'Fattening'],
  },
  {
    id: 'aquaculture',
    name: 'Aquaculture',
    image: 'stock-aquaculture.webp',
    description:
      'Feed for freshwater fish — from fingerlings through every growth stage to harvest.',
    features: ['Freshwater fish', 'Fingerlings', 'Every growth stage', 'Floating fish feed'],
  },
];

