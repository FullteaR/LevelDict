import leveldb
import pickle


class LevelDict:
    
    def __init__(self, filepath, create_if_missing=True):
        self.db = leveldb.LevelDB(filepath, create_if_missing=create_if_missing)
        self.open = True

    def __checkState(self):
        assert self.open


    def __encode(self, item):
        return pickle.dumps(item)

    
    def __decode(self, item):
        return pickle.loads

                 
    def __getitem__(self, key):
        self.__checkState()
        key_bytes = self.__encode(key)
        value_bytes = self.db.Get(key)
        return self.__decode(value_bytes)
    

    def __setitem__(self, key, value):
        self.__checkState()
        key_bytes = self.__encode(key)
        value_bytes = self.__encode(value)
        self.db.Put(key, value)


    def __contains__(self, key):
        try:
            self.__getitem__(self.db, key)
            return True
        except KeyError:
            return False
    

    def keys(self, iter=False):
        if iter:
            for key, in self.db.RangeIter(key_from=None, key_to=None, include_value=False):
                yield self.__decode(key
        return [self.__decode(key) for key in self.db.RangeIter(key_from=None, key_to=None, include_value=False)]
    

    def values(self, iter=False):
        if iter:
            for key, value in self.db.RangeIter(key_from=None, key_to=None, include_value=True):
                yield self.__decode(value)
        return [self.__decode(value) for key, value in self.db.RangeIter(key_from=None, key_to=None, include_value=True)]
    

    def items(self, iter=False):
        if iter:
            for key, value in self.db.RangeIter(key_from=None, key_to=None, include_value=True):
                yield (self.__decode(key), self.__decode(value))
        return [(self.__decode(key), self.__decode(value)) for key, value in self.db.RangeIter(key_from=None, key_to=None, include_value=True)]
    



