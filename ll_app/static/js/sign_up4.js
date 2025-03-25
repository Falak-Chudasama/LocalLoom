document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent default form submission

        // Get form data
        const businessName = document.getElementById('bname').value;
        const region = document.getElementById('region').value;
        const email = document.getElementById('email').value;
        const mobile = document.getElementById('mobile').value;

        // Basic validation
        if (!businessName || !region || !email || !mobile) {
            alert('Please fill in all fields!');
            return;
        }

        // Redirect to sign_in page after submission
        window.location.href = "/sign_in/";
    });
});
