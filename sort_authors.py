#!/usr/bin/env python3

entries = {}

with open('author-list.tex') as f:
    d = f.readlines()
    e = ''
    author = ''
    num = 0
    for line in d:
        num += 1
        if line.startswith('%'):
            # Comments at the end.
            break
        if not line.strip():
            # blank line between entries
            #print(f"On line number {num}: '{line[:-1]}'")
            assert(author != '')
            entries[author] = e
            e = ''
            author = ''
            continue
        if not author:
            # first line of the block is the author's name
            assert(line.startswith('\\author{'))
            author = line[8:-2].split(' ')[-1]
            print(f"Found {author}")
        e += line

print(f"Found {len(entries)} authors")

with open('new-list.tex', 'w') as f:
    f.write('\n')
    f.write(entries['Lowe-Power'])
    f.write('\n')
    del entries['Lowe-Power']

    for author,entry in sorted(entries.items()):
        f.write(entry)
        f.write('\n')
