from LatexTemplater.TemplateFilter import TemplateFilter
from LatexTemplater.TemplateCore import TemplateCore
from typing import Dict, Callable, List
import os
def registrationInfo() -> Dict[str, Callable[[any], str]]:
    return {
        WorkFilter.name: WorkFilter.filter
    }


class WorkFilter(TemplateFilter):
    name = "Work"
    def filter(val: any) -> str:
        companyName = str(val["company"])
        startDate = str(val["start"])
        stopDate = str(val["stop"])
        jobTitle = str(val["jobTitle"])
        description = str(val["description"])
        accomplishments = str(val["accomplishments"])
        inst = TemplateCore.instance()
        return (inst.filter("KeepTogether", 
                           inst.filter("DoubleLineEntry", [f"{companyName}",
                                                           f'{startDate} - {stopDate}',
                                                           f'{jobTitle}',
                                                           ""
                                                           ]
                                       ) + description + os.linesep + 
                            inst.filter("Bulleted", val["accomplishments"]) + os.linesep
                            ))
