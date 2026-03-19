# Phase 08: Contact Section

## Context Links
- [Main Plan](./plan.md)
- [Phase 07: Location](./phase-07-location-hours-section.md)

## Overview
- **Priority:** Medium
- **Status:** pending
- **Effort:** 1h

Contact form and social links for customer inquiries.

## Key Insights
- Simple form: name, email, message
- Static site = use Formspree/Netlify Forms or mailto
- Include social media links

## Requirements

### Functional
- Section heading "Get in Touch"
- Contact form (name, email, message)
- Form submission handling
- Social media links (Instagram, Facebook)
- Email/phone direct links

### Non-Functional
- Form validation (HTML5)
- Accessible form labels
- Clear submission feedback

## Architecture
```html
<section id="contact" class="contact">
  <div class="container">
    <h2>Get in Touch</h2>
    <div class="contact__grid">
      <form class="contact__form" action="..." method="POST">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email</label>
        <input type="email" id="email" name="email" required>

        <label for="message">Message</label>
        <textarea id="message" name="message" rows="5" required></textarea>

        <button type="submit" class="btn btn-primary">Send Message</button>
      </form>
      <div class="contact__info">
        <p>Email: hello@brewandbloom.com</p>
        <p>Phone: (503) 555-BREW</p>
        <div class="contact__social">
          <a href="#">Instagram</a>
          <a href="#">Facebook</a>
        </div>
      </div>
    </div>
  </div>
</section>
```

## Related Code Files
- Modify: `index.html` (contact section)
- Create: `css/sections/contact.css`
- Modify: `js/main.js` (optional form handling)

## Implementation Steps
1. Add contact section HTML
2. Create form with all fields
3. Add labels with for/id association
4. Add HTML5 validation (required, type=email)
5. Add social links container
6. Create contact.css
7. Style form inputs and labels
8. Style submit button
9. Style social links
10. Set up form action (Formspree recommended)
11. Add focus states for accessibility

## Form Handling Options
1. **Formspree** (free tier): action="https://formspree.io/f/xxx"
2. **Netlify Forms**: add netlify attribute
3. **Mailto fallback**: action="mailto:hello@brewandbloom.com"

## Todo List
- [ ] Add contact HTML structure
- [ ] Create form with fields
- [ ] Add proper labels
- [ ] Add HTML5 validation
- [ ] Add social links
- [ ] Create contact.css
- [ ] Style form inputs
- [ ] Style textarea
- [ ] Style submit button
- [ ] Style social links
- [ ] Set up form action
- [ ] Test form submission

## Success Criteria
- Form validates before submit
- All fields have labels
- Form submits successfully
- Social links work
- Accessible via keyboard

## Risk Assessment
| Risk | Impact | Mitigation |
|------|--------|------------|
| Spam submissions | Med | Use Formspree/honeypot |
| Form not working | High | Test before deploy |

## Security Considerations
- No backend = use trusted form service
- HTTPS required for form data
- Honeypot field for spam prevention

## Next Steps
Proceed to [Phase 09: Responsive Polish](./phase-09-responsive-polish.md)
