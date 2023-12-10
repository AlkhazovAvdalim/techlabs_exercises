import { useState } from "react";
// Function is passed into the component
function Todo({ text, id, onClick }) {
  const [todo, setTodo] = useState("");
  // Here is the function
  function handleClick() {}
  return (
    <div data-testid={id} key={id} className="todoEntry">
      <p className="todoEntryText">{text}</p>
      <button
        data-testid={"eval-item-done-" + id}
        className="todoEntryButton"
        // Function defined from parent and passed via Props
        onClick={onClick}
      >
        ✅
      </button>
    </div>
  );
}

export default Todo;
