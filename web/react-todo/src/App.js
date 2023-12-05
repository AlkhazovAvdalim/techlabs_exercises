import { useState } from "react";
import TodoField from "./components/TodoField";
import Todo from "./components/Todo";
import "./App.css";
function App() {
  let todos = [];
  return (
    <div id="content">
      <TodoField />
      <div data-testid="email">avdalim@outlook.com</div>
    </div>
  );
}

export default App;
