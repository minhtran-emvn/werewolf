/**
 * ===================================
 * Brew & Bloom - Main JavaScript
 * ===================================
 */

// Wait for DOM to be ready
document.addEventListener('DOMContentLoaded', () => {
    console.log('🌿 Brew & Bloom loaded successfully!');
    
    // Initialize navigation
    initNavigation();
    
    // Initialize smooth scroll
    initSmoothScroll();
    
    // Initialize scroll animations (placeholder for Phase 9)
    initScrollAnimations();
});

/**
 * Navigation functionality
 */
function initNavigation() {
    const navToggle = document.querySelector('.nav-toggle');
    const navLinks = document.querySelector('.nav-links');
    
    if (!navToggle || !navLinks) return;
    
    // Mobile menu toggle
    navToggle.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        navToggle.classList.toggle('active');
    });
    
    // Close mobile menu on link click
    navLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
            navToggle.classList.remove('active');
        });
    });
    
    // Navbar scroll effect
    let lastScroll = 0;
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > 100) {
            navbar.style.boxShadow = 'var(--shadow-lg)';
        } else {
            navbar.style.boxShadow = 'var(--shadow-md)';
        }
        
        lastScroll = currentScroll;
    });
}

/**
 * Smooth scroll for anchor links
 */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href === '#') return;
            
            e.preventDefault();
            const target = document.querySelector(href);
            
            if (target) {
                const offsetTop = target.offsetTop - 80; // Account for fixed navbar
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
}

/**
 * Scroll animations (placeholder for Phase 9)
 */
function initScrollAnimations() {
    // Will be implemented in Phase 9 - Responsive Polish
    // This will add fade-in animations as sections come into view
    console.log('Scroll animations ready (Phase 9)');
}

/**
 * Utility: Debounce function
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Utility: Throttle function
 */
function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}
