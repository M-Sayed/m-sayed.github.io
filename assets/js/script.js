// Calculate dynamic years of experience
function updateYearsOfExperience() {
    const startDate = new Date('2016-08-01'); // August 2016
    const currentDate = new Date();

    // Calculate the difference in milliseconds
    const diffInMs = currentDate - startDate;

    // Convert to years and round down
    const yearsOfExperience = Math.floor(diffInMs / (365.25 * 24 * 60 * 60 * 1000));

    // Update all elements with id="years-experience"
    const yearsElements = document.querySelectorAll('#years-experience');
    yearsElements.forEach(element => {
        element.textContent = yearsOfExperience + '+';
    });
}

// Update years when page loads
document.addEventListener('DOMContentLoaded', updateYearsOfExperience);

// Mobile menu functionality
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');
const navLinks = document.querySelectorAll('.nav-link');

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
});

navLinks.forEach(link => {
    link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
    });
});

// Smooth scrolling for navigation links (only for hash links)
navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        const href = link.getAttribute('href');

        // Only prevent default for hash links (internal navigation)
        if (href.startsWith('#')) {
            e.preventDefault();
            const targetSection = document.querySelector(href);
            if (targetSection) {
                const navHeight = document.querySelector('.navbar').offsetHeight;
                const targetPosition = targetSection.offsetTop - navHeight;
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        }
        // Let external links (like blog.html) navigate normally
    });
});

// Active navigation link on scroll
const sections = document.querySelectorAll('section');
const navHeight = document.querySelector('.navbar').offsetHeight;

function updateActiveNavLink() {
    const scrollPosition = window.scrollY + navHeight + 100;

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.offsetHeight;
        const sectionId = section.getAttribute('id');

        if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${sectionId}`) {
                    link.classList.add('active');
                }
            });
        }
    });
}

window.addEventListener('scroll', updateActiveNavLink);
window.addEventListener('load', updateActiveNavLink);

// Fade in animation on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const fadeInObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            fadeInObserver.unobserve(entry.target);
        }
    });
}, observerOptions);

// Add fade-in class to elements
document.addEventListener('DOMContentLoaded', () => {
    const elementsToFade = [
        '.about-content',
        '.timeline-item',
        '.skill-category',
        '.project-card',
        '.contact-content'
    ];

    elementsToFade.forEach(selector => {
        const elements = document.querySelectorAll(selector);
        elements.forEach(element => {
            element.classList.add('fade-in');
            fadeInObserver.observe(element);
        });
    });
});

// Typing effect for hero title (optional enhancement)
const heroTitle = document.querySelector('.hero-title');
const originalText = heroTitle.textContent;
heroTitle.textContent = '';
let charIndex = 0;

function typeText() {
    if (charIndex < originalText.length) {
        heroTitle.textContent += originalText.charAt(charIndex);
        charIndex++;
        setTimeout(typeText, 50);
    }
}

// Start typing effect after page load
window.addEventListener('load', () => {
    setTimeout(typeText, 500);
});

// Navbar background on scroll
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.style.background = 'rgba(255, 255, 255, 0.98)';
        navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
    } else {
        navbar.style.background = 'rgba(255, 255, 255, 0.95)';
        navbar.style.boxShadow = '0 1px 3px rgba(0, 0, 0, 0.1)';
    }
});

// Parallax effect for hero section (subtle)
const hero = document.querySelector('.hero');

window.addEventListener('scroll', () => {
    const scrolled = window.scrollY;
    const rate = scrolled * -0.5;
    hero.style.transform = `translateY(${rate}px)`;
});
