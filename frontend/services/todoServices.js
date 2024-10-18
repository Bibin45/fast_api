import MainAxios from "./MainAxios";


export const getTodos = async () => {
  const response = await MainAxios.get(`api/todos`);
  return response;
};

export const createTodo = async (todo) => {
  const response = await MainAxios.post(`api/todos/create`, todo);
  return response;
};

export const getTodoById = async (id) => {
  const response = await MainAxios.get(`api/todos/${id}`);
  return response;
};

export const deleteTodo = async (id) => {
  const response = await MainAxios.delete(`api/todos/${id}`);
  return response;
};

export const updateTodo = async (id, updatedTodo) => {
  const response = await MainAxios.put(`api/todos/${id}`, updatedTodo);
  return response;
};