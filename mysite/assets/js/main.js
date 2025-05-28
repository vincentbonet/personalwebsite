document.addEventListener("DOMContentLoaded", () => {
  gsap.from(".container", {
    opacity: 0,
    y: 50,
    duration: 1.2,
    ease: "power3.out"
  });

  gsap.from(".navbar", {
    y: -80,
    duration: 0.8,
    ease: "power2.out"
  });

  barba.init({
    transitions: [{
      name: 'fade',
      leave(data) {
        return gsap.to(data.current.container, {
          opacity: 0,
          duration: 0.5
        });
      },
      enter(data) {
        return gsap.from(data.next.container, {
          opacity: 0,
          duration: 0.5
        });
      }
    }]
  });
});
