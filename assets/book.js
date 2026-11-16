"use strict";

const reader = document.documentElement;
const controls = document.querySelector(".controls");
const theme = document.querySelector("#theme-toggle");
const textSize = document.querySelector("#text-toggle");
const search = document.querySelector("#course-search");
const feedback = document.querySelector("#search-feedback");
const solutions = [...document.querySelectorAll(".prose details")].filter(
  (item) => item.classList.contains("solution") ||
    /solution|answer/i.test(item.querySelector("summary")?.textContent ?? ""),
);
const solutionButton = document.querySelector("#solutions-toggle");

function preference(name, value) {
  try {
    const key = `applied-thermodynamics-${name}`;
    if (value !== undefined) localStorage.setItem(key, value);
    return localStorage.getItem(key);
  } catch {
    // Some browsers disable persistent storage for documents opened from disk.
    return null;
  }
}

function setTheme(value) {
  reader.dataset.theme = value;
  theme.textContent = value === "dark" ? "Light theme" : "Dark theme";
}

function setTextSize(large) {
  reader.classList.toggle("large-text", large);
  textSize.setAttribute("aria-pressed", String(large));
  textSize.textContent = large ? "Default text" : "Larger text";
}

function syncSolutionLabel() {
  solutionButton.textContent = solutions.every((item) => item.open)
    ? "Collapse solutions"
    : "Expand solutions";
}

setTheme(preference("theme") === "light" ? "light" : "dark");
setTextSize(preference("large-text") === "true");
controls.hidden = false;

theme.addEventListener("click", () => {
  const value = reader.dataset.theme === "dark" ? "light" : "dark";
  setTheme(value);
  preference("theme", value);
});
textSize.addEventListener("click", () => {
  const large = !reader.classList.contains("large-text");
  setTextSize(large);
  preference("large-text", String(large));
});
document.querySelector("#print-page").addEventListener("click", () => window.print());

if (solutions.length) {
  solutionButton.hidden = false;
  syncSolutionLabel();
  solutionButton.addEventListener("click", () => {
    const expand = solutions.some((item) => !item.open);
    solutions.forEach((item) => { item.open = expand; });
    syncSolutionLabel();
  });
  solutions.forEach((item) => item.addEventListener("toggle", syncSolutionLabel));
}

let printStates = [];
window.addEventListener("beforeprint", () => {
  printStates = solutions.map((item) => item.open);
  solutions.forEach((item) => { item.open = true; });
});
window.addEventListener("afterprint", () => {
  solutions.forEach((item, index) => { item.open = printStates[index] ?? item.open; });
  printStates = [];
});

if (window.matchMedia("(max-width: 52rem)").matches) {
  document.querySelectorAll(".side-panel").forEach((panel) => { panel.open = false; });
}

if (search) {
  const rows = [...document.querySelectorAll("[data-chapter]")];
  const searchable = rows.map((row) => row.textContent.toLowerCase());
  search.closest(".search").hidden = false;
  search.addEventListener("input", () => {
    const query = search.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
    let count = 0;
    rows.forEach((row, index) => {
      const match = query.every((word) => searchable[index].includes(word));
      row.hidden = !match;
      if (match) count += 1;
    });
    feedback.textContent = query.length
      ? `${count} matching ${count === 1 ? "chapter" : "chapters"}`
      : "";
  });
}
