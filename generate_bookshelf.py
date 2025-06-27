import os
import json

def build_tree(base_dir, current_path=""):
    entries = []
    full_path = os.path.join(base_dir, current_path)

    for item in sorted(os.listdir(full_path)):
        rel_path = os.path.join(current_path, item)
        abs_path = os.path.join(base_dir, rel_path)

        if os.path.isdir(abs_path):
            entries.append({
                "type": "folder",
                "name": item,
                "children": build_tree(base_dir, rel_path)
            })
        elif item.endswith(".pdf"):
            entries.append({
                "type": "file",
                "name": item,
                "path": f"{base_dir}/{rel_path}".replace("\\", "/")
            })

    return entries

tree = build_tree("ebooks")

with open("bookshelf.js", "w", encoding="utf-8") as f:
    f.write("const ebookTree = ")
    json.dump(tree, f, ensure_ascii=False, indent=2)
    f.write(";\n")
