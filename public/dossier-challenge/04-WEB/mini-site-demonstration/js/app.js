"use strict";

const explanationButton = document.querySelector("#explain-button");
const explanationPanel = document.querySelector("#event-explanation");

if (explanationButton && explanationPanel) {
  explanationButton.addEventListener("click", () => {
    const isOpen = explanationButton.getAttribute("aria-expanded") === "true";
    explanationButton.setAttribute("aria-expanded", String(!isOpen));
    explanationButton.textContent = isOpen ? "Afficher l’explication" : "Masquer l’explication";
    explanationPanel.hidden = isOpen;

    console.info(
      `[Séance 17] Événement clic observé. Zone explicative ${isOpen ? "masquée" : "affichée"}.`
    );
  });
}

// Affiche de séance : ouverture accessible de la miniature dans une fenêtre agrandie.
const posterDialog = document.querySelector("#poster-dialog");
const posterOpenButton = document.querySelector("#poster-open");
const posterCloseButton = document.querySelector("#poster-close");

if (posterDialog && posterOpenButton && posterCloseButton) {
  posterOpenButton.addEventListener("click", () => {
    if (typeof posterDialog.showModal === "function") {
      posterDialog.showModal();
      posterCloseButton.focus();
    }
  });

  posterCloseButton.addEventListener("click", () => {
    posterDialog.close();
    posterOpenButton.focus();
  });

  posterDialog.addEventListener("click", (event) => {
    if (event.target === posterDialog) {
      posterDialog.close();
      posterOpenButton.focus();
    }
  });
}
