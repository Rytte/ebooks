# generate_bookshelf.py
import os
import json

ebook_folder = "ebooks"
output_file = "bookshelf.js"

book_list = []
for filename in sorted(os.listdir(ebook_folder)):
    if filename.endswith(".pdf"):
        title = os.path.splitext(filename)[0]
        book_list.append({
            "title": title,
            "author": "未知作者",  # 你也可以改为从文件名中提取作者
            "file": f"{ebook_folder}/{filename}"
        })

with open(output_file, "w", encoding="utf-8") as f:
    f.write("const books = ")
    json.dump(book_list, f, ensure_ascii=False, indent=2)
    f.write(";\n")

    f.write("""
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
""")
