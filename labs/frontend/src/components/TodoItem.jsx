import React from 'react';

const TodoItem = ({ todo, onDelete }) => {
  return (
    <div className="todo-item">
      <div className="todo-content">
        <h3>{todo.title}</h3>
        <p>{todo.description}</p>
      </div>
      <button onClick={() => onDelete(todo.id)}>Delete</button>
    </div>
  );
};

export default TodoItem; 