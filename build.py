#! /usr/bin/env python

from LatexTemplater.TemplatePluginManager import load_plugins
from LatexTemplater.TemplateCore import TemplateCore

load_plugins(["Filters"])

if __name__ == '__main__':
    inst = TemplateCore.instance()
    inst.templateDir = "Templates"
    inst.resultsFolder = "Output"
    inst.generate("Resume", "Output", varFiles=["vars.json"])
