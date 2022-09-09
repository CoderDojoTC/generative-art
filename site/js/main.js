const card = document.querySelector(".card__inner");

card.addEventListener("click", function (e) {
  //alert('hi')
  card.classList.toggle('is-flipped');
});