import { useState } from "react";
import TodoField from "./components/TodoField";
import Todo from "./components/Todo";
import "./App.css";
import Heading from "./components/Heading";
function App() {
  let todos = [];
  return (
    <div id="content">
      <Heading></Heading>
      <TodoField />
      <div data-testid="email">avdalim@outlook.com</div>
    </div>
  );
}

export default App;
