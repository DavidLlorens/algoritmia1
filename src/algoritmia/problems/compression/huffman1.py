class HuffmanCodeBuilder1: #[full
    def __init__(self, createMap: "-> IMap<Symbol, str>"=dict):
        self.createMap = createMap
        
    def build_tree(self, freq: "IMap<Symbol, Real>") -> "Tree of Symbol": 
        T = [[(freq[symbol], symbol)] for symbol in freq] 
        while len(T) > 1:
            left_tree = min(T) 
            T.remove(left_tree) 
            right_tree = min(T)
            T.remove(right_tree) 
            new_tree = [(left_tree[0][0]+right_tree[0][0],), left_tree, right_tree] 
            T.append( new_tree ) 
        return T[0] #]full
    
    def build_code(self, freq: "IMap<Symbol, Real>") -> "IMap<Symbol, str>":
        code = self.createMap()
        def _build_code(t, prefix):
            if len(t[0]) > 1:
                code[t[0][1]] = prefix
            else:
                _build_code(t[1], prefix + '0')
                _build_code(t[2], prefix + '1')
        tree = self.build_tree(freq)
        _build_code(tree, '')
        return code
