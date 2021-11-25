import { createStore, combineReducers, applyMiddleware } from 'redux'
import thunk from 'redux-thunk'
import { composeWithDevTools } from 'redux-devtools-extension'
import {
    techListReducer,
    createTechReducer,
} from '../src/reducers/techReducers'

import {
    userLoginReducer
} from '../src/reducers/userReducers'



const reducer = combineReducers({
    techList: techListReducer,
    techCreate:createTechReducer,

    userLogin:userLoginReducer,

})

const userInfoFromStorage = localStorage.getItem('userLogin') ? 
    JSON.parse(localStorage.getItem('userLogin')) : null

const initialState = {
    userLogin: { userInfo: userInfoFromStorage},
}

const middleware = [thunk]

const store = createStore(reducer, initialState,
    composeWithDevTools(applyMiddleware(...middleware)))

export default store