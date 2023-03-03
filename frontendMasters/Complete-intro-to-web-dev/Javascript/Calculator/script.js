let total = '0';
let operator = ''
let value = '0'
let screenVal = document.querySelector('.screen')

let clear = document.querySelector('.double')
clear.addEventListener('click', function(event){
  screenVal.innerHTML = 0
})

function doMath(symbol){
  if(value === '0')return
  const intVal = parseInt(value)
  if(total === '0') total = intVal
  else{
    if(operator === '+') total += intVal
    else if(operator === '-') total -= intVal
    else if(operator === 'x') total *= intVal
    else total /= intVal
  }
  value = '0'
  operator = symbol
}

function itIsSymbol(symbol){
  switch(symbol){
    case "C":
      value = '0'
      total = '0'
      break
    case "<-":
      if(value.length === 1)value = '0'
      else value = value.substring(0, value.length-1)
      break
    case '÷':
    case '-':
    case '+':
    case 'x':
      doMath(symbol)
      break
  }
}

function handleNumber(v){
  if(value === '0') value = v
  else value += v
}

function checkInt(v){
  if(isNaN(parseInt(v))) itIsSymbol(v)
  else handleNumber(v)
  screenVal.innerHTML = value
}

function buttonClick(value){
  checkInt(value);
}

button = document.querySelector('.calc-button')
button.addEventListener('click', (event) =>{
  buttonClick(event.target.innerText)
})