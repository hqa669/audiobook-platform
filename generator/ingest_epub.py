from pathlib import Path
from typing import List, Optional
from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup


def extract_paragraphs(
    epub_path: Path,
    limit: Optional[int] = None,
) -> List[str]:
    book = epub.read_epub(str(epub_path))
    paragraphs: List[str] = []

    spine_ids = [item_id for item_id, _ in book.spine]
    documents = {
        item.get_id(): item
        for item in book.get_items()
        if item.get_type() == ITEM_DOCUMENT
    }

    for item_id in spine_ids:
        item = documents.get(item_id)
        if not item:
            continue

        soup = BeautifulSoup(item.get_content(), "html.parser")
        for p in soup.find_all("p"):
            text = p.get_text(strip=True)
            if not text:
                continue

            paragraphs.append(text)
            if limit and len(paragraphs) >= limit:
                return paragraphs

    return paragraphs
