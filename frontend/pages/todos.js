import { useEffect, useState } from 'react';
import Link from 'next/link';
import { createTodo, deleteTodo, getTodos } from '@/services/todoServices';

export default function Todos() {
  const [todos, setTodos] = useState([]);
  const [description, setDescription] = useState('');

  useEffect(() => {
    fetchTodos();
  }, []);

  const fetchTodos = async () => {
    const todos = await getTodos();
    setTodos(todos?.data);
  };

  const handleAddTodo = async () => {
    if (!description) return;
    const newTodo = await createTodo({ name:'Test', description: description });
    setTodos([...todos, newTodo]);
    setDescription('');
  };

  const handleDeleteTodo = async (_id) => {
    await deleteTodo(_id);
    setTodos(todos.filter(todo => todo._id !== _id));
  };

  return (
    <div>
      <h1>To-Do List</h1>
      <input
        type="text"
        placeholder="Add a new task"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <button onClick={handleAddTodo}>Add</button>

      <ul>
        {todos?.map((todo) => (
          <li key={todo?._id}>
            <div className='d-flex align-items-center justify-content-center'>
            <Link href={`/${todo?._id}`}>
              <p>{todo?.description}</p>
            </Link>
            <button onClick={() => handleDeleteTodo(todo?._id)}>Delete</button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}
