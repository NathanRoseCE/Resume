from LatexTemplater.TemplateFilter import TemplateFilter
from LatexTemplater.TemplateCore import TemplateCore
from typing import Dict, Callable, List
import os
def registrationInfo() -> Dict[str, Callable[[any], str]]:
    return {
        SkillsFilter.name: SkillsFilter.filter
    }


class SkillsFilter(TemplateFilter):
    name = "Skills"
    def filter(val: any) -> str:
        inst = TemplateCore.instance()
        return ( inst.filter("CSV", val["applications"]) + "\n\n" +
                 inst.filter("CSV", val["languanges"]) + "\n\n" +
                 inst.filter("CSV", val["keywords"]) + "\n\n")
