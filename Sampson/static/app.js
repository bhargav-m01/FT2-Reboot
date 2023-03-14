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
  newWindow.document.write(`<h1>Complaint: ${text}</h1><br> <h1>Response: Dear valued customer,

  We are sorry to hear that you had a negative experience with our bank. We take all customer complaints seriously and would like to apologize for any inconvenience that you may have experienced.
  
  We would like to assure you that we are committed to providing our customers with the best service possible, and we regret that we have fallen short of your expectations.
  
  We kindly request you to provide us with more details about the issue you encountered so that we can investigate the matter and take appropriate actions to ensure that similar incidents do not occur in the future.
  
    We will attempt to contact you using the phone number you've provided. We value your business and appreciate your feedback.
  
  Thank you for bringing this matter to our attention.
  
  Sincerely,
  
  Customer Service Representative.</h1>`);
  newWindow.document.close();
}
