TIER1_ROOTS = {
    'ones': list(map(lambda s: s.split('/'), ['m/unt', 'b/doe/duo', 'tr/tret', 'quadr/quattuor', 'quint/quin', 'sext/sex', 'sept/septen', 'oct/octo', 'non/novem'])),
    'tens': ['deci', 'viginti', 'triginti', 'quadraginti', 'quinquaginti', 'sexaginti', 'septuaginti', 'octoginti', 'nonaginti'],
    'hundreds': ['cent', 'ducent', 'trecent', 'quadringent', 'quingent', 'sescent', 'septingent', 'octingent', 'nongent']
}

TIER2_ROOTS = {
    'ones': list(map(lambda s: s.split('/'), ['milli/me', 'micro/due', 'nano/tre/trio', 'pico/tetre', 'femto/pente', 'atto/hexe', 'zepto/hepte', 'yocto/octe', 'xono/enne'])),
    'tens': [['vec', 'c'], 'icos', 'triacont', 'tetracont', 'pentacont', 'hexacont', 'heptacont', 'octacont', 'ennacont'],
    'hundreds': ['hecto', 'dohecto', 'triahecto', 'tetrahecto', 'pentahecto', 'hexahecto', 'heptahecto', 'octahecto', 'ennahecto']
}
GROUP0_SPECIAL_ONES_ROOTS = ['unt', 'duot', 'tret']
GROUP0_SPECIAL_ONES_ABBR = ['Ut', 'Dt', 'Trt']

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

