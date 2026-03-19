# Phase 01: Project Setup

## Context Links
- [Main Plan](./plan.md)

## Overview
- **Priority:** High (blocking)
- **Status:** pending
- **Effort:** 1h

Initialize project structure, configure tooling, set up development environment.

## Key Insights
- Vanilla HTML/CSS/JS keeps bundle size minimal
- No build step needed for simple landing page
- Live Server extension recommended for dev

## Requirements

### Functional
- Index.html as entry point
- Organized folder structure
- Placeholder content structure

### Non-Functional
- Fast initial load (<2s)
- No external dependencies beyond fonts

## Architecture
```
brew-and-bloom/
├── index.html           # Main entry
├── css/
│   ├── variables.css    # CSS custom properties
│   ├── base.css         # Reset + typography
│   └── sections/        # Per-section styles
├── js/
│   └── main.js          # Minimal interactivity
└── assets/
    └── images/          # Optimized images
```

## Related Code Files
- Create: `index.html`
- Create: `css/variables.css`
- Create: `css/base.css`
- Create: `js/main.js`
- Create: `.gitignore`

## Implementation Steps
1. Create project root directory structure
2. Initialize git repo
3. Create `.gitignore` (OS files, editor configs, .DS_Store)
4. Create `index.html` with HTML5 boilerplate
5. Link CSS/JS files in head
6. Add meta tags (viewport, description, OG tags)
7. Create empty section containers
8. Verify dev server loads correctly

## Todo List
- [ ] Create folder structure
- [ ] Init git repo
- [ ] Create .gitignore
- [ ] Create index.html boilerplate
- [ ] Create empty CSS files
- [ ] Create main.js
- [ ] Test with live server

## Success Criteria
- `index.html` loads without errors
- All linked resources resolve (no 404s)
- Viewport meta present for mobile
- Git initialized with clean working tree

## Risk Assessment
| Risk | Impact | Mitigation |
|------|--------|------------|
| Missing folder | Low | Check structure before coding |

## Security Considerations
- No sensitive data in repo
- CSP headers if deploying

## Next Steps
Proceed to [Phase 02: Design System](./phase-02-design-system.md)
