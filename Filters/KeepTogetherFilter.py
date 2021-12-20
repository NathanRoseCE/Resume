from LatexTemplater.TemplateFilter import TemplateFilter
from typing import Dict, Callable, List
import os
def registrationInfo() -> Dict[str, Callable[[any], str]]:
    return {
        KeepTogetherFilter.name: KeepTogetherFilter.filter
    }


class KeepTogetherFilter(TemplateFilter):
    name = "KeepTogether"
    
    def filter(val: str) -> str:
        return (r"\noindent\begin{minipage}{\linewidth}" + os.linesep +
                val + os.linesep + 
                r"\end{minipage}" + os.linesep +
                r"\vspace{\entrySpacing}" + os.linesep)
