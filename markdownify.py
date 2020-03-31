#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 31.03.20
@author: felix
"""
import re


def markdownify(html_str: str) -> str:

    class Markdownify:
        FirstOpenPTag = r'^<[a-z]>'
        OpenPTag = r'<p>'
        ClosingPTag = r'</p>'
        BrTag = r'<br>'
        StrongTag = r'<strong>'
        CStrongTag = r'</strong>'

        def __init__(self, html_text: str):
            self.html = html_text

        @staticmethod
        def replace_linebreak(txt: str) -> str:
            return txt.replace('\n', ' ')

        def replace_p_tags(self, txt: str) -> str:
            return re.sub(self.OpenPTag, '\n\n', txt)

        def replace_closing_p(self, txt: str) -> str:
            return re.sub(self.ClosingPTag, '', txt)

        def replace_br_tag(self, txt: str) -> str:
            return re.sub(self.BrTag, '  \n', txt)

        def replace_strong_tag(self, txt: str) -> str:
            return re.sub(self.StrongTag, '**', re.sub(self.CStrongTag, '**', txt))

        @staticmethod
        def replace_hyperlinks(txt: str) -> str:
            def rep_hyper(tmp_txt: str) -> str:
                link_pattern = r'[\w\W\d\D]+(</a>)'
                link_name_pattern = r'[>][\w\W\d\D]+[<]'
                link_url_pattern = r'[\"][\w\W\d\D]+[\"]'
                tmp = tmp_txt
                l_names = re.findall(link_name_pattern, tmp)
                l_uris = re.findall(link_url_pattern, tmp_txt)
                link_url = link_name = None
                if l_names:
                    link_name = f'[{l_names[0].replace(">", "").replace("<", "")}]'
                if l_uris:
                    link_url = l_uris[0].replace('"', '')
                    link_url = f'({link_url})'
                if link_url is not None and link_name is not None:
                    tmp = re.sub(link_pattern, f'{link_name}{link_url}', tmp_txt)
                    return tmp.strip()
                else:
                    if '<a' not in tmp_txt:
                        return tmp_txt.strip()

            new_text = [rep_hyper(t) for t in re.split(r'(<a)', txt)]
            new_text = [n for n in new_text if n]
            return ' '.join(new_text) if new_text else rep_hyper(txt)

        def markdownify(self) -> str:
            tmp = self.replace_linebreak(self.html)
            # split after first tag
            tmp_split = re.split(self.FirstOpenPTag, tmp)
            tmp_split = tmp_split[0] if len(tmp_split) == 1 else tmp_split[1]

            # find and replace tags
            tmp = tmp_split
            for func in [self.replace_p_tags, self.replace_closing_p, self.replace_br_tag, self.replace_strong_tag]:
                tmp = func(tmp)

            if '</a>' in tmp:
                return self.replace_hyperlinks(tmp)
            else:
                return tmp

    return Markdownify(html_str).markdownify()
