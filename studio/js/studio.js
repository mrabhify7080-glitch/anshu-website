/* ==========================================================================
   Anshu Properties — Content Creation & Digital Studio JavaScript
   Shared interactive behaviors (Navigation, Accordions, Contact)
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  // Mobile Navigation Drawer Toggle
  const menuToggle = document.getElementById('menu-toggle');
  const navMobile = document.getElementById('nav-mobile');

  if (menuToggle && navMobile) {
    menuToggle.addEventListener('click', () => {
      const isVisible = navMobile.style.display === 'block';
      navMobile.style.display = isVisible ? 'none' : 'block';
      menuToggle.setAttribute('aria-expanded', !isVisible);
    });
  }

  // FAQ Accordions
  const faqQuestions = document.querySelectorAll('.faq-question');
  faqQuestions.forEach(question => {
    question.addEventListener('click', () => {
      const currentItem = question.closest('.faq-item');
      const isOpen = currentItem.classList.contains('active');

      // Close all items in the same container
      const parentWrap = currentItem.closest('.faq-wrap') || document;
      parentWrap.querySelectorAll('.faq-item').forEach(item => {
        item.classList.remove('active');
        const btn = item.querySelector('.faq-question');
        if (btn) btn.setAttribute('aria-expanded', 'false');
      });

      // Toggle current item
      if (!isOpen) {
        currentItem.classList.add('active');
        question.setAttribute('aria-expanded', 'true');
      }
    });
  });
});

// Enquiry Form Handler (WhatsApp Integration)
function handleStudioEnquiry(event) {
  event.preventDefault();

  const name = document.getElementById('client-name')?.value.trim() || '';
  const business = document.getElementById('business-name')?.value.trim() || '';
  const email = document.getElementById('client-email')?.value.trim() || '';
  const industry = document.getElementById('client-industry')?.value || 'Not Specified';
  const service = document.getElementById('service-interest')?.value || 'General Content';
  const budget = document.getElementById('budget-range')?.value || 'Introductory';
  const notes = document.getElementById('project-notes')?.value.trim() || '';

  const message = `Hi Anshu Properties, I want to discuss a Content Project.\n\n` +
                  `*Name:* ${name}\n` +
                  `*Business/Brand:* ${business}\n` +
                  `*Email:* ${email}\n` +
                  `*Industry:* ${industry}\n` +
                  `*Service Required:* ${service}\n` +
                  `*Budget Tier:* ${budget}\n` +
                  (notes ? `*Project Details:* ${notes}\n` : '') +
                  `\nPlease share availability and next steps.`;

  const waUrl = `https://wa.me/918303727724?text=${encodeURIComponent(message)}`;
  window.open(waUrl, '_blank');
}
