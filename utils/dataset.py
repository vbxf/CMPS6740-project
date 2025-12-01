import os
from .base import ProgramFrame

class ProgramDataset(object):
    
    def __init__(
        self,
        path:str,
    ) -> None:
        self.programs, self.subsets = self._load_set(path)
        
    def __len__(self):
        return len(self.programs)
    
    def __getitem__(self, key):
        return self.programs[key]
    
    def __repr__(self):
        return f'< ProgramDataset: {self.subsets} >'
    
    def _load_set(
        self,
        path:str
    ) -> list:
        _programs, _subsets = [], []
        for _dir_name in os.listdir(path):
            _dir_path = os.path.join(path, _dir_name)
            if os.path.isdir(_dir_path):
                _programs += self._load_subset(path, _dir_name)
                _subsets.append(_dir_name)
        return _programs, _subsets
        
    
    def _load_subset(
        self,
        path:str,
        subset_name:str,
    ) -> list:
        _full_path = os.path.join(path, subset_name)
        _programs = []
        for _file_name in os.listdir(_full_path):
            _programs.append(
                ProgramFrame(
                    os.path.join(_full_path, _file_name),
                    subset = subset_name
                )
            )
        return _programs
        