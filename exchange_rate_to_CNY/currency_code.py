# coding=utf-8
import json

import sys

data = [
    {"currency": "阿富汗尼", "code": "USD", "country": "阿富汗"},
    {"currency": "欧元", "code": "EUR", "country": "阿尔巴尼亚"},
    {"currency": "阿尔及利亚第纳尔", "code": "DZD", "country": "阿尔及利亚"},
    {"currency": "美元", "code": "USD", "country": "美属萨摩亚"},
    {"currency": "欧元", "code": "EUR", "country": "安道尔"},
    {"currency": "安哥拉宽扎", "code": "AOA", "country": "安哥拉"},
    {"currency": "东加勒比元", "code": "XCD", "country": "安圭拉"},
    {"currency": "东加勒比元", "code": "XCD", "country": "安提瓜和巴布达"},
    {"currency": "阿根廷比索", "code": "ARS", "country": "阿根廷"},
    {"currency": "亚美尼亚德拉姆", "code": "AMD", "country": "亚美尼亚"},
    {"currency": "阿鲁巴盾／弗罗林", "code": "AWG", "country": "阿鲁巴"},
    {"currency": "澳大利亚元", "code": "AUD", "country": "澳大利亚"},
    {"currency": "欧元", "code": "EUR", "country": "奥地利"},
    {"currency": "阿塞拜疆马纳特", "code": "AZM", "country": "阿塞拜疆"},
    {"currency": "欧元", "code": "EUR", "country": "亚速尔群岛"},
    {"currency": "巴哈马元", "code": "BSD", "country": "巴哈马"},
    {"currency": "巴林第纳尔", "code": "BHD", "country": "巴林"},
    {"currency": "孟加拉塔卡", "code": "BDT", "country": "孟加拉"},
    {"currency": "巴贝多元", "code": "BBD", "country": "巴巴多斯"},
    {"currency": "白俄罗斯卢布", "code": "BYR", "country": "白俄罗斯"},
    {"currency": "欧元", "code": "EUR", "country": "比利时"},
    {"currency": "伯利兹元", "code": "BZD", "country": "伯利兹"},
    {"currency": "西非国家中央银行非洲法郎", "code": "XOF", "country": "贝宁"},
    {"currency": "百慕大元", "code": "BMD", "country": "百慕大"},
    {"currency": "不丹努尔特鲁姆", "code": "BTN", "country": "不丹"},
    {"currency": "玻利维亚比索", "code": "BOB", "country": "玻利维亚"},
    {"currency": "荷属安的列斯盾", "code": "ANG", "country": "博奈尔岛"},
    {"currency": "波斯尼亚马克", "code": "BAM", "country": "波斯尼亚"},
    {"currency": "博茨瓦纳普拉", "code": "BWP", "country": "博茨瓦纳"},
    {"currency": "巴西雷亚尔", "code": "BRL", "country": "巴西"},
    {"currency": "美元", "code": "USD", "country": "英属维尔京群岛"},
    {"currency": "文莱元", "code": "BND", "country": "文莱"},
    {"currency": "欧元", "code": "EUR", "country": "保加利亚"},
    {"currency": "西非国家中央银行非洲法郎", "code": "XOF", "country": "布基纳法索"},
    {"currency": "布隆迪法郎", "code": "BIF", "country": "布隆迪"},
    {"currency": "柬埔寨瑞尔", "code": "KHR", "country": "柬埔寨"},
    {"currency": "中非共同体法郎", "code": "XAF", "country": "喀麦隆"},
    {"currency": "加拿大元", "code": "CAD", "country": "加拿大"},
    {"currency": "欧元", "code": "EUR", "country": "加那利群岛"},
    {"currency": "佛得角群岛埃斯库多", "code": "CVE", "country": "佛得角群岛"},
    {"currency": "开曼元", "code": "KYD", "country": "开曼群岛"},
    {"currency": "中非共同体法郎", "code": "XAF", "country": "中非共和国"},
    {"currency": "中非共同体法郎", "code": "XAF", "country": "乍得"},
    {"currency": "智利比索", "code": "CLP", "country": "智利"},
    {"currency": "人民币元", "code": "RMB", "country": "中华人民共和国"},
    {"currency": "哥伦比亚比索", "code": "COP", "country": "哥伦比亚"},
    {"currency": "科摩罗法郎", "code": "USD", "country": "科摩罗"},
    {"currency": "中非共同体法郎", "code": "XAF", "country": "刚果"},
    {"currency": "刚果法郎", "code": "CDF", "country": "刚果民主共和国"},
    {"currency": "新西兰元", "code": "NZD", "country": "库克群岛"},
    {"currency": "哥斯达黎加科朗", "code": "CRC", "country": "哥斯达黎加"},
    {"currency": "欧元", "code": "EUR", "country": "克罗地亚"},
    {"currency": "荷属安的列斯盾", "code": "ANG", "country": "库拉索岛"},
    {"currency": "欧元", "code": "EUR", "country": "塞浦路斯"},
    {"currency": "捷克克朗", "code": "CZK", "country": "捷克共和国"},
    {"currency": "丹麦克朗", "code": "DKK", "country": "丹麦"},
    {"currency": "吉布提法郎", "code": "DJF", "country": "吉布提"},
    {"currency": "东加勒比元", "code": "XCD", "country": "多米尼克"},
    {"currency": "多米尼加比索", "code": "DOP", "country": "多米尼加共和国"},
    {"currency": "美元", "code": "USD", "country": "东帝汶"},
    {"currency": "美元", "code": "USD", "country": "厄瓜多尔"},
    {"currency": "埃及镑", "code": "EGP", "country": "埃及"},
    {"currency": "美元", "code": "USD", "country": "萨尔瓦多"},
    {"currency": "英镑", "code": "GBP", "country": "英格兰"},
    {"currency": "中非共同体法郎", "code": "XAF", "country": "赤道几内亚"},
    {"currency": "厄立特里亚纳克法", "code": "ERN", "country": "厄立特里亚"},
    {"currency": "爱沙尼亚克朗", "code": "EEK", "country": "爱沙尼亚"},
    {"currency": "埃塞俄比亚比尔", "code": "ETB", "country": "埃塞俄比亚"},
    {"currency": "欧元", "code": "EUR", "country": "欧洲"},
    {"currency": "丹麦克朗", "code": "DKK", "country": "法罗群岛"},
    {"currency": "斐济元", "code": "FJD", "country": "斐济"},
    {"currency": "欧元", "code": "EUR", "country": "芬兰"},
    {"currency": "欧元", "code": "EUR", "country": "法国"},
    {"currency": "欧元", "code": "EUR", "country": "法属圭亚那"},
    {"currency": "太平洋法郎", "code": "XPF", "country": "法属波利尼西亚"},
    {"currency": "中非共同体法郎", "code": "XAF", "country": "加蓬"},
    {"currency": "冈比亚达拉西", "code": "GMD", "country": "冈比亚"},
    {"currency": "格鲁吉亚拉里", "code": "GEL", "country": "乔治亚州"},
    {"currency": "欧元", "code": "EUR", "country": "德国"},
    {"currency": "加纳塞地", "code": "GHC", "country": "加纳"},
    {"currency": "直布罗陀镑", "code": "GIP", "country": "直布罗陀"},
    {"currency": "欧元", "code": "EUR", "country": "希腊"},
    {"currency": "丹麦克朗", "code": "DKK", "country": "格陵兰"},
    {"currency": "东加勒比元", "code": "XCD", "country": "格林纳达"},
    {"currency": "欧元", "code": "EUR", "country": "瓜德罗普"},
    {"currency": "美元", "code": "USD", "country": "关岛"},
    {"currency": "危地马拉格查尔", "code": "GTQ", "country": "危地马拉"},
    {"currency": "英镑", "code": "GBP", "country": "根西岛"},
    {"currency": "几内亚法郎", "code": "GNF", "country": "几内亚"},
    {"currency": "西非国家中央银行非洲法郎", "code": "XOF", "country": "几内亚比绍"},
    {"currency": "圭亚那元", "code": "GYD", "country": "圭亚那"},
    {"currency": "海地古德", "code": "HTG", "country": "海地"},
    {"currency": "欧元", "code": "EUR", "country": "荷兰"},
    {"currency": "洪都拉斯伦皮拉", "code": "HNL", "country": "洪都拉斯"},
    {"currency": "港元", "code": "HKD", "country": "中国香港"},
    {"currency": "匈牙利福林", "code": "HUF", "country": "匈牙利"},
    {"currency": "冰岛克朗", "code": "ISK", "country": "冰岛"},
    {"currency": "印度卢比", "code": "INR", "country": "印度"},
    {"currency": "印尼盾", "code": "IDR", "country": "印度尼西亚"},
    {"currency": "伊拉克第纳尔", "code": "NID", "country": "伊拉克"},
    {"currency": "欧元", "code": "EUR", "country": "爱尔兰共和国"},
    {"currency": "以色列谢克尔", "code": "ILS", "country": "以色列"},
    {"currency": "欧元", "code": "EUR", "country": "意大利"},
    {"currency": "西非国家中央银行非洲法郎", "code": "XOF", "country": "科特迪瓦"},
    {"currency": "牙买加元", "code": "JMD", "country": "牙买加"},
    {"currency": "日元", "code": "JPY", "country": "日本"},
    {"currency": "英镑", "code": "GBP", "country": "泽西岛"},
    {"currency": "约旦第纳尔", "code": "JOD", "country": "约旦"},
    {"currency": "哈萨克坚戈", "code": "KZT", "country": "哈萨克斯坦"},
    {"currency": "肯尼亚先令", "code": "KES", "country": "肯尼亚"},
    {"currency": "澳大利亚元", "code": "AUD", "country": "基里巴斯"},
    {"currency": "韩圆", "code": "KRW", "country": "韩国"},
    {"currency": "美元", "code": "USD", "country": "科斯雷"},
    {"currency": "科威特第纳尔", "code": "KWD", "country": "科威特"},
    {"currency": "吉尔吉斯索姆", "code": "千克", "country": "吉尔吉斯共和国"},
    {"currency": "老挝基普", "code": "LAK", "country": "老挝"},
    {"currency": "拉脱维亚拉特", "code": "LVL", "country": "拉脱维亚"},
    {"currency": "黎巴嫩镑", "code": "LBP", "country": "黎巴嫩"},
    {"currency": "莱索托洛蒂", "code": "LSL", "country": "莱索托"},
    {"currency": "利比里亚元", "code": "LRD", "country": "利比里亚"},
    {"currency": "利比亚第纳尔", "code": "LYD", "country": "利比亚"},
    {"currency": "瑞士法郎", "code": "CHF", "country": "列支敦士登"},
    {"currency": "立陶宛利塔斯", "code": "LTL", "country": "立陶宛"},
    {"currency": "欧元", "code": "EUR", "country": "卢森堡"},
    {"currency": "澳门元", "code": "MOP", "country": "澳门"},
    {"currency": "欧元", "code": "EUR", "country": "马其顿（前南斯拉夫马其顿共和国）"},
    {"currency": "马达加斯加阿里亚里", "code": "MGA", "country": "马达加斯加"},
    {"currency": "欧元", "code": "EUR", "country": "马德拉"},
    {"currency": "马拉维克瓦查", "code": "MWK", "country": "马拉维"},
    {"currency": "马来西亚林吉特", "code": "MYR", "country": "马来西亚"},
    {"currency": "马尔代夫卢比", "code": "MVR", "country": "马尔代夫"},
    {"currency": "西非国家中央银行非洲法郎", "code": "XOF", "country": "马里"},
    {"currency": "欧元", "code": "EUR", "country": "马耳他"},
    {"currency": "美元", "code": "USD", "country": "马绍尔群岛"},
    {"currency": "欧元", "code": "EUR", "country": "马提尼克"},
    {"currency": "毛里塔尼亚乌吉亚", "code": "MRO", "country": "毛里塔尼亚"},
    {"currency": "毛里求斯卢比", "code": "MUR", "country": "毛里求斯"},
    {"currency": "法郎", "code": "EUR", "country": "马约特岛"},
    {"currency": "墨西哥比索", "code": "MXN", "country": "墨西哥"},
    {"currency": "美元", "code": "USD", "country": "密克罗尼西亚联邦"},
    {"currency": "摩尔多瓦列伊", "code": "MDL", "country": "摩尔多瓦"},
    {"currency": "欧元", "code": "EUR", "country": "摩纳哥"},
    {"currency": "蒙古图格里克", "code": "MNT", "country": "蒙古"},
    {"currency": "塞尔维亚第纳尔", "code": "EUR", "country": "黑山"},
    {"currency": "东加勒比元", "code": "XCD", "country": "蒙特塞拉特岛"},
    {"currency": "摩洛哥迪拉姆", "code": "MAD", "country": "摩洛哥"},
    {"currency": "莫桑比克梅蒂卡尔", "code": "MZM", "country": "莫桑比克"},
    {"currency": "纳米比亚元", "code": "NAD", "country": "纳米比亚"},
    {"currency": "尼泊尔卢比", "code": "NPR", "country": "尼泊尔"},
    {"currency": "欧元", "code": "EUR", "country": "荷兰"},
    {"currency": "荷属安的列斯元", "code": "ANG", "country": "荷属安的列斯"},
    {"currency": "太平洋法郎", "code": "XPF", "country": "新喀里多尼亚"},
    {"currency": "新西兰元", "code": "NZD", "country": "新西兰"},
    {"currency": "尼加拉瓜金科多巴", "code": "NIO", "country": "尼加拉瓜"},
    {"currency": "西非国家中央银行非洲法郎", "code": "XOF", "country": "尼日尔"},
    {"currency": "尼日利亚奈拉", "code": "NGN", "country": "尼日利亚"},
    {"currency": "澳大利亚元", "code": "AUD", "country": "诺福克岛"},
    {"currency": "英镑", "code": "GBP", "country": "北爱尔兰"},
    {"currency": "美元", "code": "USD", "country": "北马里亚纳群岛"},
    {"currency": "挪威克朗", "code": "NOK", "country": "挪威"},
    {"currency": "阿曼里亚尔", "code": "OMR", "country": "阿曼"},
    {"currency": "巴基斯坦卢比", "code": "PKR", "country": "巴基斯坦"},
    {"currency": "美元", "code": "USD", "country": "帕劳"},
    {"currency": "巴拿马巴波亚", "code": "PAB", "country": "巴拿马"},
    {"currency": "巴布亚基纳", "code": "PGK", "country": "巴布亚新几内亚"},
    {"currency": "巴拉圭瓜拉尼", "code": "PYG", "country": "巴拉圭"},
    {"currency": "秘鲁新索尔", "code": "PEN", "country": "秘鲁"},
    {"currency": "菲律宾比索", "code": "PHP", "country": "菲律宾"},
    {"currency": "波兰兹罗提", "code": "PLN", "country": "波兰"},
    {"currency": "美元", "code": "USD", "country": "波纳佩岛"},
    {"currency": "欧元", "code": "EUR", "country": "葡萄牙"},
    {"currency": "美元", "code": "USD", "country": "波多黎各"},
    {"currency": "卡塔尔里亚尔", "code": "QAR", "country": "卡塔尔"},
    {"currency": "欧元", "code": "EUR", "country": "留尼旺岛"},
    {"currency": "罗马尼亚列伊", "code": "ROL", "country": "罗马尼亚"},
    {"currency": "美元", "code": "USD", "country": "罗塔"},
    {"currency": "俄罗斯卢布", "code": "RUB", "country": "俄罗斯"},
    {"currency": "卢旺达法郎", "code": "RWF", "country": "卢旺达"},
    {"currency": "荷属安的列斯盾", "code": "ANG", "country": "萨巴岛"},
    {"currency": "美元", "code": "USD", "country": "塞班岛"},
    {"currency": "西萨摩亚塔拉", "code": "WST", "country": "萨摩亚"},
    {"currency": "欧元", "code": "EUR", "country": "圣马力诺"},
    {"currency": "沙特里亚尔", "code": "SAR", "country": "沙特阿拉伯"},
    {"currency": "英镑", "code": "GBP", "country": "苏格兰"},
    {"currency": "西非国家中央银行非洲法郎", "code": "XOF", "country": "塞内加尔"},
    {"currency": "塞尔维亚第纳尔", "code": "EUR", "country": "塞尔维亚"},
    {"currency": "塞舌尔卢比", "code": "SCR", "country": "塞舌尔"},
    {"currency": "塞拉利昂利昂", "code": "SLL", "country": "塞拉利昂"},
    {"currency": "新加坡元", "code": "SGD", "country": "新加坡"},
    {"currency": "欧元", "code": "EUR", "country": "斯洛伐克"},
    {"currency": "欧元", "code": "EUR", "country": "斯洛文尼亚"},
    {"currency": "所罗门群岛元", "code": "SBD", "country": "所罗门群岛"},
    {"currency": "南非兰特", "code": "ZAR", "country": "南非"},
    {"currency": "欧元", "code": "EUR", "country": "西班牙"},
    {"currency": "斯里兰卡卢比", "code": "LKR", "country": "斯里兰卡"},
    {"currency": "欧元", "code": "EUR", "country": "圣巴泰勒米"},
    {"currency": "东加勒比元", "code": "XCD", "country": "圣克里斯托弗岛"},
    {"currency": "美元", "code": "USD", "country": "圣克罗伊岛"},
    {"currency": "荷属安的列斯盾", "code": "ANG", "country": "圣尤斯特歇斯"},
    {"currency": "美元", "code": "USD", "country": "圣约翰"},
    {"currency": "东加勒比元", "code": "XCD", "country": "圣基茨和尼维斯"},
    {"currency": "东加勒比元", "code": "XCD", "country": "圣卢西亚"},
    {"currency": "荷属安的列斯盾", "code": "ANG", "country": "圣马坦"},
    {"currency": "欧元", "code": "EUR", "country": "圣马丁"},
    {"currency": "美元", "code": "USD", "country": "圣托马斯"},
    {"currency": "东加勒比元", "code": "XCD", "country": "圣文森特和格林纳丁斯"},
    {"currency": "苏里南盾", "code": "SRG", "country": "苏里南"},
    {"currency": "斯威士兰里兰吉尼", "code": "SZL", "country": "斯威士兰"},
    {"currency": "瑞典克朗", "code": "SEK", "country": "瑞典"},
    {"currency": "瑞士法郎", "code": "CHF", "country": "瑞士"},
    {"currency": "太平洋法郎", "code": "XPF", "country": "塔希提岛"},
    {"currency": "台湾元", "code": "TWD", "country": "中国台湾"},
    {"currency": "塔吉克斯坦 索莫尼", "code": "TJS", "country": "塔吉克斯坦"},
    {"currency": "坦桑尼亚先令", "code": "TZS", "country": "坦桑尼亚"},
    {"currency": "泰铢", "code": "THB", "country": "泰国"},
    {"currency": "美元", "code": "USD", "country": "提尼安岛"},
    {"currency": "西非国家中央银行非洲法郎", "code": "XOF", "country": "多哥"},
    {"currency": "汤加 潘加", "code": "TOP", "country": "汤加"},
    {"currency": "美元", "code": "USD", "country": "托尔托拉岛"},
    {"currency": "特立尼达和多巴哥元", "code": "TTD", "country": "特立尼达和多巴哥"},
    {"currency": "美元", "code": "USD", "country": "特鲁克群岛"},
    {"currency": "突尼斯第纳尔", "code": "TND", "country": "突尼斯"},
    {"currency": "美元", "code": "USD", "country": "土耳其"},
    {"currency": "土库曼马纳特", "code": "TMM", "country": "土库曼斯坦"},
    {"currency": "美元", "code": "USD", "country": "特克斯群岛和凯科斯群岛"},
    {"currency": "澳大利亚元", "code": "AUD", "country": "图瓦卢"},
    {"currency": "美元", "code": "USD", "country": "美属维尔京群岛"},
    {"currency": "乌干达先令", "code": "UGX", "country": "乌干达"},
    {"currency": "乌克兰格里夫纳", "code": "UAH", "country": "乌克兰"},
    {"currency": "东加勒比元", "code": "XCD", "country": "尤宁岛"},
    {"currency": "阿联酋迪拉姆", "code": "AED", "country": "阿拉伯联合酋长国"},
    {"currency": "英镑", "code": "GBP", "country": "英国"},
    {"currency": "美元", "code": "USD", "country": "美国"},
    {"currency": "乌拉圭比索", "code": "UYU", "country": "乌拉圭"},
    {"currency": "乌兹别克斯坦索姆", "code": "UZS", "country": "乌兹别克斯坦"},
    {"currency": "瓦努阿图 瓦图", "code": "VUV", "country": "瓦努阿图"},
    {"currency": "欧元", "code": "EUR", "country": "梵蒂冈"},
    {"currency": "委内瑞拉博利瓦", "code": "VEB", "country": "委内瑞拉"},
    {"currency": "越南盾", "code": "VND", "country": "越南"},
    {"currency": "美元", "code": "USD", "country": "维尔京戈尔达岛"},
    {"currency": "英镑", "code": "GBP", "country": "威尔士"},
    {"currency": "太平洋法郎", "code": "XPF", "country": "瓦利斯和富图纳群岛"},
    {"currency": "美元", "code": "USD", "country": "雅浦群岛"},
    {"currency": "也门里亚尔", "code": "YER", "country": "也门"},
    {"currency": "赞比亚克瓦查", "code": "ZMK", "country": "赞比亚"},
    {"currency": "津巴布韦元", "code": "ZWD", "country": "津巴布韦"}]

query = sys.argv[1]

result = []
for record in data:
    if query in record['currency'] or query in record['code'] or query in record['country']:
        result.append(record)

items = []
for record in result:
    items.append({
        "title": '国家：{}  货币：{}'.format(record['country'], record['currency']),
        "subtitle": record['code']
    })

print json.dumps({'items': items})