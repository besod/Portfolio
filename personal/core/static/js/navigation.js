// Get the current URL path
const path = window.location.pathname;

// Find the navigation links
const links = document.querySelectorAll(".nav-link");

// Loop through the links and check if the link's href matches the current path
links.forEach((link) => {
  if (link.getAttribute("href") === path) {
    link.classList.add("active"); // Add a class to highlight the active link
  }
});
