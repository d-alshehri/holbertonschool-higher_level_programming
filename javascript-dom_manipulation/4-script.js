document.querySelector('#add_item').addEventListener('click', function () {
    const newItem = document.createElement('li'); // Create a new <li> element
    newItem.textContent = 'Item';                 // Set its text content to "Item"
    document.querySelector('.my_list').appendChild(newItem); // Append to the <ul>
  });
  