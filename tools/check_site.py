"""Check the static site's local links, fragment IDs, original assets, and scope."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]


class Document(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.images = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if 'id' in values:
            assert values['id'] not in self.ids, f'Duplicate id: {values["id"]}'
            self.ids.add(values['id'])
        for attr in ('href', 'src'):
            if values.get(attr):
                self.links.append(values[attr])
        if tag == 'img':
            assert 'alt' in values, 'Image missing alt attribute'
            self.images.append(values)


documents = {}
for path in ROOT.rglob('*.html'):
    if '.git' in path.parts:
        continue
    document = Document()
    document.feed(path.read_text())
    documents[path.resolve()] = document
checked = 0
for path, document in documents.items():
    for raw in document.links:
        url = urlsplit(raw)
        if url.scheme or url.netloc:
            assert url.scheme in ('https', 'http', 'mailto'), f'Unexpected scheme: {raw}'
            continue
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        assert target.is_relative_to(ROOT), f'Link escapes website: {raw}'
        assert target.exists(), f'Missing local target in {path.name}: {raw}'
        if url.fragment and target.suffix == '.html':
            assert unquote(url.fragment) in documents[target].ids, f'Missing fragment: {raw}'
        checked += 1
for entry in json.loads((ROOT / 'assets/PROVENANCE.json').read_text()):
    assert hashlib.sha256((ROOT / entry['asset']).read_bytes()).hexdigest() == entry['sha256']
assert len(documents) == 2
assert 'not live monitoring' in (ROOT / 'index.html').read_text()
assert 'Zero real model requests' in (ROOT / 'docs/controllers.html').read_text()
print(json.dumps(dict(status='PASS', html_documents=len(documents), local_links=checked,
                      original_figure_hashes='2/2 match', hardware='NOT_RUN',
                      scope='Static website checks only'), indent=2))
