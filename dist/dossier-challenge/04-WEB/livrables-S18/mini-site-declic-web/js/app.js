"use strict";
// Le comportement est séparé du contenu HTML et de sa présentation CSS.
const explainButton = document.querySelector("#explain-button");
const explanation = document.querySelector("#event-explanation");
if (explainButton && explanation) {
  explainButton.addEventListener("click", () => {
    const expanded = explainButton.getAttribute("aria-expanded") === "true";
    explainButton.setAttribute("aria-expanded", String(!expanded));
    explanation.hidden = expanded;
    explainButton.textContent = expanded ? "Afficher l’explication" : "Masquer l’explication";
  });
}
const posterDialog = document.querySelector("#poster-dialog");
const posterOpen = document.querySelector("#poster-open");
const posterClose = document.querySelector("#poster-close");
if (posterDialog && posterOpen && posterClose) {
  posterOpen.addEventListener("click", () => posterDialog.showModal());
  posterClose.addEventListener("click", () => posterDialog.close());
  posterDialog.addEventListener("close", () => posterOpen.focus());
}
// Le score sert ? réviser, sans validation automatique du pilote.
const quizForm = document.querySelector("#quiz-form");
const corrections = [
 { answer:"0", text:"HTML organise le titre et les paragraphes dans index.html." },
 { answer:"1", text:"CSS règle les couleurs et la disposition dans css/styles.css." },
 { answer:"0", text:"JavaScript écoute le clic et change l’état de la zone dans js/app.js." }
];
if (quizForm) {
 const clear = () => corrections.forEach((_,i) => { document.querySelector("#feedback-"+i).hidden=true; });
 quizForm.addEventListener("submit", event => {
  event.preventDefault(); const responses=new FormData(quizForm); let score=0, answered=0;
  corrections.forEach((c,i) => {
   const response=responses.get("q"+i), correct=response===c.answer;
   if(response!==null) answered++; if(correct) score++;
   const feedback=document.querySelector("#feedback-"+i); feedback.hidden=false;
   feedback.textContent=(response===null?"Non renseigné. ":correct?"Bonne réponse. ":"À reprendre. ")+c.text;
  });
  document.querySelector("#quiz-result").textContent=`${score} / 3 · ${answered} question(s) renseignée(s). Relisez les explications.`;
 });
 quizForm.addEventListener("reset",()=>{document.querySelector("#quiz-result").textContent="";clear();});
 quizForm.addEventListener("change",()=>{document.querySelector("#quiz-result").textContent="Réponses modifiées : corrigez à nouveau votre essai.";clear();});
}
