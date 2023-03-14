let items = [];

function addItem() {
  const itemInput = document.getElementById('item');

  const item = itemInput.value;

  if (!item) {
    alert('Please enter an item');
    return;
  }

  const newItem = { item };
  items.push(newItem);

  itemInput.value = '';

  renderItems();
}

function renderItems() {
  const checklist = document.getElementById('checklist');
  checklist.innerHTML = '';

  items.forEach(item => {
    const li = document.createElement('li');
    const a = document.createElement('a');
    a.href = '#';
    a.textContent = item.item;
    a.addEventListener('click', () => openWindow(item.item));
    li.appendChild(a);
    checklist.appendChild(li);
  });
}

function openWindow(text) {
  const newWindow = window.open('', 'Checklist Item', 'height=200,width=400');
  newWindow.document.write(`<h1>${text}</h1>`);
  newWindow.document.close();
}
