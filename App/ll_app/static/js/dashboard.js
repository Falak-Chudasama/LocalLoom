let productArray = []; // Declare globally

fetch('/dashboard/?format=json')
  .then(response => {
    if (!response.ok) throw new Error("Network response was not ok");
    return response.json();
  })
  .then(data => {
    productArray = data.products; // Store in global variable
    console.log("Product ID and Name array:", productArray);
  })
  .catch(error => {
    console.error("Error fetching product data:", error);
  });
