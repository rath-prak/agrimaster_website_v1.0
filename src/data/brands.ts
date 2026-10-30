export interface Brand {
  name: string;
  className: string;
  logo: string;
  /** false = hide from the site until the name/spelling is verified */
  verified?: boolean | undefined;
}

export const brands: Brand[] = [
  { name: 'Master Feed', className: 'b1', logo: 'master.svg' },
  { name: 'Super Feed', className: 'b2', logo: 'super.svg' },
  { name: 'Eco Feed', className: 'b4', logo: 'echo.svg' },
  { name: 'Vital Feed', className: 'b5', logo: 'vital.svg' },
  { name: 'Golden Feed', className: 'b3', logo: 'golden.svg' },
  { name: 'Diamond Feed', className: 'b6', logo: 'diamond.svg' },
];

/** Brands safe to publish (verified spelling). */
export const publishedBrands = brands.filter((b) => b.verified !== false);
