document.addEventListener('DOMContentLoaded', () => {
    fetch('/')
        .then(response => response.json())
        .then(data => {
            const productsSection = document.getElementById('products');
            data.forEach(product => {
                const productElement = document.createElement('div');
                productElement.className = 'product';
                productElement.innerHTML = `
                    <h3>${product.name}</h3>
                    <p>${product.description}</p>
                    <p>Price: $${product.price}</p>
                    <button data-id="${product.id}">Add to Cart</button>
                `;
                productsSection.appendChild(productElement);
            });
        });
});
