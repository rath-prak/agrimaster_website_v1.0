import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  site: 'https://rath-prak.github.io',
  base: '/agrimaster_website_v1.0',
  output: 'static',
  build: {
    assets: 'assets'
  },
  vite: {
    build: {
      assetsInlineLimit: 0
    }
  }
});
