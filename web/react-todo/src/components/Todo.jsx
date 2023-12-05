import { useState } from "react";

function Todo({ text, id, onClick }) {
  const [todo, setTodo] = useState("");
  function handleClick() {}
  return (
    <div data-testid={id} key={id} className="todoEntry">
      <p className="todoEntryText">{text}</p>
      <button
        data-testid={"eval-item-done-" + id}
        className="todoEntryButton"
        onClick={onClick}
      >
        ✅
      </button>
    </div>
  );
}

export default Todo;
