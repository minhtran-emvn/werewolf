# Phase 05: Menu Section

## Context Links
- [Main Plan](./plan.md)
- [Phase 04: About](./phase-04-about-section.md)

## Overview
- **Priority:** High
- **Status:** pending
- **Effort:** 2h

Display cafe menu with categories, items, prices.

## Key Insights
- Organize by category (Coffee, Tea, Pastries, etc.)
- Card or list layout works well
- Optional: category tabs/filters

## Requirements

### Functional
- Section heading "Our Menu"
- Categories: Coffee, Tea, Pastries, Light Bites
- Item name + description + price
- Optional item images

### Non-Functional
- Easy to scan
- Clear pricing
- Appetizing presentation

## Architecture
```html
<section id="menu" class="menu">
  <div class="container">
    <h2>Our Menu</h2>
    <div class="menu__categories">
      <div class="menu__category">
        <h3>Coffee</h3>
        <div class="menu__items">
          <article class="menu__item">
            <h4>Espresso</h4>
            <p>Rich, bold single shot</p>
            <span class="menu__price">$3.50</span>
          </article>
          <!-- more items -->
        </div>
      </div>
      <!-- more categories -->
    </div>
  </div>
</section>
```

## Related Code Files
- Modify: `index.html` (menu section)
- Create: `css/sections/menu.css`

## Implementation Steps
1. Add menu section HTML structure
2. Create category containers
3. Add 4-6 items per category (sample data)
4. Create menu.css
5. Style grid layout for categories
6. Style individual menu items (card style)
7. Style item name/description/price
8. Add hover effect on items
9. Make responsive (single column mobile)
10. Optional: add category filter tabs

## Menu Sample Data
### Coffee
- Espresso - $3.50
- Americano - $4.00
- Cappuccino - $4.50
- Latte - $5.00
- Cold Brew - $4.50

### Tea
- Earl Grey - $3.50
- Matcha Latte - $5.50
- Chai Latte - $5.00

### Pastries
- Croissant - $4.00
- Blueberry Muffin - $3.50
- Cinnamon Roll - $4.50

### Light Bites
- Avocado Toast - $8.00
- Granola Bowl - $7.00

## Todo List
- [ ] Add menu HTML structure
- [ ] Add category containers
- [ ] Add sample menu items
- [ ] Create menu.css
- [ ] Style category headers
- [ ] Style menu item cards
- [ ] Style price display
- [ ] Add hover effects
- [ ] Mobile responsive layout
- [ ] Optional: category tabs

## Success Criteria
- All categories display correctly
- Prices clearly visible
- Items scannable at glance
- Works on all breakpoints

## Risk Assessment
| Risk | Impact | Mitigation |
|------|--------|------------|
| Too many items | Med | Limit to highlights |
| Layout breaks | Med | Test all breakpoints |

## Security Considerations
- Static data, no concerns

## Next Steps
Proceed to [Phase 06: Gallery Section](./phase-06-gallery-section.md)
