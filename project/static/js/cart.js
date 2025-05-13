// Отримуємо контейнер для відображення товарів
const cartItemsContainer = document.querySelector('.cart-items');

// Функція для оновлення підсумків корзини
function updateCartSummary() {
    // Отримуємо товари з сесії
    const cart = JSON.parse(sessionStorage.getItem('cart')) || [];

    // Оновлюємо ціни всіх товарів
    const prices = cart.map(item => item.productPrice);

    const total = prices.reduce((sum, price) => sum + price, 0);
    document.querySelector('.cart-price').textContent = `$${total.toFixed(2)}`;

    // Вартість доставки (припустимо $20)
    const shippingCost = 20;
    document.querySelector('.cart-shipping').textContent = `from $${shippingCost.toFixed(2)}`;

    // Повна ціна з доставкою
    document.querySelector('.cart-full-price').textContent = `$${(total + shippingCost).toFixed(2)}`;
}

// Функція для додавання товару в корзину
function addToCart(productId, productName, productPrice) {
    // Отримуємо поточний кошик із сесії
    const cart = JSON.parse(sessionStorage.getItem('cart')) || [];
    
    // Перевірка чи товар вже є в кошику
    const existingProduct = cart.find(item => item.productId === productId);
    if (existingProduct) {
        existingProduct.quantity += 1;
    } else {
        cart.push({ productId, productName, productPrice, quantity: 1 });
    }

    // Зберігаємо оновлений кошик у сесії
    sessionStorage.setItem('cart', JSON.stringify(cart));

    // Оновлюємо вміст кошика
    renderCartItems();
    updateCartSummary();
}

// Функція для відображення товарів в корзині
function renderCartItems() {
    // Отримуємо товари з сесії
    const cart = JSON.parse(sessionStorage.getItem('cart')) || [];

    // Очищаємо контейнер
    cartItemsContainer.innerHTML = '';

    // Якщо кошик порожній
    if (cart.length === 0) {
        cartItemsContainer.innerHTML = '<p>Your cart is empty</p>';
        return;
    }

    // Додаємо товари в контейнер
    cart.forEach(item => {
        const cartItem = document.createElement('div');
        cartItem.classList.add('cart-item');
        cartItem.innerHTML = `
            <div class="item-details">
                <p class="item-name">${item.productName}</p>
                <p class="item-price">$${item.productPrice.toFixed(2)}</p>
                <p class="item-quantity">Quantity: ${item.quantity}</p>
            </div>
        `;
        cartItemsContainer.appendChild(cartItem);
    });
}

// Викликаємо функцію рендерингу при завантаженні сторінки
renderCartItems();
updateCartSummary();

// Оновлення кошика при натисканні кнопки "Add to Cart"
const addToCartButtons = document.querySelectorAll('.add-to-cart');

addToCartButtons.forEach(button => {
    button.addEventListener('click', (event) => {
        const productId = button.getAttribute('data-product-id');
        const productName = button.getAttribute('data-product-name');
        const productPrice = parseFloat(button.getAttribute('data-product-price'));

        // Додаємо товар в корзину
        addToCart(productId, productName, productPrice);
    });
});
