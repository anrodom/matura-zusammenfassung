"""
Create the pdf's for the site
"""
import os
import re

nav = []
site_dir = ""
preamble = """
---
header-includes:
  \\usepackage{float}
  \\usepackage{amsmath}
  \\usepackage{cancel}
  \\floatplacement{figure}{H}
---
"""

subjects = ["geographie", "am", "mathematik", "physik"]

up=u"ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ"
lo=u"abcdefghijklmnopqrstuvwxyzäöü"

def define_env(env):
    global nav
    nav = env.conf.get('nav')

def on_post_page_macros(env):

    env._raw_markdown = env._raw_markdown.replace("\\\\\n", "\\\\[11pt]\n")

def on_post_build(env):
    global site_dir
    site_dir = env.conf['site_dir']
    n2l = []
    for n1 in nav:
        for n2 in n1:
            n2s = n1.get(n2)
            n4l = []
            if type(n2s) is list:
                for n3 in n2s:
                    for n4 in n3:
                        n4s = n3.get(n4)
                        n6l = []
                        if type(n4s) is list:
                            for n5 in n4s:
                                for n6 in n5:
                                    n6s = n5.get(n6)
                                    createPDF(n6s, n6)
                                    n6l.append(n6s)
                                    n4l.append(n6s)
                                    n2l.append(n6s)
                        else:
                            createPDF(n4s, n4)
                            n4l.append(n4s)
                            n2l.append(n4s)
                        if n6l != []:
                            createPDF(n6l, n4)
            else:
                createPDF(n2s, n2)
                n2l.append(n2s)
            if n4l != []:
                createPDF(n4l, n2)
    if n2l != []:
        createPDF(n2l, "Main")


def createPDF(md_files, final_file):
    if final_file == "Home":
        return
    t = type(md_files) == list
    d_name = md_files[0] if t else md_files[:-3] + "/file.type"
    path = os.path.join(site_dir, os.path.dirname(d_name), final_file)
    n = "Temp.md"
    # print(md_files, path, d_name)
    with open(n, "w") as f:
        path += ".pdf"
        if t:
            for md_file_rel in md_files:
                if "kurz-" in md_file_rel:
                    continue
                md_file = "docs/" + md_file_rel
                with open(md_file, "r") as m:
                    text = m.readlines()
                    text = replaceText(text)
                    f.writelines(text)
                    f.write('\n')
        else:
            if "kurz-" in md_files:
                return
            md_file = "docs/" + md_files
            with open(md_file, "r") as m:
                text = m.readlines()
                text = replaceText(text)
                f.writelines(text)
                f.write('\n')

    a = f'pandoc -s --pdf-engine=pdflatex "{n}" --resource-path=.:docs/img -o "{path}"'
    print(a)
    os.system(a)


def replaceText(text):
    final = [preamble]
    string = "".join(text)
    string = re.sub(r"\$\$\\begin\{align\}.*?end\{align\}\$\$", replace, string, count=0, flags=re.DOTALL)
    string = string.replace("../../", "../")
    string = re.sub(r"\s\[.*?\]\(.*?\)", links, string)
    for s in string.splitlines(True):
        final.append(s)
    # print(string)
    return final

def replace(obj):
    t = obj[0][2:-2]
    return t

def links(obj):
    s = obj[0].split("]")[0]
    t = s[2:].replace(" ", "-").replace(",", "").replace("(", "").replace(")", "").replace("|", "")
    text = ""
    for i,let in enumerate(t):
        ind = up.find(let)
        if ind > -1:
            text += lo[ind]
        else:
            text += let
    if text in subjects:
        text += "-überblick"
    return s + "](#" + text + ")"
