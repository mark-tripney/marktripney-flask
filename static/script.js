buttonContent = (theme) => {
  if (theme === "light") {
    btn.textContent = "Dark";
  } else {
    btn.textContent = "Light";
  }
}

// Select the button
const btn = document.getElementById("toggle-mode");
// Select the theme preference from localStorage
const currentTheme = localStorage.getItem("theme");
// If the current theme in localStorage is "dark"...
if (currentTheme === "dark") {
  // ...then use the .dark-theme class
  document.body.classList.add("dark-theme");
  btn.textContent = "Light"
}

// Listen for a click on the button
btn.addEventListener("click", function () {
  // Toggle the .dark-theme class on each click
  document.body.classList.toggle("dark-theme");
  // Let's say the theme is equal to light
  let theme = "light";
  // If the body contains the .dark-theme class...
  if (document.body.classList.contains("dark-theme")) {
    // ...then let's make the theme dark
    theme = "dark";
  }
  buttonContent(theme)
  // Then save the choice in localStorage
  localStorage.setItem("theme", theme);
});