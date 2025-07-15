fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json()) // convert the response to JSON
  .then(data => {
    document.querySelector('#character').textContent = data.name; // set name to div
  })
  .catch(error => {
    console.error('Error fetching character:', error);
  });
