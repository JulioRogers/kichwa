import sys
import yaml
import re

from typing import (Optional,List,cast)
from Kichwa.repl import *

_KICHWA_: str = """ 
##    ##   ####    ######    ##     ##   ##      ##      ###    
##   ##     ##    ##    ##   ##     ##   ##  ##  ##     ## ##   
##  ##      ##    ##         ##     ##   ##  ##  ##    ##   ##  
#####       ##    ##         #########   ##  ##  ##   ##     ## 
##  ##      ##    ##         ##     ##   ##  ##  ##   ######### 
##   ##     ##    ##    ##   ##     ##   ##  ##  ##   ##     ## 
##    ##   ####    ######    ##     ##    ###  ###    ##     ##
"""



def show_cover(version):
    global _KICHWA_
    print('-'*106)
    print(
        f'\n\nBienvenido a Kichwa v{version}, Un lenguaje de programacion en Kichwa basado en JavaScript\n\n{_KICHWA_}')
    print('-'*106)


def show_head(version):
    print(f'Kichwa v{version} | Salir: llukshina() | Actualizar: update()')


def get_configs():
    with open('configs.yaml', 'r') as fin:
        configs = yaml.load(fin, Loader=yaml.FullLoader)
    return dict(configs)


def presentation_config(configs, params, exe_file=False):
    version = configs['version']
    if not params is None:
        if exe_file:
            if '-cover' in params:
                show_cover(version)
                return
            show_head(version)
        else:
            if not '-ncover' in params:
                show_cover(version)
                return
            show_head(version)
    else:
        if exe_file:
            show_head(version)
        else:
            show_cover(version)




def main(path=None, params=None) -> None:
    configs = get_configs()
    if not params is None and '-version' in params:
        version = configs['version']
        print(f'Kichwa v{version}')
        return
    if path is None:
        presentation_config(configs, params, exe_file=False)
        start_repl()
    elif not path is None:
        presentation_config(configs, params, exe_file=True)

        src = read_module(path)
        if not src is None:
            start_repl(src, path)


def filter_path_params(args):
    path = list(filter(lambda s: not re.match('(\S+?\.kw$)', s) is None, args))
    params = list(filter(lambda s: s.startswith('-'), args))
    if len(path) > 0:
        path = path[0]
    else:
        path = None

    if len(params) == 0:
        params = None

    return path, params


if __name__ == '__main__':
    args: List[str] = sys.argv

    if len(args) > 1:
        path, params = filter_path_params(args)
    else:
        path, params = None, None
    try:
        main(path, params)
    except KeyboardInterrupt:
        print('\n↳ Rikunakushun(Adios) \n')
