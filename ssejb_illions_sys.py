TIER1_ROOTS = {
    'ones': list(map(lambda s: s.split('/'), ['m/unt', 'b/doe/duo', 'tr/tret', 'quadr/quattuor', 'quint/quin', 'sext/sex', 'sept/septen', 'oct/octo', 'non/novem'])),
    'tens': ['deci', 'viginti', 'triginti', 'quadraginti', 'quinquaginti', 'sexaginti', 'septuaginti', 'octoginti', 'nonaginti'],
    'hundreds': ['cent', 'ducent', 'trecent', 'quadringent', 'quingent', 'sescent', 'septingent', 'octingent', 'nongent']
}

TIER2_ROOTS = {
    'ones': list(map(lambda s: s.split('/'), ['milli/me', 'micro/due', 'nano/tre/trio', 'pico/tetre', 'femto/pente', 'atto/hexe', 'zepto/hepte', 'yocto/octe', 'xono/enne'])),
    'tens': [['vec', 'c'], 'icos', 'triacont', 'tetracont', 'pentacont', 'hexacont', 'heptacont', 'octacont', 'ennacont'],
    'hundreds': ['hect', 'dohect', 'triahect', 'tetrahect', 'pentahect', 'hexahect', 'heptahect', 'octahect', 'ennahect']
}
TIER2_SPECIAL_ONES_ROOTS = ['unt', 'duot', 'tret']
TIER2_SPECIAL_ONES_ABBR = ['Ut', 'Dt', 'Trt']

TIER3_ROOTS = {
    'ones': list(map(lambda s: s.split('/'), ['killa/hen/ena', 'mega/do/da', 'giga/tra', 'tera/te', 'peta/pe', 'exa/ex/ecta', 'zetta/ze/zeta', 'yotta/yo/yota', 'xenna/ne/xena'])),
    'tens': list(map(lambda s: s.split('/'), ['daka/ka', 'ika/ik/ic', 'traka/trak/trac', 'teka/tek/tec', 'peka/pek/pec', 'exaka/exak/exac', 'zaka/zak/zac', 'yoka/yok/yoc', 'neka/nek/nec'])),
    'hundreds': list(map(lambda s: s.split('/'), ['hota/hot/ho', 'bota/bot/bo', 'trota/trot/tro', 'tota/tot/to', 'pota/pot/po', 'exota/exot/exo', 'zota/zot/zo', 'yoota/yoot/yoo', 'nota/not/no']))
}

TIER1_ABBR = {
    'ones': list(map(lambda s: s.split('/'), ['M/U', 'B/D', 'T', 'Qa', 'Qi', 'Sx', 'Sp', 'O', 'N'])),
    'tens': ['Dc', 'V', 'Tg', 'Qag', 'Qig', 'Sxg', 'Spg', 'Og', 'Ng'],
    'hundreds': ['Ce', 'Dce', 'Tce', 'Qae', 'Qie', 'Sxce', 'Spe', 'Oe', 'Noe']
}

TIER2_ABBR = {
    'ones': list(map(lambda s: s.split('/'), ['Mi/Me', 'Mc/De', 'Na/Tr', 'Pc/Tt', 'Fm/Pt', 'At/Hx', 'Zp/Hp', 'Yc/Ot', 'Xn/En'])),
    'tens': ['Vc', 'Is', 'Trc', 'Ttc', 'Ptc', 'Hxc', 'Hpc', 'Otc', 'Enc'],
    'hundreds': ['Ht', 'Deht', 'Trht', 'Ttht', 'Ptht', 'Hxht', 'Hpht', 'Otht', 'Enht']
}

