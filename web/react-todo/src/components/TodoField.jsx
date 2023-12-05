import { useState } from "react";
import Todo from "./Todo";

function TodoField() {
  let todos = [];
  // click of the button
  const [todo, setTodo] = useState("");
  // Text from input
  const [text, setText] = useState("");
  // List of todos
  const [items, setItems] = useState([]);

  function deleteTodo(id) {
    setItems(items.filter((item) => item !== id));
  }

  function handleClick() {
    let inputText = text;
    console.log(text);
    setItems((prevList) => [...prevList, inputText]);
    // <Todo text={inputText} onClick={() => deleteTodo({ inputText })} />,
    // setItems((prevList)=>[...prevList,{{inputText}})
    setText("");
  }

  return (
    <>
      {items.map((todo, index) => {
        return (
          <Todo
            key={todo}
            id={todo}
            text={todo}
            onClick={() => deleteTodo(todo)}
          />
        );
      })}
      <div className="todoField">
        {/* <button className="todoButton" onClick={console.log("CLicked")}>
        {" "}
        &#10133;
      </button> */}
        <input
          type="text"
          className="inputField"
          placeholder="Enter new Todo"
          data-testid="eval-input-field"
          value={text}
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
