import markdown

from markdown.extensions.toc import TocExtension

from ProjectWeb.blog.markdown_utils.ext_del_ins import DelInsExtension
from ProjectWeb.blog.markdown_utils.ext_emoji import EmojiExtension
from ProjectWeb.blog.markdown_utils.ext_escapehtml import EscapeHtml


def conv_from_markdown(md_text):
    md = markdown.Markdown(
        extensions=[
            "markdown.extensions.extra",
            "markdown.extensions.nl2br",
            "markdown.extensions.smarty",
            "markdown.extensions.fenced_code",
            TocExtension(toc_class="markdown_toc", toc_depth="2-6"),
            "markdown_captions",
            DelInsExtension(),
            EmojiExtension(),
            EscapeHtml(),
        ])
    return md.convert(md_text), md.toc
