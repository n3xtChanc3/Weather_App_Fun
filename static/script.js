// script.js

// Function to toggle between light and dark modes
function toggleDarkMode() {
    var body = document.body;
    var container = document.querySelector('.container');
    var footer = document.querySelector('footer');

    // Toggle background color and text color
    body.classList.toggle('dark-mode');
    container.classList.toggle('dark-mode');
    footer.classList.toggle('dark-mode');
}

// Event listener for button click
document.addEventListener('DOMContentLoaded', function() {
    var toggleButton = document.querySelector('#dark-mode-toggle');
    toggleButton.addEventListener('click', toggleDarkMode);
});
