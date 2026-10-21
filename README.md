# Agri Master Cambodia Website

Official website for Agri Master Cambodia, showcasing our commitment to advancing Cambodia's agricultural sector through high-quality animal nutrition products and services.

**Live site:** https://rath-prak.github.io/agrimaster_website_v1.0/

## Project Structure

```
agrimaster_website_v1.0/
├── docs/              # Built website (GitHub Pages serves from here)
│   ├── *.html         # Generated HTML pages
│   ├── styles.css     # Compiled styles
│   ├── assets/        # Images, logos, SVGs
│   └── .nojekyll      # GitHub Pages config
├── src/               # Source files
│   ├── build.py       # Static site generator
│   ├── styles.css     # Source stylesheet
│   ├── assets/        # Source images and media
│   └── templates/     # HTML templates (base, header, footer)
├── scripts/           # Development tools
│   ├── devserver.py   # Local dev server with live reload
│   ├── shoot.py       # Screenshot generator (Playwright)
│   └── livereload.js  # Live reload client script
└── README.md          # This file
```

## Prerequisites

- **Python 3.8+** for building and development server
- **Git** for version control
- **Optional:** Playwright for screenshots (`pip install playwright`)

## Quick Start

### 1. Build the Site

```bash
cd src
python3 build.py
```

This generates the complete website in `docs/` from templates and content definitions.

### 2. Preview Locally

**Option A: Development server with live reload (recommended)**

```bash
python3 scripts/devserver.py
```

Then open http://localhost:8080 in your browser. The page will automatically reload when files in `docs/` change.

To use a custom port or root directory:
```bash
PORT=3000 python3 scripts/devserver.py
AGRIMASTER_ROOT=/path/to/docs python3 scripts/devserver.py
```

**Option B: Simple static server**

```bash
cd docs
python3 -m http.server 8080
```

Then open http://localhost:8080 (no live reload).

## Development Workflow

### Making Content Changes

1. **Edit content** in `src/build.py`:
   - Page content is defined in functions like `build_home()`, `build_about()`, etc.
   - Modify text, structure, or add new sections
   - Product data, brands, timeline are defined as data structures at the top

2. **Edit templates** in `src/templates/`:
   - `base.html` - Overall page structure
   - `header.html` - Site header and navigation
   - `footer.html` - Site footer

3. **Edit styles** in `src/styles.css`

4. **Rebuild** the site:
   ```bash
   cd src && python3 build.py
   ```

5. **Preview changes** with the dev server (auto-reloads on file changes):
   ```bash
   python3 scripts/devserver.py
   ```

### Workflow Tips

- The dev server watches `docs/` for changes and auto-reloads the browser
- Run the build script each time you change source files
- Commit both source (`src/`) and built files (`docs/`) together

## Deployment

### GitHub Pages Setup

The site is deployed via **GitHub Pages** from the `docs/` folder on the `main` branch.

**Initial setup** (if not already configured):

1. Go to repository Settings → Pages
2. Under "Build and deployment":
   - Source: **Deploy from a branch**
   - Branch: **main**
   - Folder: **/ (root)** or **/docs** (recommended)
3. Save

GitHub Pages will automatically deploy when you push changes to `main`.

### Deploying Changes

```bash
# Make your changes in src/
# Rebuild
cd src && python3 build.py

# Commit both source and built files
git add src/ docs/
git commit -m "Update content: [describe changes]"

# Push to GitHub
git push origin main
```

GitHub Pages will rebuild and deploy automatically (usually within 1-2 minutes).

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

### Hero Image
**Required attribution (already included in footer):**
- "Cambodia's rice fields" by Dmitry A. Mottl
- Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Cambodia%27s_rice_fields.jpg)
- License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- **This attribution must remain visible in the footer**

### Other Images
All other images in `assets/img/` (feed mill, production line, animals, raw materials):
- ☐ **Confirm usage rights and licensing**
- ☐ **Add proper credits if required**

See `assets/img/CREDITS.txt` for image source information.

### Profile Photos / Staff
If adding team or staff photos:
- ☐ **Obtain signed usage consent** from individuals before publishing

## Browser Support

The site is designed to work on:
- Modern browsers (Chrome, Firefox, Safari, Edge - last 2 versions)
- Mobile devices (responsive design with mobile-first approach)
- Screen readers and assistive technologies (semantic HTML, ARIA labels)

## Technical Details

### Static Site Generator
- Pure Python, no external dependencies for building
- Template-based approach with shared header/footer
- Content defined as Python data structures and functions
- Output: clean, standards-compliant HTML

### Styling
- Single `styles.css` file (no preprocessor)
- CSS custom properties (variables) for theming
- Mobile-first responsive design
- Minimal JavaScript (only mobile menu toggle)

### Performance
- Optimized images (JPEG for photos, SVG for logos)
- Lazy loading for below-the-fold images
- No external dependencies (except fonts if added)
- Static HTML = fast loading

### Accessibility
- Semantic HTML5 elements
- ARIA labels for interactive elements
- Skip link for keyboard navigation
- Proper heading hierarchy
- Color contrast meets WCAG AA standards

## Maintenance

### Adding a New Page

1. Add content function in `src/build.py`:
   ```python
   def build_newpage():
       return '<section>Your content here</section>'
   ```

2. Add to navigation array:
   ```python
   NAV = [..., ("newpage.html", "New Page")]
   ```

3. Add to pages list in `main()`:
   ```python
   ("newpage.html", "Title", "Description", build_newpage())
   ```

4. Rebuild and commit.

### Updating Products or Brands

Edit the `PRODUCTS` or `BRANDS` lists at the top of `src/build.py`, then rebuild.

### Changing Styles

Edit `src/styles.css`, then copy to `docs/styles.css` (or run the full build).

## Troubleshooting

### Build Issues
- **Error: "No such file or directory"**: Run `build.py` from the `src/` directory
- **Missing templates**: Ensure `src/templates/` contains `base.html`, `header.html`, `footer.html`

### Dev Server Issues
- **Port already in use**: Change port with `PORT=3000 python3 scripts/devserver.py`
- **Live reload not working**: Check browser console for errors; ensure livereload.js is present

### Deployment Issues
- **Site not updating**: Check GitHub Actions tab for build errors
- **404 errors**: Verify GitHub Pages source is set correctly (branch: main, folder: /docs)
- **Images not loading**: Check that `assets/` was committed and paths are relative

## GitHub Actions (Optional)

A GitHub Actions workflow is included at `.github/workflows/check-build.yml` that:
- Runs on every pull request
- Rebuilds the site from source
- Fails if `docs/` is out of date (i.e., source was changed but site wasn't rebuilt)

This prevents deploying stale content.

## Branching Strategy

- **`main`** - Production branch (deploys to GitHub Pages)
- **`dev`** - Development branch for ongoing work
- Feature branches - Create from `dev` for specific changes, merge back to `dev`, then to `main`

## Support

For technical questions about this codebase, contact the development team.

For business inquiries, visit the [Contact page](https://rath-prak.github.io/agrimaster_website_v1.0/contact.html).

---

**Last updated:** October 2026  
**Maintained by:** Agri Master Cambodia Development Team
