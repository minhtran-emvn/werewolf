# Phase 09: Responsive Polish

## Context Links
- [Main Plan](./plan.md)
- [Phase 08: Contact](./phase-08-contact-section.md)

## Overview
- **Priority:** High
- **Status:** pending
- **Effort:** 1h

Final responsive testing, performance optimization, cross-browser checks.

## Key Insights
- Test all breakpoints systematically
- Performance audit with Lighthouse
- Fix any accessibility issues

## Requirements

### Functional
- Add navigation header with scroll links
- Add footer with copyright
- Smooth scroll behavior
- Mobile hamburger menu (optional)

### Non-Functional
- Lighthouse score >90
- WCAG AA compliance
- Works in Chrome, Firefox, Safari, Edge
- No horizontal scroll at any breakpoint

## Architecture

### Navigation
```html
<header class="header">
  <nav class="nav container">
    <a href="#" class="nav__logo">Brew & Bloom</a>
    <ul class="nav__links">
      <li><a href="#about">About</a></li>
      <li><a href="#menu">Menu</a></li>
      <li><a href="#gallery">Gallery</a></li>
      <li><a href="#location">Visit</a></li>
      <li><a href="#contact">Contact</a></li>
    </ul>
  </nav>
</header>
```

### Footer
```html
<footer class="footer">
  <p>&copy; 2026 Brew & Bloom. All rights reserved.</p>
</footer>
```

## Related Code Files
- Modify: `index.html` (add header/footer)
- Create: `css/sections/header.css`
- Create: `css/sections/footer.css`
- Modify: `css/base.css` (responsive utilities)
- Modify: `js/main.js` (mobile menu toggle)

## Implementation Steps

### Navigation & Footer
1. Add sticky header with nav links
2. Style nav for desktop
3. Add mobile hamburger menu
4. Add JS toggle for mobile nav
5. Add footer with copyright

### Responsive Testing
6. Test at 320px (small mobile)
7. Test at 375px (iPhone)
8. Test at 768px (tablet)
9. Test at 1024px (laptop)
10. Test at 1440px (desktop)
11. Fix any layout breaks

### Performance
12. Run Lighthouse audit
13. Optimize images (compress, WebP)
14. Minimize CSS if needed
15. Add meta description, OG tags

### Accessibility
16. Check color contrast
17. Verify focus states
18. Test keyboard navigation
19. Add skip-to-content link
20. Verify alt texts

## Breakpoint Checklist
| Breakpoint | Issues | Fixed |
|------------|--------|-------|
| 320px | | |
| 375px | | |
| 768px | | |
| 1024px | | |
| 1440px | | |

## Todo List
- [ ] Add header navigation
- [ ] Style desktop nav
- [ ] Add mobile hamburger
- [ ] Add mobile nav toggle JS
- [ ] Add footer
- [ ] Test 320px breakpoint
- [ ] Test 375px breakpoint
- [ ] Test 768px breakpoint
- [ ] Test 1024px breakpoint
- [ ] Test 1440px breakpoint
- [ ] Run Lighthouse audit
- [ ] Optimize images
- [ ] Check color contrast
- [ ] Test keyboard nav
- [ ] Add skip-to-content link
- [ ] Final cross-browser test

## Success Criteria
- Navigation works on all devices
- No horizontal scroll anywhere
- Lighthouse >90 performance
- WCAG AA compliance
- Works in all major browsers

## Risk Assessment
| Risk | Impact | Mitigation |
|------|--------|------------|
| Safari quirks | Med | Test early, use prefixes |
| Performance issues | High | Optimize images first |

## Security Considerations
- External links use rel="noopener"
- No tracking scripts without consent

## Next Steps
- Deploy to hosting (Netlify/Vercel/GitHub Pages)
- Connect custom domain
- Set up analytics (optional)
