# Agri Master Cambodia Website

Official website for Agri Master Cambodia, showcasing our commitment to advancing Cambodia's agricultural sector through high-quality animal nutrition products and services.

**Live site:** https://rath-prak.github.io/agrimaster_website_v1.0/

Built with [Astro](https://astro.build/) — a modern, fast, and developer-friendly static site generator.

## Project Structure

```
agrimaster_website_v1.0/
├── src/
│   ├── components/       # Reusable Astro components
│   │   ├── Header.astro
│   │   ├── Footer.astro
│   │   ├── ProductCard.astro
│   │   ├── StatCard.astro
│   │   ├── Timeline.astro
│   │   ├── BrandGrid.astro
│   │   ├── CTA.astro
│   │   └── Hero.astro
│   ├── data/            # Typed content data (products, brands, milestones, stats)
│   │   ├── products.ts
│   │   ├── brands.ts
│   │   ├── milestones.ts
│   │   └── stats.ts
│   ├── layouts/         # Page layouts
│   │   └── Layout.astro
│   ├── lib/             # Data access layer (CMS-ready)
│   │   └── products.ts
│   ├── pages/           # Routes (each .astro file = page)
│   │   ├── index.astro
│   │   ├── about.astro
│   │   ├── products.astro
│   │   └── contact.astro
│   └── styles/          # Global CSS
│       └── global.css
├── public/              # Static assets (images, logos, favicon)
│   └── assets/
├── .github/workflows/   # GitHub Actions CI/CD
│   └── deploy.yml
├── astro.config.mjs     # Astro configuration
├── tsconfig.json        # TypeScript configuration
├── .nvmrc               # Node version (LTS 20)
├── .prettierrc.json     # Code formatting
└── package.json         # Dependencies and scripts
```

## Prerequisites

- **Node.js 20.x LTS** (pinned in `.nvmrc`)
- **npm 10+**

To use the pinned Node version with [nvm](https://github.com/nvm-sh/nvm):

```bash
nvm use
```

## Quick Start

### 1. Install Dependencies

```bash
npm install
```

### 2. Development Server

Start the Astro dev server with hot reload:

```bash
npm run dev
```

Then open http://localhost:4321 in your browser.

### 3. Build for Production

```bash
npm run build
```

Output: `dist/` directory with static HTML, CSS, JS, and assets ready for deployment.

### 4. Preview Production Build

```bash
npm run preview
```

Serves the built site locally to verify the production build.

## Available Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server (http://localhost:4321) |
| `npm run build` | Type-check and build for production → `dist/` |
| `npm run preview` | Preview the production build locally |
| `npm run check` | Run Astro type checking and diagnostics |
| `npm run format` | Format code with Prettier |

## Making Content Changes

### Editing Products, Brands, Milestones

All content is defined as typed TypeScript data in `src/data/*.ts`:

- **Products**: `src/data/products.ts` — feed lines (Swine, Poultry, Ruminant, Aquaculture)
- **Brands**: `src/data/brands.ts` — six brand names and styling
- **Milestones**: `src/data/milestones.ts` — company history timeline
- **Stats**: `src/data/stats.ts` — capacity and quality statistics

Edit these files directly. Types are enforced, so TypeScript will catch errors.

### Editing Pages

Page content lives in `src/pages/*.astro`:

- `index.astro` — Homepage
- `about.astro` — About page
- `products.astro` — Products page
- `contact.astro` — Contact page

Astro uses component-based architecture. Shared sections (header, footer, CTA, etc.) are in `src/components/`.

### Editing Styles

Global styles are in `src/styles/global.css`. The existing design is preserved exactly.

### Adding Images

Place images in `public/assets/img/`. Reference them in code like:

```astro
<img src={`${base}assets/img/your-image.jpg`} alt="Description" />
```

## Data Access Layer (CMS-Ready)

All content is accessed through `src/lib/products.ts`, which provides async functions:

- `getProducts()` — fetch products
- `getBrands()` — fetch brands  
- `getMilestones()` — fetch milestones
- `getHeroStats()`, `getCapacityStats()`, `getQualityStats()` — fetch stats

Currently these read from local `src/data/*.ts` files, but the architecture supports swapping to a headless CMS (like Strapi) with minimal changes. See **Connecting Strapi** below.

## Connecting Strapi (Future Enhancement)

The site is structured to easily connect to [Strapi](https://strapi.io/) or another headless CMS:

### Current Architecture

- Content is defined in `src/data/*.ts` files (TypeScript)
- Accessed via `src/lib/products.ts` data access functions
- Components use these functions: `const products = await getProducts();`

### To Connect Strapi

1. **Set Up Strapi** (separate repo/server):
   - Install Strapi: `npx create-strapi-app@latest my-agrimaster-cms`
   - Create content types matching `src/data/*.ts` structures (Product, Brand, Milestone, etc.)
   - Populate content via Strapi admin panel
   - Generate API token with read permissions

2. **Configure Environment Variables**:
   ```bash
   # .env (local dev) or Secrets (GitHub Actions)
   STRAPI_URL=https://your-strapi-instance.com
   STRAPI_TOKEN=your_api_token_here
   ```

3. **Update `src/lib/products.ts`**:
   Replace the local imports with fetch calls:
   
   ```typescript
   export async function getProducts(): Promise<Product[]> {
     const response = await fetch(`${import.meta.env.STRAPI_URL}/api/products?populate=*`, {
       headers: { Authorization: `Bearer ${import.meta.env.STRAPI_TOKEN}` }
     });
     const { data } = await response.json();
     return data.map(item => ({
       id: item.attributes.slug,
       name: item.attributes.name,
       // ... map Strapi fields to Product type
     }));
   }
   ```

4. **Rebuild**:
   ```bash
   npm run build
   ```
   
   Astro fetches from Strapi at build time and generates static HTML.

5. **Webhook for Auto-Rebuild** (optional):
   - In Strapi, set up a webhook to trigger on content publish:  
     URL: `https://api.github.com/repos/rath-prak/agrimaster_website_v1.0/actions/workflows/deploy.yml/dispatches`
   - Requires GitHub personal access token with `repo` scope
   - Payload: `{ "ref": "main" }`
   - Now publishing in Strapi auto-deploys the website

### Benefits

- Non-technical editors can update content via Strapi UI
- No code changes needed for content updates
- Static site remains fast and secure
- Rebuild only when content changes (via webhook)

## Deployment

The site is deployed to **GitHub Pages** via **GitHub Actions** on every push to `main`.

### GitHub Actions Workflow

The workflow (`.github/workflows/deploy.yml`):

1. Checks out code
2. Sets up Node.js 20
3. Installs dependencies (`npm ci`)
4. Builds the site (`npm run build`)
5. Deploys `dist/` to GitHub Pages

### GitHub Pages Configuration

**Required Settings** (if not already configured):

1. Go to: https://github.com/rath-prak/agrimaster_website_v1.0/settings/pages
2. Under "Build and deployment":
   - Source: **GitHub Actions**
3. Save

The site will auto-deploy on every push to `main`.

### Manual Deployment

To deploy changes:

```bash
# Make your changes
# Test locally
npm run dev

# Build and check
npm run build

# Commit and push to main
git add .
git commit -m "Update: describe changes"
git push origin main
```

GitHub Actions will automatically build and deploy (usually 1-2 minutes).

## Content Placeholders

The following content is marked with `<span class="todo">` and needs to be provided:

### Contact Information
- ☐ Phone number
- ☐ Email address  
- ☐ Full street address
- ☐ Opening hours
- ☐ Exact map pin location (currently shows Kandal Province region)

### Branding
- ☐ Brand logos / packaging photos for all six feed brands (Master Feed, Super Feed, Golden Feed, Echo Feed, Vital Feed, Diamond Feed)
- ☐ Formal mission statement

### Social Media
- ☐ Facebook URL
- ☐ Telegram URL
- ☐ YouTube URL

### Contact Form
- ☐ Backend API endpoint for form submissions (currently demo-only)

## Image Credits & Licensing

### Hero Image (Required Attribution)
**Must remain visible in the footer:**

- "Cambodia's rice fields" by Dmitry A. Mottl
- Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Cambodia%27s_rice_fields.jpg)
- License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

### Other Images
All other images in `public/assets/img/` (feed mill, production line, animals, raw materials):
- ☐ **Confirm usage rights and licensing**
- ☐ **Add proper credits if required**

See `public/assets/img/CREDITS.txt` for image source information.

### Profile Photos / Staff
If adding team or staff photos:
- ☐ **Obtain signed usage consent** from individuals before publishing

## Code Quality

### Type Checking

Astro + TypeScript enforces types for content and components:

```bash
npm run check
```

Runs before every build to catch type errors.

### Code Formatting

Prettier with Astro plugin formats code consistently:

```bash
npm run format
```

Configuration in `.prettierrc.json`.

## Browser Support

The site works on:
- Modern browsers (Chrome, Firefox, Safari, Edge - last 2 versions)
- Mobile devices (responsive design)
- Screen readers and assistive technologies

## Technical Details

### Stack
- **Astro 5.x** — Static site generator
- **TypeScript** — Type safety and better DX
- **CSS** — No preprocessor, vanilla CSS with variables
- **Deployment** — GitHub Actions → GitHub Pages

### Performance
- Static HTML (no JavaScript framework overhead)
- Optimized images
- Lazy loading for below-the-fold images
- Minimal client JavaScript (only menu toggle)

### Accessibility
- Semantic HTML5
- ARIA labels for interactive elements
- Skip link for keyboard navigation
- Proper heading hierarchy
- WCAG AA color contrast

## Troubleshooting

### Build Errors

**TypeScript errors:**
```bash
npm run check
```
Fix type errors in `.astro` or `.ts` files.

**Module not found:**
```bash
rm -rf node_modules package-lock.json
npm install
```

### Development Server Issues

**Port already in use:**
```bash
# Kill process on port 4321
lsof -ti:4321 | xargs kill -9
```

**Changes not reflecting:**
- Hard reload: `Cmd/Ctrl + Shift + R`
- Clear `.astro` cache: `rm -rf .astro`

### Deployment Issues

**GitHub Actions failing:**
- Check Actions tab for logs
- Verify Node version matches `.nvmrc`
- Ensure all dependencies are in `package.json`

**404 on GitHub Pages:**
- Verify Pages source is set to **GitHub Actions** (not branch)
- Check `astro.config.mjs` has correct `site` and `base`
- Wait 1-2 minutes for deploy to complete

## Branching Strategy

- **`main`** — Production branch (auto-deploys to GitHub Pages)
- **`dev`** — Development branch for ongoing work
- Feature branches — Create from `dev`, merge back to `dev`, then to `main`

## Support

For technical questions about this codebase, contact the development team.

For business inquiries, visit the [Contact page](https://rath-prak.github.io/agrimaster_website_v1.0/contact).

---

**Last updated:** October 2026  
**Built with:** Astro 5.x + TypeScript  
**Maintained by:** Agri Master Cambodia Development Team

## Typography

All hero headlines and large section headings (h1, h2, Raw Materials intro heading) use `line-height: var(--display-lh)` (1.1), set once in `src/styles/global.css`.
