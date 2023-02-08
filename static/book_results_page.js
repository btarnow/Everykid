

// In order to make the dropdown search bar NOT return back to it's original
// state and hold the user's selections, I need to the following code:

const raceDropdown = document.querySelector('#race');
const raceFilterInput = document.querySelector('#race_filter');

const genderDropdown = document.querySelector('#gender');
const genderFilterInput = document.querySelector('#gender_filter');

raceDropdown.value = raceFilterInput.value;
genderDropdown.value = genderFilterInput.value;

