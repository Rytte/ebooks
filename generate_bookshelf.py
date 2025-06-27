import os
import json

ebook_folder = "ebooks"
output_file = "bookshelf.js"

# 扫描目录，获取文件夹结构
def scan_directory(folder):
    categories = {}
    for root, dirs, files in os.walk(folder):
        # 获取相对路径的目录名称（相对于 ebooks/）
        category = os.path.relpath(root, folder)
        if category == ".":
            category = "未分类"
        categories[category] = []

        for file in files:
            if file.endswith(".pdf"):
                title = os.path.splitext(file)[0]
                # 正确的路径加上 ebooks/ 前缀
                relative_path = os.path.relpath(os.path.join(root, file), ".")
                categories[category].append({
                    "title": title,
                    "author": "未知作者",
                    "file": relative_path.replace("\\", "/")  # 兼容 Windows
                })
    return categories

# 获取分类数据
book_categories = scan_directory(ebook_folder)

# 写入 bookshelf.js
with open(output_file, "w", encoding="utf-8") as f:
    f.write("const bookCategories = ")
    json.dump(book_categories, f, ensure_ascii=False, indent=2)
    f.write(";\n")

    f.write("""
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
    """)
