"use strict";

const DATA_URL = "./data/projets.json";
const requiredText = ["id", "title", "category", "level", "description", "activity", "deliverable", "question", "answer"];
const state = { resources: [], category: "Toutes" };
const statusNode = document.querySelector("#status");
const resourcesGrid = document.querySelector("#resources-grid");
const flashcardsGrid = document.querySelector("#flashcards-grid");
const filtersNode = document.querySelector("#filters");
const previewNode = document.querySelector("#json-preview");
const retryButton = document.querySelector("#retry-button");
const networkStatus = document.querySelector("#network-status");

function setStatus(message, type = "info") {
  statusNode.textContent = message;
  statusNode.className = type === "error" ? "status error" : "status";
  statusNode.setAttribute("role", type === "error" ? "alert" : "status");
  retryButton.hidden = type !== "error";
}

function updateNetworkStatus() {
  const online = navigator.onLine;
  networkStatus.textContent = online ? "Navigateur en ligne" : "Navigateur hors connexion";
  networkStatus.className = online ? "network" : "network offline";
}

function isAllowedLink(value) {
  if (!value) return true;
  try {
    const url = new URL(value, window.location.href);
    return ["http:", "https:"].includes(url.protocol);
  } catch {
    return false;
  }
}

function validateResources(value) {
  if (!Array.isArray(value)) throw new Error("La réponse reçue n’est pas un tableau.");
  const ids = new Set();
  value.forEach((item, index) => {
    if (!item || typeof item !== "object") throw new Error(`Objet ${index + 1} invalide.`);
    requiredText.forEach(key => {
      if (typeof item[key] !== "string" || !item[key].trim()) throw new Error(`Objet ${index + 1} : champ ${key} absent ou invalide.`);
    });
    if (!Array.isArray(item.objectives) || item.objectives.some(x => typeof x !== "string" || !x.trim())) throw new Error(`Objet ${index + 1} : objectifs invalides.`);
    if (ids.has(item.id)) throw new Error(`Identifiant dupliqué : ${item.id}.`);
    if (!/^[a-z0-9-]+$/.test(item.id)) throw new Error(`Identifiant non autorisé : ${item.id}.`);
    if (!isAllowedLink(item.link)) throw new Error(`Protocole de lien refusé dans ${item.id}.`);
    ids.add(item.id);
  });
  return value;
}

function makeText(tag, text, className = "") {
  const node = document.createElement(tag);
  node.textContent = text;
  if (className) node.className = className;
  return node;
}

function createCard(item) {
  const card = document.createElement("article");
  card.className = "card";
  card.append(makeText("span", item.category, "tag"), makeText("h3", item.title), makeText("p", item.description));
  const meta = makeText("p", `${item.level} · ${item.deliverable}`, "hint");
  const list = document.createElement("ul");
  item.objectives.forEach(value => list.append(makeText("li", value)));
  card.append(meta, list, makeText("p", `Activité : ${item.activity}`));
  if (item.link) {
    const link = document.createElement("a");
    link.href = item.link;
    link.textContent = "Ressource complémentaire";
    link.target = "_blank";
    link.rel = "noopener noreferrer";
    card.append(link);
  }
  return card;
}

function createFlashcard(item) {
  const card = document.createElement("article");
  card.className = "flashcard";
  const button = document.createElement("button");
  const answer = makeText("div", item.answer, "answer");
  const answerId = `answer-${item.id}`;
  button.type = "button";
  button.textContent = item.question;
  button.setAttribute("aria-expanded", "false");
  button.setAttribute("aria-controls", answerId);
  answer.id = answerId;
  answer.hidden = true;
  answer.setAttribute("aria-hidden", "true");
  button.addEventListener("click", () => {
    const open = button.getAttribute("aria-expanded") === "true";
    button.setAttribute("aria-expanded", String(!open));
    answer.hidden = open;
    answer.setAttribute("aria-hidden", String(open));
  });
  card.append(button, answer);
  return card;
}

function visibleResources() {
  return state.category === "Toutes" ? state.resources : state.resources.filter(item => item.category === state.category);
}

