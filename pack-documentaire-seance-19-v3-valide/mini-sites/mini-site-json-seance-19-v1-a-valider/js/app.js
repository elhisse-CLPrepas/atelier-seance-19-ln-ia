"use strict";

const statusElement = document.querySelector("#status");
const projectsElement = document.querySelector("#projects");
const reloadButton = document.querySelector("#reload-button");

function setState(message, type = "info") {
  statusElement.textContent = message;
  statusElement.classList.toggle("error", type === "error");
}

function createProjectCard(project) {
  const article = document.createElement("article");
  article.className = "card";

  const tag = document.createElement("span");
  tag.className = "tag";
  tag.textContent = project.category;

  const title = document.createElement("h3");
  title.textContent = project.title;

  const description = document.createElement("p");
  description.textContent = project.description;

  article.append(tag, title, description);
  return article;
}

async function loadProjects() {
  projectsElement.replaceChildren();
  projectsElement.setAttribute("aria-busy", "true");
  setState("Chargement des projets…");

  try {
    const response = await fetch("./data/projets.json", { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`Réponse HTTP ${response.status}`);
    }

    const projects = await response.json();
    if (!Array.isArray(projects)) {
      throw new Error("Le JSON doit contenir un tableau.");
    }

    projects.forEach((project, index) => {
      if (!project || typeof project !== "object" || Array.isArray(project) ||
          ["title", "category", "description"].some(key => typeof project[key] !== "string" || !project[key].trim())) {
        throw new Error(`Objet ${index + 1} : titre, catégorie et description doivent être des chaînes non vides.`);
      }
    });

    if (projects.length === 0) {
      setState("Aucun projet disponible pour le moment.");
      return;
    }

    const fragment = document.createDocumentFragment();
    projects.forEach((project) => fragment.append(createProjectCard(project)));
    projectsElement.append(fragment);
    setState(`${projects.length} projets chargés avec succès.`);
  } catch (error) {
    console.error("Chargement impossible :", error);
    setState("Impossible de charger les projets. Vérifiez le serveur local, le chemin et le JSON.", "error");
  } finally {
    projectsElement.setAttribute("aria-busy", "false");
  }
}

reloadButton?.addEventListener("click", loadProjects);
loadProjects();
