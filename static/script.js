function toggleDarkMode() {
  document.documentElement.classList.toggle("dark-mode");
  const isDark = document.documentElement.classList.contains("dark-mode");
  localStorage.setItem("theme", isDark ? "dark" : "light");

  const btn = document.getElementById("themeToggleBtn");
  btn.innerText = isDark ? "☀️" : "🌙";
}

// Set icon on load
window.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("themeToggleBtn");
  if (document.documentElement.classList.contains("dark-mode")) {
    btn.innerText = "☀️";
  } else {
    btn.innerText = "🌙";
  }
});
