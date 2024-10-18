import { getStorage } from '@/helper/helper';
import axios from 'axios';
import { getCookie } from 'cookies-next';


const TOKEN = getCookie('token');
const MainAxios = axios.create({
    baseURL: 'http://localhost:8000',
    headers: {
        'Content-Type': 'application/json',
    }
});

MainAxios.interceptors.request.use(function (config) {
    if (TOKEN) {
        config.headers["Authorization"] = `Bearer ${TOKEN}`;
    }
    return config;
});

MainAxios.interceptors.response.use(
({ data }) => data,
(error) => {
    return Promise.reject({ message: error.message });
}
);

export default MainAxios;