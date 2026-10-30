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

/* ------------------------------------------------------------------
 * SKU catalogue (product discovery).
 * Populate ONLY from approved, current product source records
 * (e.g. brand brochures confirmed as active). Never infer values or
 * copy one product's nutrition spec to another. Optional fields are
 * shown only when present. While empty, the Animal Feed page shows an
 * enquiry empty state per species, and stage/brand/form filters stay
 * hidden (filters render only when SKUs supply those values).
 * ------------------------------------------------------------------ */
export type Species = 'swine' | 'poultry' | 'ruminant' | 'aquaculture';
export type ProductType = 'complete' | 'concentrate';
export type FeedForm = 'mash' | 'pellet' | 'crumble' | 'floating-pellet';

export interface Sku {
  code: string;
  name: string;
  brand: string; // must match a verified name in brands.ts
  species: Species;
  stage?: string | undefined;
  productType?: ProductType | undefined; // verified per SKU
  form?: FeedForm | undefined;
  packSize?: string | undefined;
  registrationNo?: string | undefined;
  instructions?: string | undefined;
  nutrition?: { label: string; value: string }[] | undefined;
}

export const skus: Sku[] = [];
