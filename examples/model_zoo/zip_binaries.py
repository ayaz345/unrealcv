from build_binaries import uprojects
from unrealcv.automation import get_platform_name
import os, zipfile

def zip_dir(dirpath, zippath):
    # fzip = zipfile.ZipFile(zippath, 'w', zipfile.ZIP_DEFLATED, allowZip64 = True)
    fzip = zipfile.ZipFile(zippath, 'w', zipfile.ZIP_STORED, allowZip64 = True)
    basedir = f'{os.path.dirname(dirpath)}/'
    for root, dirs, files in os.walk(dirpath):
        if os.path.basename(root)[0] == '.':
            continue #skip hidden directories
        dirname = root.replace(basedir, '')
        for f in files:
            # if f[-1] == '~' or (f[0] == '.' and f != '.htaccess'):
            #     #skip backup files and all hidden files except .htaccess
            #     continue
            fzip.write(f'{root}/{f}', f'{dirname}/{f}')
    fzip.close()

if __name__ == '__main__':
    platform_name = get_platform_name()
    plugin_version = '0.3.9'
    for uproject in uprojects:
        uproject_name = os.path.basename(uproject['uproject_path']).split('.')[0]
        binary_folder = os.path.join('Binaries', uproject_name)

        if not os.path.isdir(binary_folder):
            print(f'Binary folder {binary_folder} not exist, skip this one')
            continue

        print(f'Zipping {uproject_name} ...')
        zip_dir(binary_folder, f'{uproject_name}_{platform_name}_{plugin_version}.zip')
