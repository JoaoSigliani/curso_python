from abc import ABC, abstractmethod
from pathlib import Path

LOG_FILE = Path(__file__).parent / "log.txt"

class Log(ABC):
    @abstractmethod
    def _log(self, msg): ...
    
    def log_error(self, msg):
        return self._log(f'Erro: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Sucesso: {msg}')
    
class LogFileMixin(Log):
    def _log(self, msg):
        with open(LOG_FILE, 'a', encoding='utf8') as file:
            file.write(f'{msg} ({self.__class__.__name__})\n')
    
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')
        
if __name__ == '__main__':
    lp = LogPrintMixin()
    lf = LogFileMixin()
    
    lp.log_error("Deu erro")
    lp.log_success("Deu certo")
    
    lf.log_error("Deu erro")
    lf.log_success("Deu certo")
    