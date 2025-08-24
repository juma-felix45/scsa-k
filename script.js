// -----------------------------
// Mobile Navbar Toggle Script
// -----------------------------
document.addEventListener("DOMContentLoaded", () => {
  const menuBtn = document.querySelector("#menu-btn");
  const navLinks = document.querySelector(".nav-links");

  // Toggle nav links on button click
  menuBtn.addEventListener("click", () => {
    navLinks.classList.toggle("show");
  });
});
