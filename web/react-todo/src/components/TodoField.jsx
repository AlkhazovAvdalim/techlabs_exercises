import { useState } from "react";
import Todo from "./Todo";

function TodoField() {
  let todos = [];
  // Click of the button from the input field
  const [todo, setTodo] = useState("");
  // Text from input
  const [text, setText] = useState("");
  // Keeps track of todos, is a list with the todo entries, which gets updated with added todos
  const [items, setItems] = useState([]);

  function deleteTodo(id) {
    // Handles the click, when the done button click is clicked, filters all the todos
    // except the one clicked
    setItems(items.filter((item) => item !== id));
  }

  function handleClick() {
    let inputText = text;
    console.log(text);
    // Takes the items from the previous list and adds the inputted text to the list
    setItems((prevList) => [...prevList, inputText]);
    setText("");
  }

  return (
    <>
      {/* The List gets taken, iterated on and passed on to the constructor of the object
    The deleteTodo function is also mapped onto the todo id */}
      {items.map((todo, index) => {
        return (
          <Todo
            key={todo}
            id={todo}
            text={todo}
            // () => is necessary here as otherwise the todo is directly deleted.
            // () => leads to the function being activated on click and not directly on lead
            onClick={() => deleteTodo(todo)}
          />
        );
      })}
      <div className="todoField">
        <input
          type="text"
          className="inputField"
          placeholder="Enter new Todo"
          data-testid="eval-input-field"
          value={text}
          // Changes the Text state, will be then added to list and deleted from input field on click
          onChange={(e) => setText(e.target.value)}
        ></input>
        <button data-testid="eval-add-todo-button" onClick={handleClick}>
          ➕
        </button>
      </div>
    </>
  );
}

export default TodoField;
