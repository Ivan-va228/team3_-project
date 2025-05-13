async function searchProducts() {
    let query = document.getElementById('search-input').value.trim();
    let resultsContainer = document.getElementById('search-results');

    if (query.length < 2) {
        resultsContainer.innerHTML = ''; 
        resultsContainer.style.display = 'none'; 
        return;
    }

    try {
        let response = await fetch(`/api/products/search/?q=${query}`);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        let data = await response.json();

        if (data.count === 0) {
            resultsContainer.innerHTML = ''; 
            resultsContainer.style.display = 'none'; 
            return;
        }

        resultsContainer.style.display = 'block';

        resultsContainer.innerHTML = '';

        data.results.forEach(product => {
            let item = document.createElement('div');
            item.classList.add('search-result-item');
            item.innerHTML = `
                <a href="/product/${product.id}">${product.name}</a> <!-- Додаємо посилання на сторінку товару -->
            `;
            resultsContainer.appendChild(item);
        });
    } catch (error) {
        console.error('Search error:', error);
        resultsContainer.innerHTML = ''; 
        resultsContainer.style.display = 'none'; 
    }
}

function clearSearch() {
    document.getElementById('search-input').value = '';
    document.getElementById('search-results').innerHTML = '';
    document.getElementById('search-results').style.display = 'none'; 
}

document.getElementById('search-input').addEventListener('input', searchProducts);
document.querySelector('.search-container button').addEventListener('click', clearSearch);
