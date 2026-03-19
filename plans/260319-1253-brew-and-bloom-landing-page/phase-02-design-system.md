# Phase 02: Design System

## Context Links
- [Main Plan](./plan.md)
- [Phase 01: Setup](./phase-01-project-setup.md)

## Overview
- **Priority:** High
- **Status:** pending
- **Effort:** 1.5h

Establish CSS custom properties, typography scale, spacing system, reusable component classes.

## Key Insights
- CSS custom properties enable easy theming
- Mobile-first breakpoints: 320px base, 768px tablet, 1024px desktop
- Consistent spacing scale (4px base unit)

## Requirements

### Functional
- Color palette variables
- Typography scale (headings, body, captions)
- Spacing utilities
- Button/link component styles

### Non-Functional
- Consistent visual rhythm
- Easy maintenance/updates

## Architecture

### Color Tokens
```css
--color-brown-dark: #4A3728;
--color-brown-light: #8B7355;
--color-green: #5D7B6F;
--color-cream: #F5F1EB;
--color-white: #FFFFFF;
```

### Typography
- Headings: Playfair Display, serif
- Body: Lato, sans-serif
- Scale: 1.25 ratio (minor third)

### Spacing Scale
```css
--space-xs: 4px;
--space-sm: 8px;
--space-md: 16px;
--space-lg: 32px;
--space-xl: 64px;
```

## Related Code Files
- Modify: `index.html` (add Google Fonts link)
- Create: `css/variables.css`
- Create: `css/base.css`
- Create: `css/components.css`

## Implementation Steps
1. Add Google Fonts link to index.html
2. Define color variables in variables.css
3. Define spacing scale
4. Define typography scale
5. Create CSS reset in base.css
6. Set body defaults (font-family, line-height, color)
7. Create heading styles (h1-h6)
8. Create button component (.btn, .btn-primary, .btn-secondary)
9. Create link hover states
10. Create container/wrapper utility class

## Todo List
- [ ] Add Google Fonts link
- [ ] Create variables.css with colors
- [ ] Add spacing scale
- [ ] Add typography scale
- [ ] Create base.css reset
- [ ] Style body defaults
- [ ] Style headings h1-h6
- [ ] Create button components
- [ ] Create container utility
- [ ] Test on different screen sizes

## Success Criteria
- All variables defined and working
- Typography renders with correct fonts
- Buttons have hover/focus states
- No FOUT (flash of unstyled text)

## Risk Assessment
| Risk | Impact | Mitigation |
|------|--------|------------|
| Font load failure | Med | Fallback stack defined |
| Variable browser support | Low | Modern browsers only |

## Security Considerations
- Google Fonts loaded over HTTPS
- Consider self-hosting fonts for privacy

## Next Steps
Proceed to [Phase 03: Hero Section](./phase-03-hero-section.md)
