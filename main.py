"""
Create the pdf's for the site
"""
import os

nav = []
site_dir = ""

def define_env(env):
    global nav
    nav = env.conf.get('nav')
#"""
def on_post_build(env):
    global site_dir
    site_dir = env.conf['site_dir']
    file_path = os.path.join(site_dir, "test.html")
    with open(file_path, 'w') as f:
        f.write("Hallo")
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
    t = type(md_files) == list
    d_name = md_files[0] if t else md_files[:-3] + "/file.type"
    path = os.path.join(site_dir, os.path.dirname(d_name), final_file)
    #n = path + ".md"
    n = "Temp.md"
    print(md_files, path, d_name)
    with open(n, "w") as f:
        path += ".pdf"
        if t:
            for md_file_rel in md_files:
                md_file = "docs/" + md_file_rel
                with open(md_file, "r") as m:
                    #print(md_file, path)
                    text = m.readlines()
                    f.writelines(text)
                    f.write('\n')
        else:
            md_file = "docs/" + md_files
            with open(md_file, "r") as m:
                #print(md_file, path)
                text = m.readlines()
                f.writelines(text)
                f.write('\n')
            # m.close()
    a = f'pandoc --pdf-engine=pdflatex "{n}" --resource-path=.:docs:img -o "{path}"'
    print(a)
    os.system(a)
        # f.truncate(0)
    # os.remove(n)
#"""
