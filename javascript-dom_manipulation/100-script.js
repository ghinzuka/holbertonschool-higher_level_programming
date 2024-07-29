document.addEventListener('DOMContentLoaded', function() {
    const addItem = document.getElementById('add_item');
    const removeItem = document.getElementById('remove_item');
    const clearList = document.getElementById('clear_list');

    addItem.addEventListener('click', function() {
        const newItem = document.createElement('li');
        newItem.textContent = 'Item';
        document.querySelector('.my_list').appendChild(newItem);
    });

    removeItem.addEventListener('click', function() {
        const lastItem = document.querySelector('.my_list').lastElementChild;
        if (lastItem) {
            document.querySelector('.my_list').removeChild(lastItem);
        }
    });

    clearList.addEventListener('click', function() {
        while (document.querySelector('.my_list').firstChild) {
            document.querySelector('.my_list').removeChild(document.querySelector('.my_list').firstChild);
        }
    });
});