let buttons = document.querySelectorAll('.list-group-item');

buttons.forEach(button => {
    button.addEventListener('click', function () {
        buttons.forEach(btn => btn.classList.remove('active'));
        this.classList.add('active');
    });
});

// const activePage = window.location.pathname;
// const categoryLinks = document.querySelectorAll('.list-group a');

// categoryLinks.forEach(link => {
//     console.log(link.href)
// })

// console.log(activePage);