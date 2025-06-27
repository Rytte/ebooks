const bookCategories = {
  "未分类": [
    {
      "title": "ESP-01S Relay v4.0---",
      "author": "未知作者",
      "file": "ebooks/ESP-01S Relay v4.0---.pdf"
    },
    {
      "title": "video_file_format_spec_v10",
      "author": "未知作者",
      "file": "ebooks/video_file_format_spec_v10.pdf"
    },
    {
      "title": "csapp",
      "author": "未知作者",
      "file": "ebooks/csapp.pdf"
    },
    {
      "title": "python",
      "author": "未知作者",
      "file": "ebooks/python.pdf"
    }
  ],
  "电路": [
    {
      "title": "asdasdasdasd",
      "author": "未知作者",
      "file": "ebooks/电路/asdasdasdasd.pdf"
    }
  ]
};

function renderBooks(category) {
  const container = document.getElementById('bookshelf');
  container.innerHTML = '';

  const books = bookCategories[category];
  books.forEach(book => {
    const item = document.createElement('div');
    item.className = 'book-item';
    item.innerHTML = `
      <div class="book-info">
        <div class="book-title">📘 ${book.title}</div>
        <div class="book-author">${book.author}</div>
      </div>
      <div class="book-link">
        <a href="${book.file}" target="_blank">📥 阅读/下载</a>
      </div>
    `;
    container.appendChild(item);
  });
}

function renderCategories() {
  const categories = Object.keys(bookCategories);
  const menu = document.getElementById('category-menu');
  categories.forEach(category => {
    const button = document.createElement('button');
    button.textContent = category;
    button.onclick = () => renderBooks(category);
    menu.appendChild(button);
  });
}

document.addEventListener('DOMContentLoaded', renderCategories);
    