document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission

        // Get form data
        const businessId = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        // Basic validation (you can customize this as needed)
        if (!businessId || !password) {
            alert('Please fill in all fields!');
            return;
        }

        // You can now send the form data to the backend via an AJAX request or store it in localStorage (optional)
        // Example (using fetch to send the form data):
        // fetch('/api/register_business', {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json',
        //     },
        //     body: JSON.stringify({
        //         business_id: businessId,
        //         password: password,
        //     }),
        // })
        // .then(response => response.json())
        // .then(data => {
        //     // Redirect to the sign_up4 page on success
        //     window.location.href = "/sign_up4/";
        // })
        // .catch((error) => {
        //     console.error('Error:', error);
        // });

        // For now, just redirect to the sign_up4 page after form submission
        window.location.href = "/sign_in/";
    });
});
