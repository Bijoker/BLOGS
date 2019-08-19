1. read_excel
read_excel方法定义：

```
pandas.read_excel(io, sheet_name=0, header=0, skiprows=None, 
skip_footer=0, index_col=None, names=None, usecols=None, 
parse_dates=False, date_parser=None, na_values=None, 
thousands=None, convert_float=True, converters=None, 
dtype=None, true_values=None, false_values=None, 
engine=None, squeeze=False, **kwds)
```


io: 字符串，路径对象（pathlib.Path或py._path.local.LocalPath）
文件类对象 ，pandas Excel 文件或 xlrd 工作簿。该字符串可能是一个URL。URL包括http，ftp，s3和文件。例如，本地文件可写成file：//localhost/path/to/workbook.xlsx

io: 字符串，路径对象（pathlib.Path或py._path.local.LocalPath）
文件类对象 ，pandas Excel 文件或 xlrd 工作簿。该字符串可能是一个URL。URL包括http，ftp，s3和文件。例如，本地文件可写成file：//localhost/path/to/workbook.xlsx

sheet_name :字符串，int，字符串/整数的混合列表或None，默认为0
表名用字符串表示，索引表位置用整数表示；字符串/整数列表用于请求多个表；没有设置时将会自动获取所有表； 
可行的调用方式： 
Defaults ： 第一页作为数据文件 
1 ：第二页作为数据文件 
“Sheet1” ：第一页作为数据文件 
[0,1，“SEET5”] ：第一、第二和第五作为作为数据文件 
None ：所有表为作为数据文件

sheetname : 字符串，int，字符串/整数的混合列表或None，默认为0
从版本 0.21.0:以后用 sheet_name 代替

header : 整型，或者整型列表，默认为0
行(0-索引)用于解析的DataFrame的列标签。如果一个整数列表被传递，那么这些行位置将被合并成一个多索引。如果没有标题，请使用None。

skiprows :类列表
开始时跳过的行（0索引）

skip_footer : 整型, 默认为 0
结束时的行(0-索引)

index_col : 整型, 整型列表, 默认 None
列（0索引）用作DataFrame的行标签。 如果没有这样的列，则传递无。 如果传递一个列表，这些列将被组合成一个MultiIndex。 如果使用usecols选择数据子集，则index_col基于该子集。

names : 类似数组，默认无
要使用的列名列表。如果文件没有标题行，那么您应该显式地通过header=None。

converters : 字典 , 默认 None
在某些列中转换值的函数的命令。键可以是整数或列标签，值是接受一个输入参数的函数，Excel单元格内容，并返回转换后的内容。

dtype : 类型名称或dict的列-》其他类型,默认None
数据或列的数据类型。 例如。 {‘a’：np.float64，’b’：np.int32}使用对象保存Excel中存储的数据，而不解释dtype。 如果指定了转换器，则将应用INSTEAD进行dtype转换。

true_values : 列表, 默认 None
值视为Ture 
0.19.0版中的新功能。

false_values : 列表, 默认 None
值视为False 
0.19.0版中的新功能。

parse_cols : 整型或者列表, 默认为 None
自0.21.0版后不推荐使用：改为使用usecols。

usecols : 整型或者列表, 默认为 None
如果为None，则解析所有列，
如果为int，则某列将被解析
如果为ints，则列表要解析的列号列表将使用
如果为字符串表示逗号分隔的Excel列字母和列范围列表（例如“A：E”或“A，C，E：F”）。 范围包括边界两个。
squeeze : 布尔, 默认为 False
如果解析的数据只包含一列，则返回一个Series

na_values : 标量，字符串，列表类，或字典，默认None
某些字符串可以识别为 NA / NaN。 默认情况下，以下值将被解释为NaN： 
”，’＃N / A’，’＃N / AN / A’，’#NA’，’-1.＃IND’，’1.＃QNAN’， ‘-NNN’， 
‘-nan’，’1.＃IND’，’1.＃QNAN’，’N/A’，’NA’，’NULL’，’NaN’，’n / a’，’nan ‘， ‘null’ 。

thousands : 字符串, 默认为 None
将字符串列解析为数字的数千个分隔符。请注意，此参数仅是在Excel中作为文本存储的列所必需的，无论显示格式如何，任何数字列都将自动解析。

keep_default_na : 布尔, 默认为True
如果指定了na_values，并且keep_default_na为False，那么默认的NaN值将被重写

verbose :布尔, 默认为 False
显示列表中除去数字列，NA值的数量

engine: 字符串, 默认为 None
如果io不是缓冲区或路径，则必须将其设置为标识io。 可接受的值是None或xlrd

convert_float : 布尔, 默认为 True
将积分浮点数转换为int（即1.0 - > 1）。 如果为False，则所有数字数据都将作为浮点数读取：Excel将所有数字作为浮点数在内部存储

2. to_excel
to_excel方法定义：

```
DataFrame.to_excel(excel_writer, sheet_name='Sheet1', na_rep='',
 float_format=None, columns=None, header=True, index=True, 
 index_label=None, startrow=0, startcol=0, engine=None, 
 merge_cells=True, encoding=None, inf_rep='inf', verbose=True, 
 freeze_panes=None)
```


excel_writer : 字符串或ExcelWriter 对象
文件路径或现有的ExcelWriter

excel_writer : 字符串或ExcelWriter 对象
文件路径或现有的ExcelWriter

sheet_name :字符串,默认“Sheet1”
将包含DataFrame的表的名称。

na_rep : 字符串,默认‘ ’
缺失数据表示方式

float_format : 字符串,默认None
格式化浮点数的字符串

columns : 序列,可选
要编写的列

header : 布尔或字符串列表，默认为Ture。
写出列名。如果给定字符串列表，则假定它是列名称的别名。

index :布尔,默认的Ture
写行名（索引）

index_label : 字符串或序列，默认为None。
如果需要，可以使用索引列的列标签。如果没有给出，标题和索引为true，则使用索引名称。如果数据文件使用多索引，则需使用序列。

startrow :
左上角的单元格行来转储数据框

startcol :
左上角的单元格列转储数据帧

engine : 字符串,默认没有
使用写引擎 - 您也可以通过选项io.excel.xlsx.writer，io.excel.xls.writer和io.excel.xlsm.writer进行设置。

merge_cells : 布尔,默认为Ture
编码生成的excel文件。 只有xlwt需要，其他编写者本地支持unicode。

inf_rep : 字符串,默认“正”
无穷大的表示(在Excel中不存在无穷大的本地表示)

freeze_panes : 整数的元组(长度2)，默认为None。

