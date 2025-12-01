import os
from typing import Optional
from .code import CodeFrame


class ProgramFrame(object):
    
    def __init__(
        self,
        code_or_path:str,
        subset:Optional[str]=None,
    ) -> None:
        self.subset = subset
        if os.path.isfile(code_or_path):
            self.code = self._get_code_file(path=code_or_path)
        else:
            self.code = code_or_path
                
        self._serialized = self._get_code_components(self.code)
        
        self.name = self._serialized['info'].get('name', '')
        self.desc = self._serialized['info'].get('desc', '')
        self.codeframe = CodeFrame(self._serialized['code'])
        
    def __repr__(self):
        return f'< Program {self.subset}::{self.name} >'
    
    def to_dict(self):
        return self._serialized
    
    def keys(self):
        return self._serialized.keys()
                
    def _get_code_components(
        self,
        code:str
    ) -> dict:
        _var_define, _main_code_info = code.split('###Code###')
        try:
            _desc_idx = _main_code_info.index('#Desc')
            _name_idx = _main_code_info.index('#Name')
            _resl_idx = _main_code_info.index('#Result')
        except Exception as e:
            raise f'{self.subset}::{str(e)}'
        _main_code = _main_code_info[:_resl_idx]
        _desc = _main_code_info[_desc_idx:].split(':')[-1].strip()
        _name = _main_code_info[_name_idx:_desc_idx].split(':')[-1].strip()
        _result = _main_code_info[_resl_idx:_name_idx].split(':')[-1].strip()
        return dict(
            code = dict(
                var = _var_define,
                main = _main_code,
                result = _result,
            ),
            info = dict(
                name = _name,
                desc = _desc,
            )
        )
        
    def _get_code_file(
        self,
        path:str
    ) -> str:
        with open(path, 'r') as f:
            return f.read()