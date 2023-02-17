"use strict"

const createCollectionForm = document.querySelector('#collection-form-label');
const toggleForm = document.querySelector('#collection-form-div');

createCollectionForm.addEventListener('click', () => {
    if (toggleForm.hidden === true){
        toggleForm.hidden = false;
    } else {
        toggleForm.hidden = true;
    }
})