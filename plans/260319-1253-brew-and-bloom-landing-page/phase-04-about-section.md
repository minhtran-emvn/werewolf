# Phase 04: About Section

## Context Links
- [Main Plan](./plan.md)
- [Phase 03: Hero](./phase-03-hero-section.md)

## Overview
- **Priority:** Medium
- **Status:** pending
- **Effort:** 1h

Tell cafe story with text and supporting image/illustration.

## Key Insights
- Two-column layout: text + image
- Stack vertically on mobile
- Keep copy concise (3-4 paragraphs max)

## Requirements

### Functional
- Section heading "Our Story"
- Brief history/mission paragraph
- Values highlight (quality, community, sustainability)
- Supporting image (cafe interior or barista)

### Non-Functional
- Balanced text-to-image ratio
- Engaging but not overwhelming

## Architecture
```html
<section id="about" class="about">
  <div class="container">
    <div class="about__content">
      <h2>Our Story</h2>
      <p>...</p>
      <ul class="about__values">
        <li>Quality beans</li>
        <li>Community space</li>
        <li>Sustainable practices</li>
      </ul>
    </div>
    <div class="about__image">
      <img src="..." alt="Cafe interior" loading="lazy">
    </div>
  </div>
</section>
```

## Related Code Files
- Modify: `index.html` (about section)
- Create: `css/sections/about.css`
- Add: `assets/images/about.jpg`

## Implementation Steps
1. Add about section HTML
2. Create about.css
3. Style two-column grid layout
4. Style section heading
5. Style paragraph text
6. Style values list (icons optional)
7. Style image with subtle shadow/border
8. Add responsive stacking for mobile
9. Add lazy loading to image

## Todo List
- [ ] Add about HTML markup
- [ ] Create about.css
- [ ] Two-column grid layout
- [ ] Style heading
- [ ] Style body text
- [ ] Style values list
- [ ] Style image
- [ ] Mobile responsive stack
- [ ] Add placeholder image

## Success Criteria
- Two columns on desktop, stacked on mobile
- Image loads lazily
- Text is scannable
- Visual balance achieved

## Risk Assessment
| Risk | Impact | Mitigation |
|------|--------|------------|
| Too much text | Med | Edit copy, use bullets |

## Security Considerations
- None for static content

## Next Steps
Proceed to [Phase 05: Menu Section](./phase-05-menu-section.md)
