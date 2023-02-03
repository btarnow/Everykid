

// In order to make the dropdown search bar NOT return back to it's original
// state and hold the user's selections, I need to the following code:

const raceDropdown = document.querySelector('#race');
const raceFilterInput = document.querySelector('#race_filter');

const genderDropdown = document.querySelector('#gender');
const genderFilterInput = document.querySelector('#gender_filter');

raceDropdown.value = raceFilterInput.value;
genderDropdown.value = genderFilterInput.value;



/////////////////////////////////////////////////////////////////////////////
// CODE I NO LONGER NEED, BUT AM KEEPING TO REMEMBER THINGS I'VE TRIED: 
/////////////////////////////////////////////////////////////////////////////

// I WAS GOING TO USE AN AJAX EVENT LISTENER ON THE "FIND BOOKS" BUTTON ON THE 
// BOOK_RESULTS_PAGE, BUT AJAX DOESN'T WORK WELL WITH JINJA RENDER TEMPLATES, SO
// SO I JUST UTILIZED A
// const findBooksButton = document.querySelector('#findBooksButton');

// findBooksButton.addEventListener('click', () => {
//     const raceFilter = document.querySelector('#race').value 
//     const genderFilter = document.querySelector('#gender').value 
//     const queryString = new URLSearchParams({'race':raceFilter, 'gender':genderFilter}).toString();
//     const url = `/book_filters?${queryString}`;

//     fetch(url)
//     .then(response => response.text())
//     .then(status => {
//     })
// })
