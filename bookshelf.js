const books = [
  {
    "title": "csapp",
    "author": "未知作者",
    "file": "ebooks/csapp.pdf"
  },
  {
    "title": "python",
    "author": "未知作者",
    "file": "ebooks/python.pdf"
  },
  {
    "title": "video_file_format_spec_v10",
    "author": "未知作者",
    "file": "ebooks/video_file_format_spec_v10.pdf"
  }
];

const container = document.getElementById("bookshelf");
books.forEach(book => {
  const item = document.createElement("div");
  item.className = "book-item";
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
