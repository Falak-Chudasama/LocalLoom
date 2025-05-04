let productArray = [];

    fetch('/api/products/')
        .then(response => response.json())
        .then(data => {
            productArray = data;
            console.log(productArray);  // [{ id: '...', name: '...' }, ...]
        })
        .catch(error => console.error('Error fetching product data:', error));