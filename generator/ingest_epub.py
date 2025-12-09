from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup
from pathlib import Path

def extract_paragraphs(epub_path: Path, limit=None):
    book = epub.read_epub(str(epub_path))
    paragraphs = []

    spine_ids = [item_id for item_id, _ in book.spine]
    docs = {
        item.get_id(): item
        for item in book.get_items()
        if item.get_type() == ITEM_DOCUMENT
    }

    for item_id in spine_ids:
        item = docs.get(item_id)
        if not item:
            continue

        soup = BeautifulSoup(item.get_content(), "html.parser")
        for p in soup.find_all("p"):
            text = p.get_text(strip=True)
            if text:
                paragraphs.append(text)
                if limit and len(paragraphs) >= limit:
                    return paragraphs

    return paragraphs
