function getOrders() {
  fetch('http://192.168.80.3:5004/api/orders', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
    credentials: 'include',
  })
    .then((response) => response.json())
    .then((data) => {
      // Obtener el cuerpo de la tabla
      var orderListBody = document.querySelector('#order-list tbody');
      orderListBody.innerHTML = ''; // Limpiar datos anteriores

      // Recorrer los pedidos y llenar las filas de la tabla
      data.forEach((order) => {
        var row = document.createElement('tr');

        // Price (saleTotal en tu JSON)
        var priceCell = document.createElement('td');
        priceCell.textContent = order.saleTotal;
        row.appendChild(priceCell);

        // Name (userName en tu JSON)
        var nameCell = document.createElement('td');
        nameCell.textContent = order.userName ? order.userName : 'N/A';
        row.appendChild(nameCell);

        // Actions
        var actionsCell = document.createElement('td');

        // View Details button
        var viewButton = document.createElement('button');
        viewButton.textContent = 'View Details';
        viewButton.addEventListener('click', function () {
          showOrderDetails(order.id);
        });
        actionsCell.appendChild(viewButton);

        row.appendChild(actionsCell);

        // Añadir la fila a la tabla
        orderListBody.appendChild(row);
      });
    })
    .catch((error) => console.error('Error:', error));
}

function showOrderDetails(orderId) {
  fetch(`http://192.168.80.3:5004/api/orders/${orderId}`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
    credentials: 'include',
  })
    .then((response) => response.json())
    .then((order) => {
      const orderDetails = document.getElementById('order-details');

      // Como no has mencionado un campo 'products', lo omitimos
      const detailsHtml = `
          <h4>Order ID: ${order.id}</h4>
          <p><strong>User:</strong> ${order.userName}</p>
          <p><strong>Email:</strong> ${order.userEmail}</p>
          <p><strong>Total:</strong> ${order.saleTotal}</p>
      `;

      orderDetails.innerHTML = detailsHtml;
    })
    .catch((error) => console.error('Error:', error));
}
