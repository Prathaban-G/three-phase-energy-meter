document.addEventListener('DOMContentLoaded', function () {
    var expandableDivs = document.querySelectorAll('.expandableDiv');
    var fullViewButtons = document.querySelectorAll('.fullViewButton');

    fullViewButtons.forEach(function (button, index) {
        button.addEventListener('click', function () {
            expandDiv(expandableDivs[index]);
        });
    });

    function expandDiv(div) {
        if (!div.classList.contains('expanded')) {
            div.classList.add('expanded');
        } else {
            div.classList.remove('expanded');
        }
    }
});
