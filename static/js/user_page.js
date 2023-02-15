"use strict"

const createCollection = document.querySelector('#create-collection-form');
const toggleForm = document.querySelector('#toggle-form');

createCollection.addEventListener('click', () => {
    if (toggleForm.hidden === true){
        toggleForm.hidden = false;
    } else {
        toggleForm.hidden = true;
    }
})