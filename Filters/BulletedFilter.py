from LatexTemplater.TemplateFilter import TemplateFilter
from LatexTemplater.TemplateCore import TemplateCore
from typing import Dict, Callable, List
import os
def registrationInfo() -> Dict[str, Callable[[any], str]]:
    return {
        BulletedListFilter.name: BulletedListFilter.filter
    }


class BulletedListFilter(TemplateFilter):
    name = "Bulleted"
    def filter(items: List[str]) -> str:
        return (r"\begin{itemize}[noitemsep,nolistsep]" + os.linesep + 
                ("\n").join([r"\item " + item for item in items]) + os.linesep +
                r"\end{itemize}" + os.linesep
                )
