import json, re, sys

raw = open('ASSETS_PRESENTASI_BINUS_BDSRC/arena_embed2.html', encoding='utf-8', errors='replace').read()
first_entry = raw.find('{id:"')
start = raw.rfind('[', 0, first_entry)  # '[' immediately before first entry
depth = 0; i = start; instr = False; esc = False
BS = chr(92)
while True:
    c = raw[i]
    if instr:
        if esc: esc = False
        elif c == BS: esc = True
        elif c == '"': instr = False
    else:
        if c == '"': instr = True
        elif c in '[{': depth += 1
        elif c in ']}':
            depth -= 1
            if depth == 0:
                break
    i += 1
arr_text = raw[start:i+1]
print('array length:', len(arr_text))

def fix_keys(m): return '"' + m.group(1) + '":'
txt = re.sub(r'([{,])([A-Za-z_][A-Za-z0-9_]*):', fix_keys, arr_text)
data = json.loads(txt)
json.dump(data, open('ASSETS_PRESENTASI_BINUS_BDSRC/arena_data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('entries:', len(data), '| keys:', list(data[0].keys()))
for d in data:
    print(' -', d['id'], '| metrics:', [(m['label'], m['value']) for m in d.get('metrics', [])],
          '| research:', len(d.get('research', [])), '| pengabdian:', len(d.get('pengabdian', [])), '| status:', d.get('status'))
