---
layout: default
title: Contact
permalink: /contact/
---

# Contact Me

<form id="contact-form">
  <input type="text" name="name" placeholder="Your Name" required />
  <input type="email" name="email" placeholder="Your Email" required />
  <textarea name="message" placeholder="Your Message" required></textarea>
  <button type="submit">Send</button>
  <p id="status-message"></p>
</form>

<script>
  const form = document.getElementById('contact-form');
  const status = document.getElementById('status-message');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const data = {
      name: form.name.value,
      email: form.email.value,
      message: form.message.value,
    };

    const res = await fetch('http://localhost:5000/send-email', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    });

    const result = await res.json();
    if (res.ok) {
      status.textContent = result.success;
      form.reset();
    } else {
      status.textContent = `Error: ${result.error}`;
    }
  });
</script>
