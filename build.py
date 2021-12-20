#! /usr/bin/env python

from LatexTemplater.TemplatePluginManager import load_plugins
from LatexTemplater.TemplateCore import TemplateCore
from glob import glob
from typing import List
from copy import deepcopy
import shutil
import os

load_plugins(["Filters"])

def handleFormatMode(main_tex: str, texLoc: str, finalOut: str, formatFile: str, varFiles: List[str]) -> None:
    theseVars = deepcopy(varFiles)
    theseVars.append(formatFile)
    inst = TemplateCore.instance()
    inst.generate(main_tex, texLoc, varFiles=theseVars)
    finalName = extensionLessName(formatFile) + ".pdf"
    shutil.move(os.path.join(texLoc, main_tex + ".pdf"), os.path.join(finalOut, finalName))

def extensionLessName(fileName: str) -> str:
    return fileName.split("/")[-1].split(".")[0]
    
if __name__ == '__main__':
    inst = TemplateCore.instance()
    inst.templateDir = "Templates"
    inst.resultsFolder = "TexFolder"
    formatModes = glob("FormattingVars/*.json")
    varFiles=glob("data/*.json")
    if len(formatModes) > 1:
        commonFile = "FormattingVars/Common.json"
        if commonFile in formatModes:
            formatModes.remove(commonFile)
            varFiles.append(commonFile)
        for formatFile in formatModes:
            handleFormatMode("Resume", "TexFolder", "Output", formatFile, varFiles)
