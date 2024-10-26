document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('dark-mode-toggle');

    function toggleDarkMode() {
        document.body.classList.toggle('dark-mode');
    }

    toggleButton.addEventListener('click', toggleDarkMode);
});
