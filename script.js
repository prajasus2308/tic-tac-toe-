const boardEl = document.getElementById("board");
const statusEl = document.getElementById("status");
const startBtn = document.getElementById("startBtn");
const resetBtn = document.getElementById("resetBtn");

let board = Array(9).fill(null);
let current = "X";
let gameOver = false;
let playerNames = { X: "Player X", O: "Player O" };

const wins = [
  [0,1,2],[3,4,5],[6,7,8],
  [0,3,6],[1,4,7],[2,5,8],
  [0,4,8],[2,4,6]
];

function startGame() {
  const nameX = document.getElementById("playerX").value.trim();
  const nameO = document.getElementById("playerO").value.trim();
  if (nameX) playerNames.X = nameX;
  if (nameO) playerNames.O = nameO;
  resetGame();
  statusEl.textContent = `${playerNames[current]}'s turn`;
}

function render() {
  boardEl.innerHTML = "";
  board.forEach((val, i) => {
    const cell = document.createElement("div");
    cell.className = "cell";
    cell.textContent = val ? val : "";
    cell.addEventListener("click", () => handleClick(i));
    boardEl.appendChild(cell);
  });
}

function checkWinner() {
  for (const [a,b,c] of wins) {
    if (board[a] && board[a] === board[b] && board[a] === board[c]) {
      return board[a];
    }
  }
  return null;
}

function checkDraw() {
  return board.every(v => v !== null);
}

function handleClick(i) {
  if (gameOver || board[i]) return;
  board[i] = current;
  const winner = checkWinner();
  if (winner) {
    gameOver = true;
    statusEl.textContent = `${playerNames[winner]} wins!`;
  } else if (checkDraw()) {
    gameOver = true;
    statusEl.textContent = "It's a draw.";
  } else {
    current = current === "X" ? "O" : "X";
    statusEl.textContent = `${playerNames[current]}'s turn`;
  }
  render();
}

function resetGame() {
  board = Array(9).fill(null);
  current = "X";
  gameOver = false;
  render();
}

// Event listeners
startBtn.addEventListener("click", startGame);
resetBtn.addEventListener("click", resetGame);

// Initial render
render();
