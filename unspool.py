import sqlite3
import json
import yaml

def txt2state(txt, states):
  idxs=["one","two","three","four","five"]
  ss = states.split(",")
  if txt == "":
    return "none"
  return ss[idxs.index(txt)]

tapeDB="file.sqlite"
con = sqlite3.connect(tapeDB)
c = con.cursor()

x=c.execute("SELECT * FROM ItemTable")

fetched=x.fetchall()

# Data is stored in a binary encoding
tapedata = fetched[-1][1].decode("ascii").replace("\0", "")
data = json.loads(tapedata)

for collection in data.values():
  for item in collection["items"]:
    item["state"] = txt2state(item["state"], collection["states"])

with open("db.yaml", "w") as f:
  f.write(yaml.dump(data))

