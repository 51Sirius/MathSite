const quest = document.querySelector('.quest')
quest.innerHTML = String(getRandomInt(10)) + ' + ' + String(getRandomInt(10)) + ' = ?';


function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}