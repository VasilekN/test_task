import unittest
from .services import parse_content


class TestParseContent(unittest.TestCase):
    def test_empty_html(self):
        html = ""
        result = parse_content(html)
        self.assertEqual(result["h1_count"], 0)
        self.assertEqual(result["h2_count"], 0)
        self.assertEqual(result["h3_count"], 0)
        self.assertEqual(result["links"], [])

    def test_headers_with_links(self):
        html = """
        <html>
            <body>
                <h1>Title</h1>
                <a href="https://example.com/page1">Link 1</a>
                <a href="https://example.com/page2">Link 2</a>
                <h2>Subtitle</h2>
                <a href="https://example.com/page3">Link 3</a>
            </body>
        </html>
        """
        result = parse_content(html)
        self.assertEqual(result["h1_count"], 1)
        self.assertEqual(result["h2_count"], 1)
        self.assertEqual(result["h3_count"], 0)
        expected_links = [
            "https://example.com/page1",
            "https://example.com/page2",
            "https://example.com/page3"
        ]
        self.assertCountEqual(result["links"], expected_links)

    def test_parse_content_json(self):
        json = """ {"key": "value"} """
        result = parse_content(json)
        self.assertEqual(result["h1_count"], 0)
        self.assertEqual(result["h2_count"], 0)
        self.assertEqual(result["h3_count"], 0)
        self.assertEqual(result["links"], [])
