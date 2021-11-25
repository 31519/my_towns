import {
    USER_LOGIN_REQUEST,
    USER_LOGIN_SUCCESS,
    USER_LOGIN_FAIL,
  } from "../constants/userConstants";
  
import axios from 'axios'  

export const userLogin = (username, password) => async (dispatch) => {
    try{
        dispatch({type: USER_LOGIN_REQUEST});

        const config = {
            headers: {
                'Content-type': 'application/json'
            }
        }
        console.log('1')
        const {data} = await axios.post(
            "http://127.0.0.1:8000/api/users/login/",
            {username, password},
            config
        )
        console.log('2')
        dispatch({
            type: USER_LOGIN_SUCCESS,
            payload: data
        })
        localStorage.setItem('userLogin', JSON.stringify(data))

    }  catch (error) {
        dispatch({
          type: USER_LOGIN_FAIL,
          payload:
            error.response && error.response.data.detail
              ? error.response.data.detail
              : error.message,
        });
    }
}