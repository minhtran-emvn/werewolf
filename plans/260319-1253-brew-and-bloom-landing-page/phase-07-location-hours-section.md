# Phase 07: Location & Hours Section

## Context Links
- [Main Plan](./plan.md)
- [Phase 06: Gallery](./phase-06-gallery-section.md)

## Overview
- **Priority:** High
- **Status:** pending
- **Effort:** 1.5h

Display cafe address, hours of operation, embedded map.

## Key Insights
- Google Maps embed is free and simple
- Two-column: info + map
- Clear, scannable hours format

## Requirements

### Functional
- Section heading "Find Us"
- Full address with link to Google Maps
- Hours table (Mon-Sun)
- Embedded Google Map
- Optional: parking info

### Non-Functional
- Map loads efficiently (lazy iframe)
- Hours easy to scan
- Mobile-friendly stacking

## Architecture
```html
<section id="location" class="location">
  <div class="container">
    <h2>Find Us</h2>
    <div class="location__grid">
      <div class="location__info">
        <h3>Address</h3>
        <address>
          123 Bloom Street<br>
          Portland, OR 97201
        </address>
        <a href="https://maps.google.com/..." target="_blank">Get Directions</a>

        <h3>Hours</h3>
        <table class="location__hours">
          <tr><td>Mon-Fri</td><td>7am - 7pm</td></tr>
          <tr><td>Saturday</td><td>8am - 8pm</td></tr>
          <tr><td>Sunday</td><td>8am - 6pm</td></tr>
        </table>
      </div>
      <div class="location__map">
        <iframe src="..." loading="lazy"></iframe>
      </div>
    </div>
  </div>
</section>
```

## Related Code Files
- Modify: `index.html` (location section)
- Create: `css/sections/location.css`

## Implementation Steps
1. Add location section HTML
2. Add address with semantic `<address>` tag
3. Add hours table
4. Embed Google Maps iframe (placeholder coords)
5. Create location.css
6. Style two-column grid
7. Style address and hours table
8. Style directions link as button
9. Style map container with aspect ratio
10. Add lazy loading to iframe
11. Stack vertically on mobile

## Sample Data
**Address:**
123 Bloom Street, Portland, OR 97201

**Hours:**
- Mon-Fri: 7:00 AM - 7:00 PM
- Saturday: 8:00 AM - 8:00 PM
- Sunday: 8:00 AM - 6:00 PM

**Phone:** (503) 555-BREW

## Todo List
- [ ] Add location HTML structure
- [ ] Add address element
- [ ] Add hours table
- [ ] Add Google Maps iframe
- [ ] Create location.css
- [ ] Style grid layout
- [ ] Style address typography
- [ ] Style hours table
- [ ] Style map container
- [ ] Lazy load iframe
- [ ] Mobile responsive

## Success Criteria
- Address/hours clearly readable
- Map displays and is interactive
- Directions link opens Maps app
- Responsive on all devices

## Risk Assessment
| Risk | Impact | Mitigation |
|------|--------|------------|
| Maps API limits | Low | Embed is free tier |
| Slow iframe load | Med | Lazy load iframe |

## Security Considerations
- External link opens in new tab (rel="noopener")
- No API keys exposed in embed

## Next Steps
Proceed to [Phase 08: Contact Section](./phase-08-contact-section.md)
