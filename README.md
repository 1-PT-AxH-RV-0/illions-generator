# -illion 数生成器

## 简介
这是一个生成 -illion 数（即以 -illion 结尾的数词）的 Python 脚本。其基于[斯比斯·赛比安的扩展乔纳森·鲍尔 -illions 系统（Sbiis Saibian's Extended Jonathan Bower's -illions System）](https://sites.google.com/site/largenumbers/home/2-4/2-4-8-bowers-illions)构造 -illion 数，支持第一层级至第三层级，之后可能会支持第四层级。

主脚本是 `ssejb_illions_sys.py`，其中 `gen_tier1_illion`, `gen_tier2_illion`, `gen_tier3_illion` 用于生成 -illion 数，`gen_class1_separator`, `gen_class2_separator`, `gen_class3_separator` 用于生成类分隔符，用法详见[函数文档](#函数文档)。

关于斯比斯·赛比安的扩展乔纳森·鲍尔 -illions 系统对层级分界线和 -ilion 数的命名法，请见[命名法](Nomenclature.md)。

之后应该会考虑将此脚本做成模块上传到 `pypi` 上。

## 函数文档

### `gen_class1_separator`

#### 函数签名
```python
def gen_class1_separator(n, prefix=False, *, abbr=False):
```

#### 概述
此函数用于生成第一层级分界线。

#### 参数说明
##### 1. `n` (必需)
- **类型**：`int`
- **描述**：
  第一层级分界线索引，1~999 以内，超出范围时抛出异常。

##### 2. `prefix` (可选)
- **类型**：`bool`
- **默认值**：`False`
- **描述**：
  返回前缀格式。

##### 3. `abbr` (可选，关键字参数)
- **类型**：`bool`
- **默认值**：`False`
- **描述**：
  返回缩写格式。

#### 返回值
- **类型**：`str`
- **描述**：
  第一层级分界线。

---

### `gen_class2_separator`

#### 函数签名
```python
def gen_class2_separator(n, prefix=False, *, abbr=False):
```

#### 概述
此函数用于生成第二层级分界线。

#### 参数说明
##### 1. `n` (必需)
- **类型**：`int`
- **描述**：
  第二层级分界线索引，1~999 以内，超出范围时抛出异常。

##### 2. `prefix` (可选)
- **类型**：`bool`
- **默认值**：`False`
- **描述**：
  返回前缀格式。

##### 3. `abbr` (可选，关键字参数)
- **类型**：`bool`
- **默认值**：`False`
- **描述**：
  返回缩写格式。

#### 返回值
- **类型**：`str`
- **描述**：
  第二层级分界线。

---

### `gen_class3_separator`

#### 函数签名
```python
def gen_class3_separator(n, *, abbr=False):
```

#### 概述
此函数用于生成第三层级分界线。

#### 参数说明
##### 1. `n` (必需)
- **类型**：`int`
- **描述**：
  第三层级分界线索引，1~999 以内，超出范围时抛出异常。

##### 2. `abbr` (可选，关键字参数)
- **类型**：`bool`
- **默认值**：`False`
- **描述**：
  返回缩写格式。

#### 返回值
- **类型**：`str`
- **描述**：
  第三层级分界线。

---

### `gen_tier1_illion`

#### 函数签名
```python
def gen_tier1_illion(n, *, check_argu=True, abbr=False):
```

#### 概述
此函数用于生成第一层级的 -illion 数，同时返回用科学计数法表示的值及其序号。

#### 参数说明

##### 1. `n` (必需)
- **类型**：`int`
- **描述**：
  第一层级分界线索引，1~999 以内。
  
##### 2. `check_argu` (可选，关键字参数)
- **类型**：`bool`
- **默认值**：`True`
- **描述**：
  启用时自动校验字典键值合法性，禁用后跳过校验。

##### 3. `abbr` (可选，关键字参数)
- **类型**：`bool`
- **默认值**：`False`
- **描述**：
  控制返回名称是否为缩写形式（仅影响命名部分）。

#### 返回值
```python
tuple[str, str, str]  # (-illion 数, 科学计数法, 序号)
```
- **-illion 数**：根据 `abbr` 生成的完整 -illion 数（如 `septenvigintiquadringentillion`）或缩写（如 `SpVQae`）
- **科学计数法**：-illion 数对应的值
- **序号**：-illion 数的序号

#### 异常处理
当 `check_argu=True` 时，可能会抛出 `ValueError`，触发条件：第一层级分界线索引超出 1~999 范围

#### 使用示例

##### 完整输出模式
```python
print(gen_tier1_illion(427))
```
输出：
```python
('septenvigintiquadringentillion', 
 '1e1284')
```

##### 缩写输出模式
```python
print(gen_tier1_illion(427, abbr=True))
```
输出：
```python
('SpVQae', 
 '1e1284')
```

#### 科学计数法规则
```plaintext
科学计数法 = 1e(3*第一层级分界线索引 + 3)
```

---

### `gen_tier2_illion`

#### 函数签名
```python
def gen_tier2_illion(groups, *, check_argu=True, abbr=False):
```

#### 概述
此函数用于生成第二层级的 -illion 数，同时返回用科学计数法表示的值及其序号。

#### 参数说明

##### 1. `groups` (必需)
- **类型**：`dict`
- **描述**：
  定义第二类组的映射关系。  

  格式：
  - 键：第二层级分界线索引（0~999 的整数）
  - 值：第一层级分界线索引（1~999 的整数）

##### 2. `check_argu` (可选，关键字参数)
- **类型**：`bool`
- **默认值**：`True`
- **描述**：
  启用时自动校验字典键值合法性，禁用后跳过校验。

##### 3. `abbr` (可选，关键字参数)
- **类型**：`bool`
- **默认值**：`False`
- **描述**：
  控制返回名称是否为缩写形式（仅影响命名部分）。

#### 返回值
```python
tuple[str, str, str]  # (-illion 数, 科学计数法, 序号)
```
- **-illion 数**：根据 `abbr` 生成的完整 -illion 数（如 `quattuorquadraginti...illion`）或缩写（如 `QaQagi...Spg`）
- **科学计数法**：-illion 数对应的值
- **序号**：-illion 数的序号

#### 异常处理
当 `check_argu=True` 时，可能会抛出 `ValueError`，触发条件：
1. 第二类组映射表非字典类型
2. 第二层级分界线索引超出 0~999 范围
3. 第一层级分界线索引超出 1~999 范围
4. 第二类组映射表的最大的第二层级分界线索引为 0

#### 使用示例

##### 完整输出模式
```python
print(gen_tier2_illion({12: 45, 0: 75, 978: 44, 1: 42}))
```
输出：
```python
('quattuorquadragintiocteheptaconteennahecto-quinquadragintidueco-doequadragintimilli-quinseptuagintillion', 
 '1e(132e2934 + 135e36 + 126e3 + 228)')
```

##### 缩写输出模式
```python
print(gen_tier2_illion({12: 45, 0: 75, 978: 44, 1: 42}, abbr=True))
```
输出：
```python
('QaQagiOtHpcEnht-QiQagiDeVc-DQagiMi-QiSpg', 
 '1e(132e2934 + 135e36 + 126e3 + 228)')
```

#### 科学计数法规则
对于 `第二层级分界线索引 ＞ 0` 的情况：
```plaintext
每个第二类组贡献项 = (3 * 第一层级分界线索引)e(3 * 第二层级分界线索引)
```
对于 `第二层级分界线索引 ＝ 0` 的情况：
```plaintext
每个第二类组贡献项 = 3 * 第一层级分界线索引 + 3
```
最终结果：
```plaintext
科学计数法 = 1e(各个第二类组贡献项相加)
```

---

### `gen_tier3_illion`

#### 函数签名
```python
def gen_tier3_illion(class2_groups, *, check_argu=True, abbr=False):
```

#### 概述
此函数用于生成第三层级的 -illion 数，同时返回用科学计数法表示的值及其序号。

#### 参数说明

##### 1. `class2_groups` (必需)
- **类型**：`dict`
- **描述**：
  定义第二类组的映射关系。
  
  格式：
  - 键：
    
    有两种格式：
    1. 表示第三类组映射表
       - 格式：
         第三类组映射表，形如 `((第三层级分界线索引, 第二层级分界线索引), ...)` 的元组（实际上是用元组表示的字典）
       - 索引约束：
         - 第三层级分界线索引：0~999 的整数，且一个第二&三层级分界线映射表中最大的第三层级分界线索引不能为 0，同时单个个第二&三层级分界线映射表中不能出现重复的第三层级分界线索引
         - 第二层级分界线索引：1~999 的整数
    2. 表示第二层级分界线索引（0~999 的整数）
  - 值：第一层级分界线索引（1~999 的整数）

##### 2. `check_argu` (可选，关键字参数)
- **类型**：`bool`
- **默认值**：`True`
- **描述**：
  启用时自动校验字典键值合法性，禁用后跳过校验。

##### 3. `abbr` (可选，关键字参数)
- **类型**：`bool`
- **默认值**：`False`
- **描述**：
  控制返回名称是否为缩写形式（仅影响命名部分）。

#### 返回值
```python
tuple[str, str, str]  # (-illion 数, 科学计数法, 序号)
```
- **-illion 数**：根据 `abbr` 生成的完整 -illion 数（如 `dokaocta...septingentillion`）或缩写（如 `DoKaOtc...Spe`）
- **科学计数法**：-illion 数对应的值
- **序号**：-illion 数的序号

#### 异常处理
当 `check_argu=True` 时，可能抛出 `ValueError`，触发条件：
1. 第二类组映射表非字典类型
2. 第二类组映射表的键非元组或数字类型
3. 第二类组映射表的第一层级分界线索引超出 1~999 范围
4. 当第二类组映射表的键表示第三类组映射表时：
   1. 单个第三类组映射表的最大第三层级分界线索引为 0
   2. 单个第三类组映射表存在重复的第三层级分界线索引
   3. 第三类组映射表的第三层级分界线索引超出 0~999 范围
   4. 第三类组映射表的第二层级分界线索引超出 1~999 范围
5. 当第二类组映射表的键表示第二层级分界线索引时，其值超出 1~999 范围

如果 `tier2_groups` 不为 `None`，则还可能抛出 `gen_tier2_illion` 函数可能抛出的异常。

#### 使用示例

##### 完整输出模式
```python
print(gen_tier3_illion({
    ((2, 13), (0, 1), (1, 14)): 5,
    ((6, 13), (0, 1), (1, 14)): 5,
    ((6, 13), (0, 1), (1, 15)): 5,
    ((6, 13), (0, 2), (1, 15)): 5,
    ((6, 13), (4, 15), (3, 110)): 120,
    ((17, 13), (8, 15), (7, 110)): 120,
    ((672, 13), (27, 15), (45, 110)): 120,
    ((0, 1), (4, 1)): 120,
    ((3, 1), ): 120
}, {15: 1, 4: 1}))
```
输出：
```python
('viginticentitreceexozacodavecehectetecpetapenteceiczeto-viginticentitrecezedakapenteceyottavecehectezetto-viginticentitreceexapenteceteravecehectegigo-quintreceexapentecekillamicro-quintreceexapentecekillamilli-quintreceexatetrecekillamilli-viginticentiteramilli-viginticentigigo-quintrecemegatetrecekillamilli-penteco-picillion', 
 '1e(3e(39e2016 + 330e135 + 45e81) + 3e(39e51 + 45e24 + 330e21) + 3e(39e18 + 45e12 + 330e9) + 3e(39e18 + 45e3 + 6) + 3e(39e18 + 45e3 + 3) + 3e(39e18 + 42e3 + 3) + 3e(3e12 + 3) + 3e(3e9) + 3e(39e6 + 42e3 + 3) + 3e45 + 3e12 + 3)')
```

##### 缩写输出模式
```python
print(gen_tier3_illion({
    ((2, 13), (0, 1), (1, 14)): 5,
    ((6, 13), (0, 1), (1, 14)): 5,
    ((6, 13), (0, 1), (1, 15)): 5,
    ((6, 13), (0, 2), (1, 15)): 5,
    ((6, 13), (4, 15), (3, 110)): 120,
    ((17, 13), (8, 15), (7, 110)): 120,
    ((672, 13), (27, 15), (45, 110)): 120,
    ((0, 1), (4, 1)): 120,
    ((3, 1), ): 120
}, {15: 1, 4: 1}, abbr=True))
```
输出：
```python
('VCeiTrVceExoZcDaVcHteTecPtaPtVceIcZo-VCeiTrVceZDkaPtVceYtaVcHteZto-VCeiTrVceExaPtVceTeaVcHteGo-QiTrVceExaPtVceKlaMc-QiTrVceExaPtVceKlaMi-QiTrVceExaTtVceKlaMi-VCeiTeaMi-VCeiGo-QiTrVceMgaTtVceKlaMi-PtVc-Pc', 
 '1e(3e(39e2016 + 330e135 + 45e81) + 3e(39e51 + 45e24 + 330e21) + 3e(39e18 + 45e12 + 330e9) + 3e(39e18 + 45e3 + 6) + 3e(39e18 + 45e3 + 3) + 3e(39e18 + 42e3 + 3) + 3e(3e12 + 3) + 3e(3e9) + 3e(39e6 + 42e3 + 3) + 3e45 + 3e12 + 3)')
```

#### 科学计数法规则
- 当第二类组映射表的键表示第二层级分界线索引时：
  - 对于 `第二层级分界线索引 ＞ 0` 的情况：
    ```plaintext
    每个第二类组贡献项 = (3 * 第一层级分界线索引)e(3 * 第二层级分界线索引)
    ```
  - 对于 `第二层级分界线索引 ＝ 0` 的情况：
    ```plaintext
    每个第二类组贡献项 = 3 * 第一层级分界线索引 + 3
    ```
- 当第二类组映射表的键表示第三类组映射表时：
  - 对于 `第三层级分界线索引 ＞ 0` 的情况：
    ```plaintext
    每个第三类组贡献项 = (3 * 第二层级分界线索引)e(3 * 第三层级分界线索引)
    ```
  - 对于 `第三层级分界线索引 ＝ 0` 的情况：
    ```plaintext
    每个第三类组贡献项 = 3 * 第二层级分界线索引
    ```
  - 然后构造第二类组贡献项：
    ```plaintext
    每个第二类组贡献项 = (3 * 第一层级分界线索引)e(各个第三类组贡献项相加)
    ```
- 最后，构造结果：
  ```plaintext
  科学计数法 = 1e(各个第二类组贡献项相加)
  ```
