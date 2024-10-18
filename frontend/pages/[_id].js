import { useEffect, useState } from 'react';
import { useRouter } from 'next/router';
import { getTodoById, updateTodo } from '@/services/todoServices';

export default function TodoDetails() {
  const [todo, setTodo] = useState(null);
  const [isEdit , setIsEdit] = useState(null);
  const [description, setDescription] = useState('');

  const router = useRouter();
  const { _id } = router.query;

  useEffect(() => {
    if (_id) {
      fetchTodo();
    }
  }, [_id]);

  const fetchTodo = async () => {
    const todoItem = await getTodoById(_id);
    setTodo(todoItem);
  };
  const handleEditTodo = async () => {
    const todoItem = await updateTodo(_id,{ name:'Test', description: isEdit });
    setTodo(todoItem);
    setIsEdit(false);
  };
  if (!todo) return <p>Loading...</p>;

  return (
    <div>
      <h1>Todo: {todo.title}</h1>
      {isEdit?
      <input  type="text"
        placeholder="edit a new task"
        value={isEdit}
        onChange={(e) => setIsEdit(e.target.value)}/>
        :
        <p>{todo.description || 'No description provided'}</p>}
       <button onClick={()=>isEdit?handleEditTodo():setIsEdit(todo.description)}>{isEdit?'save':'edit'}</button>
    </div>
  );
}
