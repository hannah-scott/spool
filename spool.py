import sqlite3
import json
import yaml

def state2txt(state, states):
  idxs=["one","two","three","four","five"]
  ss = states.split(",")
  if state == "none":
    return ""
  return idxs[ss.index(state)]

with open("db.yaml", "r") as f:
  data = yaml.load(f, Loader=yaml.FullLoader)

for collection in data.values():
  for item in collection["items"]:
    item["state"] = state2txt(item["state"], collection["states"])

jsond = "\x00".join(json.dumps(data)) + "\x00"

jsonb = jsond.encode('ascii')

tapeDB="file.sqlite"
con = sqlite3.connect(tapeDB)
c = con.cursor()


x=c.execute('''
UPDATE ItemTable
SET value=(?)
WHERE key='tapedata'
''', [jsonb])

con.commit()