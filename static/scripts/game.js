function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

const quest = document.querySelector('.quest');

function generateExample(event) {
  const level = document.querySelector('.level').textContent;
  const clas = level[7];
  const difficulty = level[9]
    if ('5' === clas) {
      if ('1' === difficulty) {
        let number_one = getRandomInt(10)
        let number_two = getRandomInt(10)
        quest.innerHTML = String(number_one) + ' + ' + String(number_two) + ' = ?';
      }

  }
}

generateExample()