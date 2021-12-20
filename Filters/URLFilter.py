from LatexTemplater.TemplateFilter import TemplateFilter
from LatexTemplater.TemplateCore import TemplateCore
from typing import Dict, Callable
import os
def registrationInfo() -> Dict[str, Callable[[any], str]]:
    return {
        URLFilter.name: URLFilter.filter
    }


class URLFilter(TemplateFilter):
    name = "URL"
    
    @staticmethod
    def filter(url: Dict[str, str]) -> str:
        inst = TemplateCore.instance()
        if inst.vars["paper"]:
            return url["short"]
        else:
            return r"\url{" + url["url"] + "}"
