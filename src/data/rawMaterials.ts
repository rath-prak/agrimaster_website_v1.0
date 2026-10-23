export interface RawTile {
  kind: 'image' | 'text';
  /** image tiles */
  image?: string;
  alt?: string;
  /** text tiles */
  title?: string;
  body?: string;
  tone?: 'grey' | 'lime';
}

export const rawMaterials = {
  image: 'corn-hero.jpg',
  imageAlt: 'Golden corn kernels being loaded into a storage pile',
  headline: ['Supporting Local Agriculture.', 'International Standards.'],
  headlineMuted: 'Quality Animal Nutrition.',
  pill: 'RAW MATERIALS',
  heading: 'Quality animal nutrition starts with high',
  headingMuted: 'quality ingredients.',
  lead: 'Agri-Master prioritises locally sourced agricultural products while importing high-quality raw materials to produce nutritious, consistent feed for Cambodia\u2019s livestock and aquaculture industries.',
  body: 'Our sourcing approach supports Cambodian agriculture while providing access to quality ingredients from international markets. All raw materials undergo strict in-house quality control to ensure nutritional value, safety, and consistency.',
  tiles: [
    { kind: 'image', image: 'farmer-field.jpg', alt: 'Cambodian woman working in a field' },
    {
      kind: 'text',
      tone: 'grey',
      title: 'Supporting Cambodian Farmers',
      body: 'We prioritise purchasing locally grown corn, cassava, broken rice, and rice bran whenever available, supporting Cambodian farmers and the local agricultural economy.',
    },
    { kind: 'image', image: 'local-crops.jpg', alt: 'Village vegetable beds in Cambodia' },
    {
      kind: 'text',
      tone: 'lime',
      title: 'High quality International suppliers',
      body: 'We source high-quality raw materials from international suppliers, primarily in the United States, to complement local ingredients and support our animal nutrition formulations.',
    },
  ] as RawTile[],
};