TIER3_ABBR = {
    'ones': list(map(lambda s: s.split('/'), ['Kla/H/Ea', 'Mga/Do/Da', 'Ga/Ta', 'Tea/Te', 'Pta/P', 'Exa/E/Ec', 'Zta/Z/Za', 'Yta/Y/Ya', 'Xea/Ne/Xa'])),
    'tens': list(map(lambda s: s.split('/'), ['Dka/Ka', 'Ika/Ik/Ic', 'Trka/Trk/Trc', 'Teka/Tek/Tec', 'Peka/Pek/Pec', 'Eka/Exk/Exc', 'Zka/Zk/Zc', 'Yka/Yk/Yc', 'Nka/Nk/Nc'])),
    'hundreds': list(map(lambda s: s.split('/'), ['Ha/Ho', 'Ba/Bo', 'Tra/Tro', 'Toa/To', 'Poa/Po', 'Eta/Exo', 'Zta/Zo', 'Yta/Yo', 'Nta/No']))
}

def gen_class1_separator(n, prefix=False, *, abbr=False):
    if n >= 1000 or n <= 0:
        raise ValueError('第一类分隔符的索引必须在 1~999 中。')
    ones = n % 10
    tens = (n // 10) % 10
    hundreds = (n // 100) % 10
    
    if abbr:
        if tens == hundreds == 0:
            if ones == 1 and prefix:
                separator = ''
            else:
                separator = TIER1_ABBR['ones'][ones - 1][-1 if prefix else 0]
        else:
            ones_root = '' if ones == 0 else TIER1_ABBR['ones'][ones - 1][-1]
            tens_root = '' if tens == 0 else TIER1_ABBR['tens'][tens - 1]
            hundreds_root = '' if hundreds == 0 else TIER1_ABBR['hundreds'][hundreds - 1]
            separator = ones_root + tens_root + hundreds_root
        
        if prefix and (hundreds > 0 or tens > 0):
            separator += 'i'
        
        return separator
    
    if tens == hundreds == 0:
        if ones == 1 and prefix:
            separator = ''
        else:
            separator = TIER1_ROOTS['ones'][ones - 1][-1 if prefix else 0]
            if prefix and ones == 3:
                separator = separator.rstrip('t')
    elif tens > 0 and hundreds == 0:
        ones_root = '' if ones == 0 else TIER1_ROOTS['ones'][ones - 1][1].rstrip('t')
        tens_root = TIER1_ROOTS['tens'][tens - 1].rstrip('i')
        separator = ones_root + tens_root
    elif hundreds > 0 and tens == 0:
        if ones == 1 or ones == 3:
            ones_root = TIER1_ROOTS['ones'][ones - 1][1]
            hundreds_root = TIER1_ROOTS['hundreds'][hundreds - 1].rstrip('t')
            separator = hundreds_root + ones_root
        else:
          ones_root = '' if ones == 0 else TIER1_ROOTS['ones'][ones - 1][-1]
          hundreds_root = TIER1_ROOTS['hundreds'][hundreds - 1]
          separator = ones_root + hundreds_root
    elif hundreds > 0 and tens > 0:
        ones_root = '' if ones == 0 else TIER1_ROOTS['ones'][ones - 1][1].rstrip('t')
        tens_root = TIER1_ROOTS['tens'][tens - 1]
        hundreds_root = TIER1_ROOTS['hundreds'][hundreds - 1]
        separator = ones_root + tens_root + hundreds_root
    
    if prefix and (hundreds > 0 or tens > 0):
        separator += 'i'
    
    return separator


def gen_class2_separator(n, prefix=False, *, abbr=False):
    if n >= 1000 or n <= 0:
        raise ValueError('第二类分隔符的索引必须在 1~999 中。')
    ones = n % 10
    tens = (n // 10) % 10
    hundreds = (n // 100) % 10
    
    if abbr:
        if tens == hundreds == 0:
            separator = TIER2_ABBR['ones'][ones - 1][0]
        else:
            ones_root = '' if ones == 0 else TIER2_ABBR['ones'][ones - 1][-1]
            tens_root = '' if tens == 0 else TIER2_ABBR['tens'][tens - 1]
            hundreds_root = '' if hundreds == 0 else TIER2_ABBR['hundreds'][hundreds - 1]
            separator = ones_root + tens_root + hundreds_root
        
        if prefix:
            separator += 'e'
        
        return separator
    
    if tens == hundreds == 0:
        separator = TIER2_ROOTS['ones'][ones - 1][0]
    elif hundreds == 0 and tens == 1:
        if ones == 0:
            separator = TIER2_ROOTS['tens'][tens - 1][0] + 'o'
        else:
            ones_root = TIER2_ROOTS['ones'][ones - 1][1]
            tens_root = TIER2_ROOTS['tens'][tens - 1][1] + 'o'
            separator = ones_root + tens_root
    elif hundreds == 0 and tens > 1:
        ones_root = '' if ones == 0 else TIER2_ROOTS['ones'][ones - 1][-1]
        tens_root = TIER2_ROOTS['tens'][tens - 1] + 'o'
        separator = ones_root + tens_root
    elif hundreds > 0 and tens == 0:
        ones_root = '' if ones == 0 else TIER2_ROOTS['ones'][ones - 1][-1]
        hundreds_root = TIER2_ROOTS['hundreds'][hundreds - 1] + 'o'
        separator = ones_root + hundreds_root
    elif hundreds > 0 and tens == 1:
        if ones == 0:
            tens_root = TIER2_ROOTS['tens'][tens - 1][0] + 'e'
            hundreds_root = TIER2_ROOTS['hundreds'][hundreds - 1] + 'o'
            separator = tens_root + hundreds_root
        else:
            ones_root = '' if ones == 0 else TIER2_ROOTS['ones'][ones - 1][1]
            tens_root = TIER2_ROOTS['tens'][tens - 1][1] + 'e'
            hundreds_root = TIER2_ROOTS['hundreds'][hundreds - 1] + 'o'
            separator = ones_root + tens_root + hundreds_root
    elif hundreds > 0 and tens > 1:
        ones_root = '' if ones == 0 else TIER2_ROOTS['ones'][ones - 1][-1]
        tens_root = TIER2_ROOTS['tens'][tens - 1] + 'e'
        hundreds_root = TIER2_ROOTS['hundreds'][hundreds - 1] + 'o'
        separator = ones_root + tens_root + hundreds_root
    
    if prefix:
        separator = separator.rstrip('aeiou') + 'e'
    
    return separator


def gen_class3_separator(n, *, abbr=False):
    if n >= 1000 or n <= 0:
        raise ValueError('第三类分隔符的索引必须在 1~999 中。')
    ones = n % 10
    tens = (n // 10) % 10
    hundreds = (n // 100) % 10
    
    if abbr:
        res = ['', '', '']
        if hundreds == tens == 0:
            res[2] = TIER3_ABBR['ones'][ones - 1][0]
        elif tens == 1:
            if ones == 0:
                res[1] = TIER3_ABBR['tens'][tens - 1][0]
            else:
                res[2] = TIER3_ABBR['tens'][tens - 1][1 if ones == 2 else 0]
                res[1] = TIER3_ABBR['ones'][ones - 1][1]
        elif tens > 1:
            if ones == 0:
                res[1] = TIER3_ABBR['tens'][tens - 1][0]
            else:
                res[2] = TIER3_ABBR['ones'][ones - 1][0 if ones == 4 or ones == 5 else 1 if ones == 3 else 2]
                res[1] = TIER3_ABBR['tens'][tens - 1][1 if ones in {1, 6, 8} else 2]
        
        if hundreds > 0:
            if tens == ones == 0:
                res[0] = TIER3_ABBR['hundreds'][hundreds - 1][0]
            else:
                if tens == 0:
                    res[2] = TIER3_ABBR['ones'][ones - 1][0 if ones == 4 or ones == 5 else 1 if ones == 3 else 2]
                res[0] = TIER3_ABBR['hundreds'][hundreds - 1][1]
        
        separator = ''.join(res)
        
        return separator
    
    ones_roots = TIER3_ROOTS['ones'][ones - 1]
    tens_roots = TIER3_ROOTS['tens'][tens - 1]
    hundreds_roots = TIER3_ROOTS['hundreds'][hundreds - 1]
    
    res = ['', '', '']
    
    if hundreds == tens == 0:
        res[2] = ones_roots[0]
    elif tens == 1:
        if ones == 0:
            res[1] = tens_roots[0]
        else:
            res[1] = ones_roots[1]
            res[2] = tens_roots[1 if ones == 2 else 0]
    elif tens > 1:
        if ones == 0:
            res[1] = tens_roots[0]
        else:
            res[2] = ones_roots[0 if ones == 4 or ones == 5 else 1 if ones == 3 else 2]
            res[1] = tens_roots[1 if ones in {1, 6, 8} else 2]
            if ones == 2:
                res[1] += 'o'
    
    if hundreds > 0:
        if tens == ones == 0:
            res[0] = hundreds_roots[0]
        else:
            if tens == 1 and ones == 1:
                res[1] = res[1][1:]
            elif tens == 0:
                res[2] = ones_roots[0 if ones == 4 or ones == 5 else 1 if ones == 3 else 2]
                if ones == 2:
                    res[1] += 'o'
            next_root = res[1] if res[1] else res[2]
            res[0] = hundreds_roots[1 if next_root[0] in {'a', 'e', 'i', 'o', 'u'} else 2]
        
    separator = ''.join(res)
    
    return separator


def gen_tier1_illion(n, *, check_argu=True, abbr=False):
    if check_argu and not 0 < n <= 999:
        raise ValueError('第一层级前缀索引必须是 0~999 中的整数。')
    if abbr:
        return gen_class1_separator(n, abbr=True), f'1e{3 * n + 3}'
    return gen_class1_separator(n) + 'illion', f'1e{3 * n + 3}'


def gen_tier2_illion(groups, *, check_argu=True, abbr=False):
    if check_argu:
        if not isinstance(groups, dict):
            raise ValueError(f'第二类组必须是一个字典。')
        for k, v in groups.items():
            if not (isinstance(k, int) and 0 <= k <= 999):
                raise ValueError(f'第二类组索引 "{k}" 非法，第二类组索引必须是 0~999 中的整数。')
            if not (isinstance(v, int) and 0 < v <= 999):
                raise ValueError(f'第一层级前缀索引 "{v}" 非法，第一层级前缀索引必须是 1~999 中的整数。')

    group0 = groups[0] if 0 in groups and groups[0] != 0 else None
    groups = {k: groups[k] for k in sorted(groups, reverse=True) if k and groups[k]}

    if len(groups) == 0 and group0 is None:
        return ''

    prefixes = []
    values = []
    for tier2_prefix_i, tier1_prefix_i in groups.items():
        tier2_prefix = gen_class2_separator(tier2_prefix_i, abbr=abbr)
        tier1_prefix = gen_class1_separator(tier1_prefix_i, True, abbr=abbr)
        
        prefixes.append(tier1_prefix + tier2_prefix)
        values.append(f'{tier1_prefix_i * 3}e{tier2_prefix_i * 3}')
    
    if group0 is not None:
        values.append(str(3 * group0 + 3))
        if group0 in {1, 2, 3}:
            prefixes.append((TIER2_SPECIAL_ONES_ABBR if abbr else TIER2_SPECIAL_ONES_ROOTS)[group0 - 1])
        else:
            prefixes.append(gen_class1_separator(group0, abbr=abbr))
    else:
        values.append('3')
        if not abbr:
            prefixes[-1] = prefixes[-1].rstrip('aeiou')
    
    illion = '-'.join(prefixes) + ('' if abbr else 'illion')
    
    return illion, f"1e({' + '.join(values)})"


def gen_tier3_illion(class3_groups, tier2_groups=None, *, check_argu=True, abbr=False):
    def sort_class3_groups(d):
        def create_sorted_key(original_key):
            if len(original_key) == 3:
                a, b, c = original_key
                sorted_c = tuple(sorted(c))
                return (a, b, sorted_c)
            else:
                return original_key
        
        def key_func(k):
            a, b = k[0], k[1]
            has_c = len(k) == 3
            if has_c:
                c = k[2]
                sorted_c = sorted(c, key=lambda elem: (-elem[0], -elem[1]))
                sorted_c_tuple = tuple(sorted_c)
            else:
                sorted_c_tuple = ()
            return (a, b, has_c, sorted_c_tuple)
        
        sorted_keys = sorted(d.keys(), key=key_func)
        return {create_sorted_key(k): d[k] for k in sorted_keys}

    def values_key_func(s):
        splited = tuple(map(int, s.split('e')))
        
        if len(splited) == 1:
            return (-1,)
        return splited[::-1]
    
    if check_argu:
        if not isinstance(class3_groups, dict):
            raise ValueError(f'第三类组索引必须是一个字典。')
        for other_prefixes, tier1_prefix_i in class3_groups.items():
            if len(other_prefixes) == 2:
                tier3_prefix_i, tier2_prefix_i = other_prefixes
                tier3_embed_tier2_prefix_groups = None
            elif len(other_prefixes) == 3:
                tier3_prefix_i, tier2_prefix_i, tier3_embed_tier2_prefix_groups = other_prefixes
            else:
                raise ValueError(f'第三类组索引 "{other_prefixes}" 非法，长度必须为三或二。')
            if not (isinstance(tier3_prefix_i, int) and 0 < tier3_prefix_i <= 999):
                raise ValueError(f'第三类组索引 "{other_prefixes}" 非法，第三层级前缀索引必须是在 1~999 中的整数。')
            if not (isinstance(tier2_prefix_i, int) and 0 < tier2_prefix_i <= 999):
                raise ValueError(f'第三类组索引 "{other_prefixes}" 非法，第二层级前缀索引必须是在 1~999 中的整数。')
            if not (isinstance(tier1_prefix_i, int) and 0 < tier1_prefix_i <= 999):
                raise ValueError(f'第三类组索引 "{other_prefixes}" 的第一层级前缀索引非法，第一层级前缀索引必须是在 1~999 中的整数。')
            if tier3_embed_tier2_prefix_groups is not None and not isinstance(tier3_embed_tier2_prefix_groups, tuple):
                raise ValueError(f'第三类组索引 "{other_prefixes}" 非法，第二三层级嵌套前缀组必须是一个元组。')
            
            if tier3_embed_tier2_prefix_groups is not None:
                for prefixes_i in tier3_embed_tier2_prefix_groups:
                    if not (isinstance(prefixes_i, tuple) and len(prefixes_i) == 2 and all(map(lambda i: isinstance(i, int), prefixes_i))):
                        raise ValueError(f'第三类组索引 "{other_prefixes}" 中第二三层级嵌套前缀索引 "{prefixes_i}" 非法，第二三层级嵌套前缀索引必须是一个长度为二的整数元组。')
                    inner_tier3_prefix_i, inner_tier2_prefix_i = prefixes_i
                    if not 0 <= inner_tier3_prefix_i < tier3_prefix_i:
                        raise ValueError(f'第三类组索引 "{other_prefixes}" 中第二三层级嵌套前缀索引 "{prefixes_i}" 非法，内部第三层级前缀索引必须是在 0~999 中的整数，且小于外部第三层级前缀索引（{tier3_prefix_i}）。')
                    if not 0 < inner_tier2_prefix_i <= 999:
                        raise ValueError(f'第三类组索引 "{other_prefixes}" 中第二三层级嵌套前缀索引 "{prefixes_i}" 非法，内部第二层级前缀索引必须是在 1~999 中的整数。')
        
    class3_groups = sort_class3_groups(class3_groups)
    tier3_roots = []
    values = []
    for other_prefixes, tier1_prefix_i in class3_groups.items():
        if len(other_prefixes) == 2:
            tier3_prefix_i, tier2_prefix_i = other_prefixes
            tier3_embed_tier2_prefix_groups = None
        else:
            tier3_prefix_i, tier2_prefix_i, tier3_embed_tier2_prefix_groups = other_prefixes
        
        tier1_prefix = gen_class1_separator(tier1_prefix_i, True, abbr=abbr)
        tier2_prefix = '' if tier2_prefix_i == 1 else gen_class2_separator(tier2_prefix_i, True, abbr=abbr)
        tier3_prefix = gen_class3_separator(tier3_prefix_i, abbr=abbr)

        tier3_prefix_values = []
        tier3_prefix_values.append(f'{tier2_prefix_i * 3}e{tier3_prefix_i * 3}')

        if tier3_embed_tier2_prefix_groups is not None:
            tier3_embed_tier2_prefixes = ''
            tier3_embed_tier2_prefixes_end_in_tier2_prefix = False
            for inner_tier3_prefix_i, inner_tier2_prefix_i in tier3_embed_tier2_prefix_groups:
                inner_tier2_prefix = gen_class2_separator(inner_tier2_prefix_i, abbr=abbr) if inner_tier3_prefix_i == 0 else '' if inner_tier2_prefix_i == 1 else gen_class2_separator(inner_tier2_prefix_i, True, abbr=abbr)
                inner_tier3_prefix = '' if inner_tier3_prefix_i == 0 else gen_class3_separator(inner_tier3_prefix_i, abbr=abbr)
                
                tier3_embed_tier2_prefix = inner_tier2_prefix + inner_tier3_prefix
                if inner_tier3_prefix_i == 0:
                    tier3_prefix_values.append(str(inner_tier2_prefix_i * 3))
                    tier3_embed_tier2_prefixes_end_in_tier2_prefix = True
                else:
                    tier3_prefix_values.append(f'{inner_tier2_prefix_i * 3}e{inner_tier3_prefix_i * 3}')
                tier3_embed_tier2_prefixes = tier3_embed_tier2_prefix + tier3_embed_tier2_prefixes
            
            if not tier3_embed_tier2_prefixes_end_in_tier2_prefix:
                tier3_embed_tier2_prefixes = tier3_embed_tier2_prefixes.rstrip('aeiou') + 'o'
            
            tier3_roots.insert(0, tier1_prefix + tier2_prefix + tier3_prefix + tier3_embed_tier2_prefixes)
        else:
            tier3_roots.insert(0, (tier1_prefix + tier2_prefix + tier3_prefix).rstrip('aeiou') + 'o')
        values.insert(0, f'{tier1_prefix_i * 3}e({" + ".join(sorted(tier3_prefix_values, key=values_key_func, reverse=True))})')
    
    tier3_illion = '-'.join(tier3_roots)
    if tier2_groups is not None and isinstance(tier2_groups, dict) and list(tier2_groups.values()).count(0) != len(tier2_groups):
        tier2_and_tier1_illion, tier2_values = gen_tier2_illion(tier2_groups, abbr=abbr)
        tier2_values = tier2_values[3:-1]
        values.append(tier2_values)
        illion = tier3_illion + '-' + tier2_and_tier1_illion
    elif abbr:
        illion = tier3_illion
    else:
        illion = tier3_illion.rstrip('aeiou') + 'illion'
    
    return illion, f"1e({' + '.join(values)})"

print(gen_tier2_illion({12: 45, 0: 75, 978: 44, 1: 42}))
print(gen_tier2_illion({12: 45, 0: 75, 978: 44, 1: 42}, abbr=True))
print(gen_tier1_illion(427))
print(gen_tier1_illion(427, abbr=True))
