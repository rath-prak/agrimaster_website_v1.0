/**
 * Next-phase content slots (brief phase 3). Intentionally EMPTY.
 * Add entries only from approved, real sources (signed-off farmer
 * stories, published news, verified distributor details). Nothing
 * renders while these arrays are empty; no placeholder content.
 */
export interface FarmerStory {
  name: string;
  province?: string | undefined;
  species?: string | undefined;
  quote: string;
  image?: string | undefined;
  approvedBy: string; // record of consent/approval
}
export interface Insight {
  title: string;
  date: string; // ISO
  summary: string;
  href: string;
}
export interface Distributor {
  name: string;
  province: string;
  phone?: string | undefined;
  address?: string | undefined;
  brands: string[]; // verified brand names only
  verifiedOn: string; // ISO date checked
}

export const farmerStories: FarmerStory[] = [];
export const insights: Insight[] = [];
export const distributors: Distributor[] = [];
