# Phase 03: Hero Section

## Context Links
- [Main Plan](./plan.md)
- [Phase 02: Design System](./phase-02-design-system.md)

## Overview
- **Priority:** High
- **Status:** pending
- **Effort:** 1.5h

Full-viewport hero with background image, headline, tagline, CTA button.

## Key Insights
- Hero sets first impression - must load fast
- Background image needs overlay for text readability
- CTA should scroll to Menu or Contact section

## Requirements

### Functional
- Full-height viewport on load
- Background image (cafe ambiance)
- Overlay gradient for contrast
- Headline: "Brew & Bloom"
- Tagline: "Where coffee meets calm"
- Primary CTA button

### Non-Functional
- Image lazy-loaded or optimized
- Text readable on any background
- Smooth scroll to section

## Architecture
```html
<section id="hero" class="hero">
  <div class="hero__overlay"></div>
  <div class="hero__content">
    <h1>Brew & Bloom</h1>
    <p class="hero__tagline">Where coffee meets calm</p>
    <a href="#menu" class="btn btn-primary">Explore Menu</a>
  </div>
</section>
```

## Related Code Files
- Modify: `index.html` (hero section)
- Create: `css/sections/hero.css`
- Add: `assets/images/hero-bg.jpg` (placeholder)

## Implementation Steps
1. Add hero section HTML structure
2. Create hero.css with full-viewport styles
3. Add background image with cover/center
4. Create semi-transparent overlay (linear-gradient)
5. Center content using flexbox
6. Style headline with large font size
7. Style tagline with lighter weight
8. Style CTA button
9. Add smooth scroll behavior (CSS or JS)
10. Optimize/compress hero image

## Todo List
- [ ] Add hero HTML markup
- [ ] Create hero.css
- [ ] Style full-viewport background
- [ ] Add overlay gradient
- [ ] Center content with flexbox
- [ ] Style headline
- [ ] Style tagline
- [ ] Style CTA button
- [ ] Add smooth scroll
- [ ] Optimize background image

## Success Criteria
- Hero fills viewport on load
- Text is readable over image
- CTA scrolls smoothly to target
- Works on mobile (no horizontal scroll)

## Risk Assessment
| Risk | Impact | Mitigation |
|------|--------|------------|
| Large image = slow load | High | Compress, use WebP, lazy attrs |
| Text unreadable | Med | Darker overlay, text-shadow |

## Security Considerations
- No user input in this section

## Next Steps
Proceed to [Phase 04: About Section](./phase-04-about-section.md)
