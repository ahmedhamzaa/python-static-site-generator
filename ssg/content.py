from importlib.abc import Loader
from importlib.metadata import metadata
import re
from yaml import (load ,FullLoader)
from collections.abc import Mapping

class Content(Mapping):
    __delimeter="^(?:-|\+){3}\s*$"
    __regex=re.compile(__delimeter,re.MULTILINE)

    def __init__(self,metadata,content):
        self.data=metadata
        self.data.add("content",content)

    @classmethod
    def load(cls,string):
        _,fm,content=cls.__regex.split(string,2)
        cls.load(fm,Loader=FullLoader)
        return cls(_,content)
    
    @property
    def body(self):
        return self.data["content"]
    
    @property
    def type(self):
        if "type" in self.data:
            return self.data["type"]
        return None
    
    @type.setter
    def type(self,type):
        self.data["type"]=type
    
    def __getitem__(self,key):
        return self.data[key]
    
    def __iter__(self):
        iter(self.data)
    
    def __len__(self):
        return len(self.data)
    
    def __repr__(self):
        data={}
        for key,value in self.data.items():
            if key =="content":
                data[key]=value
        return str(data)
