import os, mimetypes, re

vids = []
subs = []

for f in os.listdir():
    try:
        if mimetypes.guess_type(f)[0].startswith('video'):
            vids.append(f)
    except AttributeError:
        if f.endswith(".srt"):
            subs.append(f)

expr = r"S\d\dE\d\d"
for v in vids:
    epizode = re.findall(expr, v)
    if len(epizode)>0:
        epizode = epizode[0]
    else:
        continue
    for s in subs:
        if epizode in s:
            v_name = os.path.splitext(v)[0]
            s_name = v_name + ".srt"
            os.rename(s, s_name)
            break
    print(s + "->" + s_name)
