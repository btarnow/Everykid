

// Allows for the dropdown filters to hold the user's selections from 
// previous page:

const raceDropdown = document.querySelector('#race');
const raceFilterInput = document.querySelector('#race_filter');

const genderDropdown = document.querySelector('#gender');
const genderFilterInput = document.querySelector('#gender_filter');

raceDropdown.value = raceFilterInput.value;
genderDropdown.value = genderFilterInput.value;