def gen_tier1_separatrix(n, prefix=False, *, abbr=False):
    if n >= 1000 or n <= 0:
        raise ValueError('第一层级分界线的索引必须在 1~999 以内。')
    ones = n % 10
    tens = (n // 10) % 10
    hundreds = (n // 100) % 10
    
    if abbr:
        if tens == hundreds == 0:
            if ones == 1 and prefix:
                separatrix = ''
            else:
                separatrix = TIER1_ABBR['ones'][ones - 1][-1 if prefix else 0]
        else:
            ones_root = '' if ones == 0 else TIER1_ABBR['ones'][ones - 1][-1]
            tens_root = '' if tens == 0 else TIER1_ABBR['tens'][tens - 1]
            hundreds_root = '' if hundreds == 0 else TIER1_ABBR['hundreds'][hundreds - 1]
            separatrix = ones_root + tens_root + hundreds_root
        
        if prefix and (hundreds > 0 or tens > 0):
            separatrix += 'i'
        
        return separatrix
    
    if tens == hundreds == 0:
        if ones == 1 and prefix:
            separatrix = ''
        else:
            separatrix = TIER1_ROOTS['ones'][ones - 1][-1 if prefix else 0]
            if prefix and ones == 3:
                separatrix = separatrix.rstrip('t')
    elif tens > 0 and hundreds == 0:
        ones_root = '' if ones == 0 else TIER1_ROOTS['ones'][ones - 1][1].rstrip('t')
        tens_root = TIER1_ROOTS['tens'][tens - 1].rstrip('i')
        separatrix = ones_root + tens_root
    elif hundreds > 0 and tens == 0:
        if ones == 1 or ones == 3:
            ones_root = TIER1_ROOTS['ones'][ones - 1][1]
            hundreds_root = TIER1_ROOTS['hundreds'][hundreds - 1].rstrip('t')
            separatrix = hundreds_root + ones_root
        else:
          ones_root = '' if ones == 0 else TIER1_ROOTS['ones'][ones - 1][-1]
          hundreds_root = TIER1_ROOTS['hundreds'][hundreds - 1]
          separatrix = ones_root + hundreds_root
    elif hundreds > 0 and tens > 0:
        ones_root = '' if ones == 0 else TIER1_ROOTS['ones'][ones - 1][1].rstrip('t')
        tens_root = TIER1_ROOTS['tens'][tens - 1]
        hundreds_root = TIER1_ROOTS['hundreds'][hundreds - 1]
        separatrix = ones_root + tens_root + hundreds_root
    
    if prefix and (hundreds > 0 or tens > 0):
        separatrix += 'i'
    
    return separatrix


def gen_tier2_separatrix(n, prefix=False, *, abbr=False):
    if n >= 1000 or n <= 0:
        raise ValueError('第二层级分界线的索引必须在 1~999 以内。')
    ones = n % 10
    tens = (n // 10) % 10
    hundreds = (n // 100) % 10
    
    if abbr:
        if tens == hundreds == 0:
            separatrix = TIER2_ABBR['ones'][ones - 1][0]
        else:
            ones_root = '' if ones == 0 else TIER2_ABBR['ones'][ones - 1][-1]
            tens_root = '' if tens == 0 else TIER2_ABBR['tens'][tens - 1]
            hundreds_root = '' if hundreds == 0 else TIER2_ABBR['hundreds'][hundreds - 1]
            separatrix = ones_root + tens_root + hundreds_root
        
        if prefix:
            separatrix += 'e'
        
        return separatrix
    
    if tens == hundreds == 0:
        separatrix = TIER2_ROOTS['ones'][ones - 1][0]
    elif hundreds == 0 and tens == 1:
        if ones == 0:
            separatrix = TIER2_ROOTS['tens'][tens - 1][0] + 'o'
        else:
            ones_root = TIER2_ROOTS['ones'][ones - 1][1]
            tens_root = TIER2_ROOTS['tens'][tens - 1][1] + 'o'
            separatrix = ones_root + tens_root
    elif hundreds == 0 and tens > 1:
        ones_root = '' if ones == 0 else TIER2_ROOTS['ones'][ones - 1][-1]
        tens_root = TIER2_ROOTS['tens'][tens - 1] + 'o'
        separatrix = ones_root + tens_root
    elif hundreds > 0 and tens == 0:
        ones_root = '' if ones == 0 else TIER2_ROOTS['ones'][ones - 1][-1]
        hundreds_root = TIER2_ROOTS['hundreds'][hundreds - 1]
        separatrix = ones_root + hundreds_root
    elif hundreds > 0 and tens == 1:
        if ones == 0:
            tens_root = TIER2_ROOTS['tens'][tens - 1][0] + 'e'
            hundreds_root = TIER2_ROOTS['hundreds'][hundreds - 1]
            separatrix = tens_root + hundreds_root
        else:
            ones_root = '' if ones == 0 else TIER2_ROOTS['ones'][ones - 1][1]
            tens_root = TIER2_ROOTS['tens'][tens - 1][1] + 'e'
            hundreds_root = TIER2_ROOTS['hundreds'][hundreds - 1]
            separatrix = ones_root + tens_root + hundreds_root
    elif hundreds > 0 and tens > 1:
        ones_root = '' if ones == 0 else TIER2_ROOTS['ones'][ones - 1][-1]
        tens_root = TIER2_ROOTS['tens'][tens - 1] + 'e'
        hundreds_root = TIER2_ROOTS['hundreds'][hundreds - 1]
        separatrix = ones_root + tens_root + hundreds_root
    
    if prefix:
        separatrix = separatrix.rstrip('aeiou') + 'e'
    
    return separatrix


def gen_tier3_separatrix(n, *, abbr=False):
    if n >= 1000 or n <= 0:
        raise ValueError('第三层级分界线的索引必须在 1~999 以内。')
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
        
        separatrix = ''.join(res)
        
        return separatrix
    
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
        
    separatrix = ''.join(res)
    
    return separatrix


def gen_tier1_illion(n, *, check_argu=True, abbr=False):
    if check_argu and not 0 < n <= 999:
        raise ValueError('第一层级前缀索引必须在 0~999 以内。')
    if abbr:
        return gen_tier1_separatrix(n, abbr=True), f'1e{3 * n + 3}'
    return gen_tier1_separatrix(n) + 'illion', f'1e{3 * n + 3}'


def gen_tier2_illion(groups, *, check_argu=True, abbr=False):
    if check_argu:
        if not isinstance(groups, dict):
            raise ValueError(f'第二类组映射表必须是一个字典。')
        
        for k, v in groups.items():
            if not (isinstance(k, int) and 0 <= k <= 999):
                raise ValueError(f'第二层级分界线索引 "{k}" 非法，必须在 0~999 以内。')
            if not (isinstance(v, int) and 0 < v <= 999):
                raise ValueError(f'第一层级分界线索引 "{v}" 非法，必须在 1~999 以内。')
        
        if max(groups.keys()) == 0:
            raise ValueError(f'第二类组映射表非法，其中最大的第二层级分界线索引不能为 0.')
            
    group0 = groups.get(0)
    groups = {k: groups[k] for k in sorted(groups, reverse=True) if k}

    if len(groups) == 0 and group0 is None:
        return ''

    class2_separactor = []
    values = []
    for tier2_separatrix_i, tier1_separatrix_i in groups.items():
        tier2_separatrix = gen_tier2_separatrix(tier2_separatrix_i, abbr=abbr)
        tier1_separatrix = gen_tier1_separatrix(tier1_separatrix_i, True, abbr=abbr)
        
        class2_separactor.append(tier1_separatrix + tier2_separatrix)
        values.append(f'{tier1_separatrix_i * 3}e{tier2_separatrix_i * 3}')
    
    if group0 is not None:
        values.append(str(3 * group0 + 3))
        if group0 in {1, 2, 3}:
            class2_separactor.append((GROUP0_SPECIAL_ONES_ABBR if abbr else GROUP0_SPECIAL_ONES_ROOTS)[group0 - 1])
        else:
            class2_separactor.append(gen_tier1_separatrix(group0, abbr=abbr))
    else:
        values.append('3')
        if not abbr:
            class2_separactor[-1] = class2_separactor[-1].rstrip('aeiou')
    
    illion = '-'.join(class2_separactor) + ('' if abbr else 'illion')
    
    return illion, f"1e({' + '.join(values)})"


def gen_tier3_illion(class2_groups, *, check_argu=True, abbr=False):
    def sort_groups(d):        
        sorted_keys = sorted(d.keys(), key=lambda k: ((k - 10000, ), ) if isinstance(k, int) else tuple(sorted(k, key=lambda elem: (-elem[0], -elem[1]))), reverse=True)
        return {k if isinstance(k, int) else tuple(sorted(k, reverse=True)): d[k] for k in sorted_keys}

    if check_argu:
        if not isinstance(class2_groups, dict):
            raise ValueError(f'第二类组映射表必须是一个字典。')
        for class3_groups_or_tier2_separatrix_i, tier1_separatrix_i in class2_groups.items():
            if not (isinstance(tier1_separatrix_i, int) and 0 < tier1_separatrix_i <= 999):
                raise ValueError(f'第二类组映射表的键 "{class3_groups_or_tier2_separatrix_i}" 的第一层级分界线索引 "{tier1_separatrix_i}" 非法，必须在 1~999 以内。')
            
            if isinstance(class3_groups_or_tier2_separatrix_i, tuple):
                class3_groups = class3_groups_or_tier2_separatrix_i
            
                max_tier3_separatrix_i = max(class3_groups, key=lambda i: i[0])[0]
                existing_tier3_separatrixes_i = set()
                
                if max_tier3_separatrix_i == 0:
                    raise ValueError(f'第三类组映射表 "{class3_groups}" 非法，第三类组映射表的最大第三层级分界线索引不能为 0。')
                
                for tier3_separatrix_i, tier2_separatrix_i in class3_groups:
                    if not (isinstance(tier2_separatrix_i, int) and 0 < tier2_separatrix_i <= 999):
                        raise ValueError(f'第三类组映射表 "{class3_groups}" 的第三类组索引 "{tier3_separatrix_i}" 的第二层级分界线索引 "{tier2_separatrix_i}" 非法，必须在 1~999 以内。')
                    if not (isinstance(tier3_separatrix_i, int) and 0 <= tier3_separatrix_i <= 999):
                        raise ValueError(f'第三类组映射表 "{class3_groups}" 的第三类组索引 "{tier3_separatrix_i}" 非法，必须在 0~999 以内。')
                    if tier3_separatrix_i in existing_tier3_separatrixes_i:
                        raise ValueError(f'第三类组映射表 "{class3_groups}" 的第三类组索引 "{tier3_separatrix_i}" 非法，第三类组映射表的第三层级分界线索引不能重复。')
                    else:
                        existing_tier3_separatrixes_i.add(tier3_separatrix_i)
            elif isinstance(class3_groups_or_tier2_separatrix_i, int):
                tier2_separatrix_i = class3_groups_or_tier2_separatrix_i
                if not 0 <= tier2_separatrix_i <= 999:
                    raise ValueError(f'第二层级分界线索引 "{tier2_separatrix_i}" 非法，必须在 0~999 以内。')
            else:
                raise ValueError(f'第二类组映射表的键 "{class3_groups_or_tier2_separatrix_i}" 非法，必须是元组或整数类型。')

    class2_groups = sort_groups(class2_groups)
    class2_groups_with_tier3 = {}
    class2_groups_without_tier3 = {}
     
    for k, v in class2_groups.items():
        if isinstance(k, int):
            class2_groups_without_tier3[k] = v
        else:
            class2_groups_with_tier3[k] = v

    class2_separators_with_tier3 = []
    values = []

    for class3_groups, tier1_separatrix_i in class2_groups_with_tier3.items():
        tier1_separatrix = gen_tier1_separatrix(tier1_separatrix_i, True, abbr=abbr)
        
        class2_separator_with_tier3 = ''
        class2_separator_with_tier3_values = []
        end_in_tier2_separatrix = False
        for tier3_separatrix_i, tier2_separatrix_i in class3_groups:
            if tier3_separatrix_i == 0:
                end_in_tier2_separatrix = True
                tier2_separatrix = gen_tier2_separatrix(tier2_separatrix_i, abbr=abbr)
                
                class2_separator_with_tier3 += tier2_separatrix
                class2_separator_with_tier3_values.append(str(tier2_separatrix_i * 3))
            else:
                tier2_separatrix = '' if tier2_separatrix_i == 1 else gen_tier2_separatrix(tier2_separatrix_i, True, abbr=abbr)
                tier3_separatrix = gen_tier3_separatrix(tier3_separatrix_i, abbr=abbr)
                
                class2_separator_with_tier3 += tier2_separatrix + tier3_separatrix
                class2_separator_with_tier3_values.append(f'{tier2_separatrix_i * 3}e{tier3_separatrix_i * 3}')
        if not end_in_tier2_separatrix:
            class2_separator_with_tier3 = class2_separator_with_tier3.rstrip('aeiou') + 'o'
        
        class2_separators_with_tier3.append(tier1_separatrix + class2_separator_with_tier3)
        values.append(f"{3 * tier1_separatrix_i}e({' + '.join(class2_separator_with_tier3_values)})")
    
    illion_class2_separators_with_tier3 = '-'.join(class2_separators_with_tier3)
    if len(class2_groups_without_tier3) == 0:
        illion = illion_class2_separators_with_tier3 if abbr else illion_class2_separators_with_tier3.rstrip('aeiou') + 'illion'
    elif max(class2_groups_without_tier3) == 0:
        group0 = class2_groups_without_tier3[0]
        if group0 in {1, 2, 3}:
            illion = illion_class2_separators_with_tier3 + '-' + (GROUP0_SPECIAL_ONES_ABBR if abbr else GROUP0_SPECIAL_ONES_ROOTS)[group0 - 1]
        else:
            illion = illion_class2_separators_with_tier3 + '-' + gen_tier1_separatrix(group0, abbr=abbr)
        
        if not abbr:
            illion += 'illion'
        values.append(str(3 * group0 + 3))
    else:
        illion_class2_separators_without_tier3, class2_separators_without_tier3_values = gen_tier2_illion(class2_groups_without_tier3, abbr=abbr)
        class2_separators_without_tier3_values = class2_separators_without_tier3_values[3:-1]
        values.append(class2_separators_without_tier3_values)
        illion = illion_class2_separators_with_tier3 + '-' + illion_class2_separators_without_tier3
    
    return illion, f"1e({' + '.join(values)})"


print(gen_tier1_illion(571))
print(gen_tier3_illion({((106, 1), ): 1, ((5, 10), (4, 157)): 57, 0: 571, 5: 157, 45: 145, 999: 999}))
