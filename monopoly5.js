//Dice Roll
function rollDice(){
    const diceResult = document.getElementById("diceResult");
    const diceImages = document.getElementById("diceImages");
    const values = [];
    const images = [];

    for (let i = 0; i < 2; i++){
        const value = Math.floor(Math.random() * 6)+1
        values.push(value)
        images.push(`<img src="git_monopoly_images/dice (${value}).png" alt="Dice ${value}">`)
    }

    diceResult.textContent = `dice: ${values.join(', ')}`
    diceImages.innerHTML = images.join(' ');
}

// Players Setup
const numPlayersInput = document.getElementById('numPlayers');
const playerNamesDiv = document.getElementById('playerNames');
const myBoardDiv = document.getElementById('myBoard');
const playerForm = document.getElementById('playerForm');

playerForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const numPlayers = parseInt(numPlayersInput.value);
  playerNamesDiv.innerHTML = '';
  for (let i = 1; i <= numPlayers; i++) {
    const playerNameInput = document.createElement('input');
    playerNameInput.type = 'text';
    playerNameInput.id = `player${i}`;
    playerNameInput.name = `player${i}`;
    const label = document.createElement('label');
    label.textContent = `Player ${i}: `;
    playerNamesDiv.appendChild(label);
    playerNamesDiv.appendChild(playerNameInput);
    playerNamesDiv.appendChild(document.createElement('br'));
  }
  const startGameButton = document.createElement('button');
  startGameButton.type = 'button';
  startGameButton.textContent = 'Start Game';
  playerNamesDiv.appendChild(startGameButton);
  playerNamesDiv.style.display = 'block';
  playerForm.style.display = 'none';
  startGameButton.addEventListener('click', () => {
    const players = [];
    for (let i = 1; i <= numPlayers; i++) {
      const playerNameInput = document.getElementById(`player${i}`);
      players.push(playerNameInput.value);
    }

    // Changing  players to UpperCase

    function uppercaseChars(element,index,array){ 
      array[index] = element.toUpperCase();
    }

    players.forEach(uppercaseChars);

    console.log(players);
    playerNamesDiv.style.display = 'none';
    myBoardDiv.style.display = 'block';
  });
});