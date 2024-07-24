document.addEventListener('DOMContentLoaded', function() {
    const addItem = document.getElementById('add_item');
    const removeItem = document.getElementById('remove_item');
    const clearList = document.getElementById('clear_list');
    const myList = document.querySelector('.my_list');

    addItem.addEventListener('click', function() {
        const newItem = document.createElement('li');
        newItem.textContent = 'Item';
        myList.appendChild(newItem);
    });

    removeItem.addEventListener('click', function() {
        const lastItem = myList.lastElementChild;
        if (lastItem) {
            myList.removeChild(lastItem);
        }
    });

    clearList.addEventListener('click', function() {
        while (myList.firstChild) {
            myList.removeChild(myList.firstChild);
        }
    });
});