function render() {
  const items = visibleResources();
  resourcesGrid.replaceChildren();
  flashcardsGrid.replaceChildren();
  items.forEach(item => {
    resourcesGrid.append(createCard(item));
    flashcardsGrid.append(createFlashcard(item));
  });
  resourcesGrid.setAttribute("aria-busy", "false");
  if (!items.length) setStatus("Aucune ressource à afficher pour ce scénario.");
  else setStatus(`${items.length} ressource${items.length > 1 ? "s" : ""} affichée${items.length > 1 ? "s" : ""}.`);
}

function renderFilters() {
  const categories = ["Toutes", ...new Set(state.resources.map(item => item.category))];
  filtersNode.replaceChildren();
  categories.forEach(category => {
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = category;
    button.setAttribute("aria-pressed", String(category === state.category));
    button.addEventListener("click", () => {
      state.category = category;
      renderFilters();
      render();
    });
    filtersNode.append(button);
  });
}

async function fetchJson(url) {
  const response = await fetch(url, { cache: "no-store" });
  if (!response.ok) throw new Error(`Erreur HTTP ${response.status} — ${response.statusText || "ressource indisponible"}.`);
  return response.json();
}

async function loadResources() {
  resourcesGrid.setAttribute("aria-busy", "true");
  setStatus("Chargement des données JSON…");
  try {
    const data = validateResources(await fetchJson(DATA_URL));
    state.resources = data;
    state.category = "Toutes";
    previewNode.textContent = JSON.stringify(data, null, 2);
    renderFilters();
    render();
  } catch (error) {
    state.resources = [];
    resourcesGrid.replaceChildren();
    flashcardsGrid.replaceChildren();
    filtersNode.replaceChildren();
    resourcesGrid.setAttribute("aria-busy", "false");
    previewNode.textContent = error.message;
    setStatus(error.message, "error");
  }
}

async function runScenario() {
  resourcesGrid.setAttribute("aria-busy", "true");
  setStatus("Exécution du scénario…");
  try {
    const choice = document.querySelector("#scenario").value;
    let data;
    if (choice === "404") data = await fetchJson("./data/fichier-manquant.json");
    else if (choice === "invalid-json") data = JSON.parse('{"message": "guillemet non fermé}');
    else data = structuredClone(await fetchJson(DATA_URL));
    if (choice === "empty") data = [];
    if (choice === "not-array") data = { message: "Cette réponse est un objet." };
    if (choice === "schema" && data[0]) delete data[0].question;
    if (choice === "dangerous" && data[0]) data[0].link = "javascript:alert(1)";
    state.resources = validateResources(data);
    state.category = "Toutes";
    previewNode.textContent = JSON.stringify(data, null, 2);
    renderFilters();
    render();
  } catch (error) {
    state.resources = [];
    resourcesGrid.replaceChildren();
    flashcardsGrid.replaceChildren();
    filtersNode.replaceChildren();
    resourcesGrid.setAttribute("aria-busy", "false");
    previewNode.textContent = error.message;
    setStatus(error.message, "error");
  }
}

async function testPhp() {
  const node = document.querySelector("#api-status");
  node.textContent = "Test de api.php…";
  node.className = "status";
  try {
    const response = await fetch("./api.php", { cache: "no-store" });
    if (!response.ok) throw new Error(`Erreur HTTP ${response.status}.`);
    const type = response.headers.get("content-type") || "";
    if (!type.includes("application/json")) throw new Error("Le serveur ne semble pas interpréter PHP : réponse JSON absente.");
    const data = await response.json();
    node.textContent = data.message || "Réponse PHP reçue.";
  } catch (error) {
    node.textContent = `${error.message} Utilisez un serveur PHP pour cette démonstration facultative.`;
    node.className = "status error";
  }
}

document.querySelector("#reload-button").addEventListener("click", loadResources);
retryButton.addEventListener("click", loadResources);
document.querySelector("#run-scenario").addEventListener("click", runScenario);
document.querySelector("#test-api").addEventListener("click", testPhp);
window.addEventListener("online", updateNetworkStatus);
window.addEventListener("offline", updateNetworkStatus);
updateNetworkStatus();
loadResources();
