const addTodoBtn = document.querySelector('.todoButton')
var emoji = String.fromCodePoint(0x2705)



const todoTextField = document.querySelector(".inputField")

todoTextField.setAttribute('data-testid','eval-input-field')

function addTodo() {
    const todoList = document.querySelector("#todoList")
    const todoText = document.querySelector(".inputField").value
    const todoTextField = document.querySelector(".inputField")
    const todoEntry = document.createElement('div')
    todoEntry.classList.add('todoEntry')
    const todoEntryText = document.createElement('div')
    todoEntryText.classList.add('todoEntryText')
    const todoEntryButton = document.createElement('button')
    todoEntryButton.classList.add('todoEntryButton')
    todoEntryButton.textContent = emoji;
    todoEntryText.textContent = todoText
    todoEntry.appendChild(todoEntryText)
    todoEntry.appendChild(todoEntryButton)
    todoList.prepend(todoEntry)
    todoTextField.value = ""
    }
// function removeTodo(){
//     const todoEntryButtons
// }

addTodoBtn.addEventListener('click', addTodo);
