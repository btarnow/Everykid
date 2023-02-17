// // Handles if the user selects the bookmark to save a book to their collection
const bookToAddBtn = document.querySelector('#add-book-btn');

bookToAddBtn.addEventListener('click', evt => {
    evt.preventDefault();
    const bookID = document.querySelector('#book-id').value;

    if (bookToAddBtn.dataset.inCollection === 'true') {
        console.log("Remove from collection.")
        fetch(`/remove_book_from_details?book_id=${bookID}`)
        .then((response) => response.text())
            .then((collectionName) => {
                bookToAddBtn.innerHTML = ` Add to Collection`;
                bookToAddBtn.classList.toggle('fa-regular');
                bookToAddBtn.classList.toggle('fa-solid');
                bookToAddBtn.dataset.inCollection = 'false';
            });
    }

    else if (bookToAddBtn.dataset.inCollection === 'false') {
        fetch(`/add_book?book_id=${bookID}`)
            .then((response) => response.text())
            .then((collectionName) => {
                console.log('The route /add_books is being hit.')
                bookToAddBtn.innerHTML = ` Saved to ${collectionName}`;
                bookToAddBtn.classList.toggle('fa-regular');
                bookToAddBtn.classList.toggle('fa-solid');
                bookToAddBtn.dataset.inCollection = 'true';
            });
    }
})

