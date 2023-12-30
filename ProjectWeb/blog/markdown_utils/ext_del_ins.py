"""
Del/Ins Extension for Python-Markdown
=====================================
Wraps the inline content with ins/del tags.
Usage
-----
    >>> import markdown
    >>> src = '''This is ++added content + + and this is ~~deleted content~~'''
    >>> html = markdown.markdown(src, ['del_ins'])
    >>> print(html)
    <p>This is <ins>added content</ins> and this is <del>deleted content</del>
    </p>
Dependencies
------------
* [Markdown 2.0+](https://www.freewisdom.org/projects/python-markdown/)
Copyright
---------
2011, 2012 [The active archives contributors](https://activearchives.org/)
All rights reserved.
This software is released under the modified BSD License.
See LICENSE.md for details.
"""
from markdown import Extension
from markdown.inlinepatterns import SimpleTagPattern


DEL_RE = r"(\~\~)(.+?)(\~\~)"
INS_RE = r"(\+\+)(.+?)(\+\+)"


class DelInsExtension(Extension):
    """Adds del_ins extension to Markdown class."""

    def extendMarkdown(self, md):
        del_tag = SimpleTagPattern(DEL_RE, "del")
        ins_tag = SimpleTagPattern(INS_RE, "ins")
        md.inlinePatterns.register(del_tag, "del", 75)
        md.inlinePatterns.register(ins_tag, "ins", 76)
