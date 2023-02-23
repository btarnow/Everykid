// "use strict";

// Handles if the user selects the bookmark to save a book to their collection
const bookToAddBtn = document.querySelector('#add-book-btn');

bookToAddBtn.addEventListener('click', evt => {
    evt.preventDefault();
    const bookID = document.querySelector('#book-id').value;

    if (bookToAddBtn.dataset.inCollection === 'true') {
        fetch(`/remove_book_from_details?book_id=${bookID}`)
        .then((response) => response.text())
            .then((collectionName) => {
                bookToAddBtn.innerHTML = `<span class='text-in-btn'>Add to My Books</span>`;
                bookToAddBtn.classList.toggle('fa-regular');
                bookToAddBtn.classList.toggle('fa-solid');
                bookToAddBtn.dataset.inCollection = 'false';
            });
    }

    else if (bookToAddBtn.dataset.inCollection === 'false') {
        fetch(`/add_book?book_id=${bookID}`)
            .then((response) => response.text())
            .then((collectionName) => {
                bookToAddBtn.innerHTML = `<span class='text-in-btn'>Saved to ${collectionName}</span>`;
                bookToAddBtn.classList.toggle('fa-regular');
                bookToAddBtn.classList.toggle('fa-solid');
                bookToAddBtn.dataset.inCollection = 'true';
            });
    }
})

