# a script to rename recordings

# renames files with no prefix+number i.e. a-recorded in a toaster
# to a{len(prefix(a))+1}-recorded in a toaster i.e. a4-recorded in a toaster

from os import getcwd
from os import rename
from os import listdir


to_sort = [
    'clips',
    'songs'
]

for folder in to_sort:

    directory = f'{getcwd()}/{folder}'
    files, prefixes, to_process = listdir(directory), {}, []

    for clip in files:
        clip_split = clip.split('-', 1)
        key = clip_split[0][:1]
        prefixes.setdefault(key, 0)
        if len(clip_split[0]) < 2:
            to_process.append(clip)
        else:
            value = int(clip_split[0][1:].split('.', 1)[0])
            if int(prefixes[key]) < value:
                prefixes[key] = value

    for k in prefixes:
        print(k, prefixes[k])

    for i in to_process:
        i_split = i.split('-', 1)
        k = i_split[0][:1]
        new_name = f'{k}{int(prefixes[k]) + 1}-{i_split[1]}'
        print('renaming', i, 'to', new_name)
        try:
            rename(f'{directory}/{i}', f'{directory}/{new_name}')
            print('✅')
            prefixes[k] = int(prefixes[k]) + 1
        except NotImplementedError:
            print('❌')
