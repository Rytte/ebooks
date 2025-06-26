const books = [
    {
        title: "深入理解计算机系统",
        author: "Randal E. Bryant",
        file: "ebooks/csapp.pdf"
    },
    {
        title: "Python编程：从入门到实践",
        author: "Eric Matthes",
        file: "ebooks/python.pdf"
    },
    {
        title: "C语言程序设计",
        author: "谭浩强",
        file: "ebooks/c_programming.pdf"
    }
    // 更多书籍……
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
