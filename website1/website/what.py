import os, json, time
try: import stonksPath._JsonNotFoundError as jnfe
except ImportError: import _JsonNotFoundError as jnfe
class Path:
    """Parses configuration information from a type: 'JSON' file.
    Methods Aliases:
     __get__ : get
     workingDirectory : workingDir, wd
     __paths__ : _show__
     __getfiles__ : __files__, __findfiles__ 
     createjson : json, writejson, __cj__, createJson
    """
    def __init__(self, fileName : str = 'path.json', *args, InvalidKey = None, **kwargs) -> None:
        """Parameteres:
            1.PathJson
             >takes in the path/file-name of the .json file
        --------------------------------------------------
        Loads .json file as a dictionary
        Kwargs:
         >InvalidKey = None | default return value for Path's .__get__() method.
        """
        wd_dir, f_dir = os.getcwd().replace('\\', '/', 1), os.path.dirname(__file__)
        fileName = fileName if fileName.endswith('.json') else f"{fileName}.json"
        if os.path.isfile(fileName): pass #if in path/working directory
        elif os.path.isfile(f'{wd_dir}/{fileName}'):fileName = f'{wd_dir}/{fileName}'
        elif os.path.isfile(f'{f_dir}/{fileName}'):fileName = f'{f_dir}/{fileName}'
        else: raise jnfe.JsonNotFoundError(fileName)
        self.pathJson ,self.InvalidKey = fileName ,InvalidKey
        with open(fileName, 'r') as path:
            self.path = json.load(path)
            
    def __get__(self, key, newkeyError = None):
        """get() method for stonkspath
        Functions the same as a dict.get(*args) method"""
        if newkeyError:
            return self.path.get(key, newkeyError)
        return self.path.get(key, self.InvalidKey)
        
    def workingDirectory(self):
        """returns current working directory"""
        return os.getcwd()
    
    def __paths__(self) -> None:
        """Prints all Paths from dictionary"""
        for name, path in self.path.items():
            print('{:20s}|{:10s}\n'.format(name, path))
        
    @staticmethod
    def __getfiles__(*args, fullpath:bool = False, timer = False, specify = (''), includeOnly: bool = False, **kwargs):
        """finds and prints all files inside of working directory
        **kwargs
         >fullpath : bool = False | Gets Fullpath
         >specify : tuple = None | Exclude specific file types
         >timer : bool = False | Prints time taken to find all file and their respective paths
        """
        start = time.perf_counter()
        paths = dict()
        p = '' if fullpath == True else os.getcwd()
        if isinstance(specify, tuple): specify = tuple([ext if ext.startswith('.') else f'.{ext}' for ext in specify if isinstance(ext, str)])
        elif isinstance(specify, str): specify = (specify if specify.startswith('.') else f'.{specify}',)
        else: raise TypeError("'specify' should be a instance of the tuple class")
        paths['working directory'] = os.getcwd()
        if includeOnly != True: #ugly solution but effeciency>
            for root, _, files in os.walk(os.getcwd()):
                for file in files:
                    if not file.endswith(specify): paths[file] = os.path.join(root, file).replace(p, '')
        else: #boilerplate
            for root, _, files in os.walk(os.getcwd()):
                for file in files:
                    if file.endswith(specify): paths[file] = os.path.join(root, file).replace(p, '')
        if timer == True or set(map(kwargs.get, {'t', 'time'})).intersection({'true', 'True', True, 1}):
            print(f'time elapsed: {round((time.perf_counter()-start)*1000, 1)} miliseconds.') 
        return paths
    
    @classmethod #alternate constructor
    def createjson(cls, *args, fileName:str = 'path.json', **kwargs):
        """alternate Constructor for Path class. Creates Json file with all folders in working directory.
        Calls __getfiles__ staticmethod.
        -------------**kwargs----------------------------------
         >fileName : str = 'path.json'
        -----------|__getfiles__---**kwargs|-------------------
         >fullpath : bool  = False | Gets Fullpath
         >specify  : tuple = None | Exclude specific file types
         >timer    : bool  = False | Prints time taken to find all file and their respective paths
        -----------|__init__--------**kwargs|-------------------
         >InvalidKey = None | default return value for Path's .__get__() method.
        """
        if not fileName.endswith('.json'): fileName = f'{fileName}.json'
        with open(fileName, "w") as outfile:
            json.dump(cls.__getfiles__(**kwargs), outfile)
        return cls(fileName = fileName, **kwargs)
