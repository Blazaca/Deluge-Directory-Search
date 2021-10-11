import os
from pathlib import Path
import re

count = 0
def preset_search(folder):
    if folder == 'SONGS':
        is_SONGS = True
    not_found = []
    synth_dir = Path(folder)
    if os.path.isdir(synth_dir):
        for filename in os.listdir(synth_dir):
            # This is for searching through folders
            if os.path.isdir(f'{synth_dir}/{filename}'):
                nested_path = f'{synth_dir}/{filename}'
                for filename2 in os.listdir(nested_path):
                    if filename2.endswith(".XML"):
                        preset_path = f'{nested_path}/{filename2}'
                        print(f'Searching through patch data... {preset_path}')
                        if is_SONGS:
                            recent_search = sample_search2(preset_path)
                        else:
                            recent_search = sample_search(preset_path)
                        if recent_search:
                            for item in recent_search:
                                not_found.append(item)
                        else:
                            continue
                    else:
                        continue

            elif filename.endswith(".XML"):
                preset_path = f'{synth_dir}/{filename}'
                print(f'Searching through patch data... {preset_path}')
                if is_SONGS:
                    recent_search = sample_search2(preset_path)
                else:
                    recent_search = sample_search(preset_path)
                if recent_search:
                    for item in recent_search:
                        not_found.append(item)
    
    elif not synth_dir.is_dir():
        print('This python file is not inside of a the Deluge root folder!\n'
              'Please place file_fixer.py in the correct spot and run again...')

    print('Search and repair is complete!\n')
    if not_found:
        print('These items could not be found...')
        for item in not_found:
            print(item)
    else:
        print('all files have been repaired!')

def sample_search2(preset_path):
    not_found = []
    patch_path = preset_path
    # look through file for <fileName>
    with open(patch_path) as f:
        index_count = 0
        dir_dict = {}
        for line in f:
            index_count += 1
            if 'fileName' in line:
                # wav_name =([a-zA-Z]+-)*[a-zA-Z0-9]+.wav
                if '[' in line:
                    dir_dict[index_count] = re.search('(((([a-z0-9_]+(-|\s))*)(\[(.*?)\])(-([0-9)]?))?(\.wav)+?))', line, re.IGNORECASE).group(1)
                elif not '.wav' in line:
                    continue
                else:
                    dir_dict[index_count] = re.search('(((([a-z0-9_]+(-|\s))*)([a-z0-9_\s\[\]]+))((\.wav)+?))', line, re.IGNORECASE).group(1)

    # print(f'Found samples names:\n/{dir_dict[12]} @ line 12\n/{dir_dict[26]} @ line 26')
    print('Now searching for corresponding sample files...')
    for index, file in dir_dict.items():
        result = sample_find(file)
        if not result:
            not_found.append(file)
        else:
            dir_dict[index] = result
    print(dir_dict)
    a_file = open(preset_path, "r")
    list_of_lines = a_file.readlines()
    a_file.close()
    a_file = open(preset_path, "w")
    for line, directory in dir_dict.items():
        list_of_lines[line-1] = f'\t\t\t\t\t\tfileName="{directory}">\n'
    a_file.writelines(list_of_lines)
    a_file.close()

    return not_found

def sample_search(preset_path):
    not_found = []
    patch_path = preset_path
    # look through file for <fileName>
    with open(patch_path) as f:
        index_count = 0
        dir_dict = {}
        for line in f:
            index_count += 1
            if '<fileName>' in line:
                # wav_name =([a-zA-Z]+-)*[a-zA-Z0-9]+.wav
                if '[' in line:
                    dir_dict[index_count] = re.search('(((([a-z0-9_]+(-|\s))*)(\[(.*?)\])(-([0-9)]?))?(\.wav)+?))', line, re.IGNORECASE).group(1)
                elif not '.wav' in line:
                    continue
                else:
                    dir_dict[index_count] = re.search('(((([a-z0-9_]+(-|\s))*)([a-z0-9_\s\[\]]+))((\.wav)+?))', line, re.IGNORECASE).group(1)

    # print(f'Found samples names:\n/{dir_dict[12]} @ line 12\n/{dir_dict[26]} @ line 26')
    print('Now searching for corresponding sample files...')
    for index, file in dir_dict.items():
        result = sample_find(file)
        if not result:
            not_found.append(file)
        else:
            dir_dict[index] = result
    print(dir_dict)
    a_file = open(preset_path, "r")
    list_of_lines = a_file.readlines()
    a_file.close()
    a_file = open(preset_path, "w")
    for line, directory in dir_dict.items():
        list_of_lines[line-1] = f"\t\t<fileName>{directory}</fileName>\n"
    a_file.writelines(list_of_lines)
    a_file.close()

    return not_found


def sample_find(sample_name):
    find_flag = True
    while find_flag:

        # for loop + if, elif for /SAMPLES/
        for filename in os.listdir('SAMPLES'):
            if os.path.isdir(f'SAMPLES/{filename}'):

                # for loop + if, elif for example: /SAMPLES/DRUMS
                for filename2 in os.listdir(f'SAMPLES/{filename}'):
                    if os.path.isdir(f'SAMPLES/{filename}/{filename2}'):

                        # for loop + if, elif for example /SAMPLES/DRUMS/LINNDRUM/
                        for filename3 in os.listdir(f'SAMPLES/{filename}/{filename2}'):
                            if os.path.isdir(f'SAMPLES/{filename}/{filename2}/{filename3}'):

                                # for loop + if, elif for example /SAMPLES/DRUM/LINNDRUM/KICK/
                                for filename4 in os.listdir(f'SAMPLES/{filename}/{filename2}/{filename3}'):
                                    if filename4 == sample_name:
                                        return f'SAMPLES/{filename}/{filename2}/{filename3}/{sample_name}'
                                    else:
                                        continue

                            elif filename3 == sample_name:
                                return f'SAMPLES/{filename}/{filename2}/{sample_name}'

                            else:
                                continue

                    elif filename2 == sample_name:
                        return f'SAMPLES/{filename}/{sample_name}'
                    else:
                        continue

            elif filename == sample_name:
                return f'SAMPLES/{sample_name}'
        if 'SAMPLES' not in sample_name:
            return False

preset_search('SONGS')
preset_search('DRUMS')
preset_search('SYNTHS')