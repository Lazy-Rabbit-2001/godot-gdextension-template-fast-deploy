def make_doc_header(target, source, env):
    #import zlib

    dst = str(target[0])
    g = open(dst, "w", encoding="utf-8")
    buf = ""
    docbegin = ""
    docend = ""
    for src in source:
        src = str(src)
        if not src.endswith(".xml"):
            continue
        with open(src, "r", encoding="utf-8") as f:
            content = f.read()
        buf += content

    buf = (docbegin + buf + docend).encode("utf-8")

    g.write("/* THIS FILE IS GENERATED, DO NOT EDIT */\n")
    g.write("#ifndef _DOC_DATA_RAW_H\n")
    g.write("#define _DOC_DATA_RAW_H\n")
    g.write("static const int _doc_data_size = " + str(len(buf)) + ";\n")
    g.write("static const char _doc_data[] = {\n")
    for i in range(len(buf)):
        g.write("\t" + str(buf[i]) + ",\n")
    g.write("};\n")

    g.write("#endif")

    g.close()