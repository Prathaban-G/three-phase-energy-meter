document.addEventListener('DOMContentLoaded', function () {
    var searchForm = document.getElementById('searchForm');
    var searchInput = document.getElementById('searchInput');
    var searchResults = document.getElementById('searchResults');

    searchForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent form submission

        var searchQuery = searchInput.value.toLowerCase();

        // Example search functionality, replace with your own logic
        if (searchQuery === 'home') {
            window.location.href = 'home.html'; // Redirect to page1.html
        } else if (searchQuery === 'project') {
            window.location.href = 'addProjects.html'; // Redirect to page2.html
        }
        else if (searchQuery === 'user') {
            window.location.href = 'addUser.html'; // Redirect to page2.html
        }
         else {
            searchResults.textContent = 'No results found';
        }
    });
});
