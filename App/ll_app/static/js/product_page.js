// let productArray = [];
// fetch('/api/products/')
// .then(response => response.json())
// .then(data => {
//     productArray = data;
//     console.log(productArray);  // [{ id: '...', name: '...' }, ...]
// })
// .catch(error => console.error('Error fetching product data:', error));

document.addEventListener('DOMContentLoaded', function () {
    const buyBtn = document.querySelector('.buy');
    console.log('FUCK THIS PAGE');
    buyBtn.addEventListener('click', function () {
        Swal.fire({
            title: 'Confirm Purchase',
            text: `Buy "${document.querySelector('.name').textContent}" for ₹${document.getElementById('price').textContent.replace(/\D/g, '')}?`,
            icon: 'question',
            showCancelButton: true,
            confirmButtonText: 'Yes, Buy Now',
            cancelButtonText: 'Cancel',
            confirmButtonColor: '#4CAF50',
            cancelButtonColor: '#d33'
        }).then((result) => {
            if (result.isConfirmed) {
                Swal.fire({
                    title: 'Purchase Successful!',
                    text: 'Thank you for your purchase.',
                    icon: 'success',
                    confirmButtonText: 'OK',
                    confirmButtonColor: '#4CAF50'
                });

                // Optional: Redirect or handle purchase logic
                // window.location.href = '/purchase/success/';
            }
        });
    });
});
