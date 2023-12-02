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
        return pickle.loads(item)

                 
    def __getitem__(self, key):
        self.__checkState()
        key_bytes = self.__encode(key)
        value_bytes = self.db.Get(key_bytes)
        return self.__decode(value_bytes)
    

    def __setitem__(self, key, value):
        self.__checkState()
        key_bytes = self.__encode(key)
        value_bytes = self.__encode(value)
        self.db.Put(key_bytes, value_bytes)


    def __contains__(self, key):
        try:
            key_bytes = self.__encode(key)
            self.db.Get(key_bytes)
            return True
        except KeyError:
            return False
        
    
    def __len__(self):
        return len(self.keys(iter=False))
    

    def __keys_iter(self):
        for key in self.db.RangeIter(key_from=None, key_to=None, include_value=False):
            yield self.__decode(key)


    def keys(self, iter=False):
        if iter:
            return self.__keys_iter()
        return [key for key in self.__keys_iter()]
    

    def __values_iter(self):
        for key, value in self.db.RangeIter(key_from=None, key_to=None, include_value=True):
            yield self.__decode(value)
    

    def values(self, iter=False):
        if iter:
            return self.__values_iter()
        return [value for value in self.__values_iter()]
    

    def __items_iter(self):
        for key, value in self.db.RangeIter(key_from=None, key_to=None, include_value=True):
            yield (self.__decode(key), self.__decode(value))


    def items(self, iter=False):
        if iter:
            return self.__items_iter()
        return [(key, value) for key, value in self.__items_iter()]
    

    def clear(self):
        for key in self.db.RangeIter(key_from=None, key_to=None, include_value=False):
            self.db.Delete(key)
