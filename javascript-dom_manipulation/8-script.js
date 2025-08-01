document.addEventListener('DOMContentLoaded', () => {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
      .then(response => response.json())
      .then(data => {
        const helloDiv = document.getElementById('hello');
        helloDiv.textContent = data.hello;
      })
      .catch(error => {
        console.error('Error fetching hello translation:', error);
      });
  });
  