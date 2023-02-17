

// Allows for the dropdown filters to hold the user's selections from 
// previous page:

const raceDropdown = document.querySelector('#race');
const raceFilterInput = document.querySelector('#race_filter');

const genderDropdown = document.querySelector('#gender');
const genderFilterInput = document.querySelector('#gender_filter');

raceDropdown.value = raceFilterInput.value;
genderDropdown.value = genderFilterInput.value;



// // Handles if the user selects the bookmark to save a book to their collection
// const bookToAddBtn = document.querySelector('#add-book-btn');

// //TODO: This function needs to add the book to the data base if the button is 
// // UNSELECTED --> SELECTED. If the button goes from SELECTED --> UNSELECTED, remove
// bookToAddBtn.addEventListener('click', evt => {
//     evt.preventDefault();
//     const bookID = document.querySelector('#book-id').value;
//     fetch(`/add_book?book_id=${book_id}`)
//     .then((response) => response.text())
//     .then((jsonData) = {
//         bookToAddBtn
        
//     });
// })