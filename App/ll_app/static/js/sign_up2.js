document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission

        // Get form data
        const firstName = document.getElementById('firstname').value;
        const lastName = document.getElementById('lastname').value;
        const email = document.getElementById('email').value;
        const mobile = document.getElementById('mobile').value;
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirm').value;

        // Basic validation (you can customize this as needed)
        if (password !== confirmPassword) {
            alert('Passwords do not match!');
            return;
        }

        // You can now send the form data to the backend via an AJAX request or store it in localStorage (optional)
        // Example (using fetch to send the form data):
        // fetch('/api/register', {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json',
        //     },
        //     body: JSON.stringify({
        //         first_name: firstName,
        //         last_name: lastName,
        //         email: email,
        //         mobile: mobile,
        //         password: password,
        //     }),
        // })
        // .then(response => response.json())
        // .then(data => {
        //     // Redirect to the sign-in page on success
        //     window.location.href = "/sign_in/";
        // })
        // .catch((error) => {
        //     console.error('Error:', error);
        // });

        // For now, just redirect to the sign_in page after form submission
        window.location.href = "/sign_in/";
    });
});
