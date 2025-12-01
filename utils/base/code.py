from copy import deepcopy
import signal
import types

class CodeRunningError(object): pass        
class CodeFrame(object):
    
    def __init__(
        self,
        serialized_code:dict,
    ) -> None:
        self.serialized_code = serialized_code
        self.var_define = serialized_code['var']
        self._main_code = serialized_code['main']
        self.var_result = serialized_code['result']
        
        self.main_code_lines = self.get_code_lines(self._main_code)
        self._exec_line = 0
        
        self.global_vars = {}
        
        self.true_result, self.true_vars = self._get_ground_truth()
        self.true_code_lines = deepcopy(self.main_code_lines)

    def __getstate__(self):
        state = self.__dict__.copy()
        if 'global_vars' in state:
            del state['global_vars']
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.global_vars = {}
        
    def get_code_lines(self, code:str):
        return [
            line
            for line
            in code.split('\n')
            if len(line) > 0
        ]
        
    def __len__(self):
        return len(self.main_code_lines)
        
    def reset(self):
        self.global_vars = {}
        self.load_variables()
        self._exec_line = 0
        
    @property
    def vars(self):
        return {k:v for k,v in self.global_vars.items() if k[:2]!='__' and not isinstance(v, types.ModuleType)}
    
    @property
    def result(self):
        return self.global_vars.get(self.var_result, None)
    
    def load_variables(self):
        exec(self.var_define, self.global_vars)
        
    def step(self):
        if self._exec_line >= len(self):
            raise StopIteration
        else:
            exec(self.main_code_lines[self._exec_line], self.global_vars)
            
    def run(self):
        def handler(signum, frame):
            raise TimeoutError("Execution timed out")
        
        old_handler = signal.signal(signal.SIGALRM, handler)
        signal.alarm(2)
        
        try:
            self.reset()
            exec('\n'.join(self.main_code_lines), self.global_vars)
        except:
            self.global_vars[self.var_result] = CodeRunningError
        finally:
            signal.alarm(0)
            signal.signal(signal.SIGALRM, old_handler)
        
    def _get_ground_truth(self):
        self.reset()
        self.run()
        _gt_result, _gt_vars = self.result, self.vars
        self.reset()
        return _gt_result, _gt_vars
    
    def copy(self):
        return deepcopy(self)