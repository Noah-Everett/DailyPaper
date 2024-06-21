import os

class ParameterType:
    def __init__(self, name, path, scriptDir):
        self.name = name
        self.path = path
        self.scriptDir = scriptDir

        if not path:
            print(f'Path for {name} was not provided')
            print(f'Setting path for {name} to {scriptDir}/{name}.txt')
            self.path = os.path.join(scriptDir, f'{name}.txt')

        if not self.__check_path_abs(path):
            self.path = os.path.join(scriptDir, path)

        if not self.__check_path_exists(self.path):
            print(f'The file {self.path} does not exist')
            print(f'Making a new file at {self.path}')
            with open(self.path, 'w') as f:
                f.write('')

    def get_name(self):
        return self.name
    def get_path(self):
        return self.path
    def get_scriptDir(self):
        return self.scriptDir
    
    def __check_path_abs(self, path):
        return os.path.isabs(path)
    def __check_path_exists(self, path):
        return os.path.exists(path)
    def __check_path_dir(self, path):
        return os.path.isdir(path)
    def __check_path_file(self, path):
        return os.path.isfile(path)