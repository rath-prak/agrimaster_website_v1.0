/**
 * Product data access layer
 *
 * This module provides a single point of access to product, brand, milestone,
 * and stats data. Currently reads from local TypeScript files in src/data/,
 * but can be swapped to fetch from a Strapi CMS or other headless CMS at build
 * time by only changing this module.
 *
 * To connect Strapi later:
 * 1. Set STRAPI_URL and STRAPI_TOKEN environment variables
 * 2. Replace the imports and return statements with fetch calls to Strapi API
 * 3. Keep the same TypeScript types for consistency
 */

import type { Product } from '../data/products';
import type { Brand } from '../data/brands';
import type { Milestone } from '../data/milestones';
import { products as localProducts } from '../data/products';
import { publishedBrands as localBrands } from '../data/brands';
import { milestones as localMilestones } from '../data/milestones';
import {
  capacityStats as localCapacityStats,
  qualityStats as localQualityStats,
} from '../data/stats';

// Export types for use in components
export type { Product, Brand, Milestone };

/**
 * Get all products
 * @returns Array of products with full details
 */
export async function getProducts(): Promise<Product[]> {
  // TODO: Replace with Strapi fetch when ready
  // const response = await fetch(`${import.meta.env.STRAPI_URL}/api/products`, {
  //   headers: { Authorization: `Bearer ${import.meta.env.STRAPI_TOKEN}` }
  // });
  // return response.json();

  return localProducts;
}

/**
 * Get all brands
 * @returns Array of brand names and CSS class names
 */
export async function getBrands(): Promise<Brand[]> {
  // TODO: Replace with Strapi fetch when ready
  return localBrands;
}

/**
 * Get company milestones
 * @returns Array of milestone years and descriptions
 */
export async function getMilestones(): Promise<Milestone[]> {
  // TODO: Replace with Strapi fetch when ready
  return localMilestones;
}

/**
 * Get production capacity stats
 * @returns Array of stat cards for capacity section
 */
export async function getCapacityStats() {
  // TODO: Replace with Strapi fetch when ready
  return localCapacityStats;
}

/**
 * Get quality/capacity stats (about page)
 * @returns Array of large stat displays
 */
export async function getQualityStats() {
  // TODO: Replace with Strapi fetch when ready
  return localQualityStats;
}
