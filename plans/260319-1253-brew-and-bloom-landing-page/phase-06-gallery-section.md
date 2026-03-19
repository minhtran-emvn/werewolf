# Phase 06: Gallery Section

## Context Links
- [Main Plan](./plan.md)
- [Phase 05: Menu](./phase-05-menu-section.md)

## Overview
- **Priority:** Medium
- **Status:** pending
- **Effort:** 1.5h

Visual showcase of cafe atmosphere, drinks, food.

## Key Insights
- CSS Grid for masonry-like layout
- Lazy load all images
- Consider lightbox for fullscreen view (optional)

## Requirements

### Functional
- Section heading "Gallery"
- 6-9 showcase images
- Grid layout with varied sizes
- Click to enlarge (optional)

### Non-Functional
- Fast loading (lazy + optimized)
- Visually appealing arrangement
- Consistent image quality

## Architecture
```html
<section id="gallery" class="gallery">
  <div class="container">
    <h2>Gallery</h2>
    <div class="gallery__grid">
      <figure class="gallery__item gallery__item--wide">
        <img src="..." alt="..." loading="lazy">
      </figure>
      <figure class="gallery__item">
        <img src="..." alt="..." loading="lazy">
      </figure>
      <!-- more items -->
    </div>
  </div>
</section>
```

## Related Code Files
- Modify: `index.html` (gallery section)
- Create: `css/sections/gallery.css`
- Add: `assets/images/gallery/` (6-9 images)

## Implementation Steps
1. Add gallery section HTML
2. Create gallery__grid container
3. Add 6-9 figure elements with images
4. Create gallery.css
5. Style CSS Grid layout (auto-fit columns)
6. Add featured image variants (--wide, --tall)
7. Style image hover effect (subtle zoom/shadow)
8. Ensure lazy loading attributes
9. Make responsive (fewer columns on mobile)
10. Optional: add simple lightbox JS

## Gallery Image Suggestions
1. Latte art closeup
2. Cafe interior wide shot
3. Pastry display
4. Barista at work
5. Cozy seating corner
6. Coffee beans
7. Plants/greenery decor
8. Customer enjoying drink
9. Exterior storefront

## Todo List
- [ ] Add gallery HTML structure
- [ ] Add figure elements
- [ ] Create gallery.css
- [ ] CSS Grid layout
- [ ] Featured item modifiers
- [ ] Hover effects
- [ ] Lazy loading
- [ ] Responsive columns
- [ ] Add placeholder images
- [ ] Optional: lightbox

## Success Criteria
- Grid displays correctly all sizes
- Images lazy load
- Hover states work
- No layout shift on load

## Risk Assessment
| Risk | Impact | Mitigation |
|------|--------|------------|
| Heavy images | High | Compress, WebP, lazy |
| Layout shift | Med | Set aspect ratios |

## Security Considerations
- Alt text for accessibility
- No user uploads

## Next Steps
Proceed to [Phase 07: Location/Hours](./phase-07-location-hours-section.md)
