import re

# Read Chinese backup
with open(r"D:\Workspace_Autoclaw\fuge-replica\index.html.bak", "r", encoding="utf-8") as f:
    cn = f.read()

# Read English version for reference
with open(r"D:\Workspace_Autoclaw\fuge-replica\index.html", "r", encoding="utf-8") as f:
    en = f.read()

# Strategy: Start from Chinese version and inject English text
# Add CSS for bilingual display
css_inject = """
        /* Bilingual */
        .lang-en { display: block; font-size: 0.75rem; color: #888; font-weight: 400; margin-top: 2px; letter-spacing: 0.3px; }
        .cert-card .lang-en { font-size: 0.65rem; }
        .chain-step .lang-en { font-size: 0.7rem; }
        .feature-card-text .lang-en { font-size: 0.75rem; }
        .product-name .lang-en { font-size: 0.7rem; color: #999; font-weight: 400; }
        .product-desc .lang-en { font-size: 0.72rem; }
        .blog-title .lang-en { font-size: 0.72rem; font-weight: 400; }
        .sec-title .lang-en { font-size: 0.85rem; font-weight: 400; color: #999; letter-spacing: 0; }
        .compare-table td .lang-en { font-size: 0.7rem; color: #999; }
        .compare-table th .lang-en { font-size: 0.65rem; font-weight: 300; color: rgba(255,255,255,0.7); }
"""

# Inject CSS before the closing </style> tag
cn = cn.replace("</style>", css_inject + "\n    </style>")

# Also add a small CSS line in the meta for better mobile display
# Update title to bilingual
cn = cn.replace(
    '<title>富葛 - 懂生活 选富葛 | 重庆富葛实业有限公司</title>',
    '<title>富葛 Fuge - 懂生活 选富葛 | Live Well, Choose Fuge</title>'
)

# Update meta description to bilingual
cn = cn.replace(
    'content="富葛是一种鲜食葛根品种，色泽洁白、纤维细腻、绵软化渣、味道清甜。富葛富含膳食纤维、直链淀粉、葛根素、蛋白质、氨基酸、人体必需矿物质等。"',
    'content="富葛是一种鲜食葛根品种... Fuge is a fresh-edible kudzu variety with pure white color, fine fiber, soft texture, and naturally sweet taste."'
)

cn = cn.replace(
    'content="富葛,鲜食葛根富葛,重庆富葛实业有限公司"',
    'content="富葛,Fuge,鲜食葛根,fresh kudzu,重庆富葛实业有限公司,Chongqing Fourgen Kudzu"'
)

# Navigation text replacements - add English in hover-effect spans
# Mobile nav:
cn = cn.replace('<li><a href="/">首页</a></li>', '<li><a href="/">首页 <span class="lang-en">Home</span></a></li>')

cn = cn.replace(
    '<li class="has-children" onclick="toggleSub(this)"><a href="#">关于我们</a><ul class="sub-menu"><li><a href="#">企业简介</a></li><li><a href="#">发展理念</a></li><li><a href="#">发展历程</a></li></ul></li>',
    '<li class="has-children" onclick="toggleSub(this)"><a href="#">关于我们 <span class="lang-en">About Us</span></a><ul class="sub-menu"><li><a href="#">企业简介 <span class="lang-en">Company Profile</span></a></li><li><a href="#">发展理念 <span class="lang-en">Philosophy</span></a></li><li><a href="#">发展历程 <span class="lang-en">Milestones</span></a></li></ul></li>'
)

cn = cn.replace(
    '<li class="has-children" onclick="toggleSub(this)"><a href="#">关于富葛</a><ul class="sub-menu"><li><a href="#">品种介绍</a></li><li><a href="#">葛根百科</a></li></ul></li>',
    '<li class="has-children" onclick="toggleSub(this)"><a href="#">关于富葛 <span class="lang-en">About Fuge</span></a><ul class="sub-menu"><li><a href="#">品种介绍 <span class="lang-en">Variety Info</span></a></li><li><a href="#">葛根百科 <span class="lang-en">Kudzu Encyclopedia</span></a></li></ul></li>'
)

cn = cn.replace(
    '<li class="has-children" onclick="toggleSub(this)"><a href="#">种植体系</a><ul class="sub-menu"><li><a href="#">特质农品产区</a></li><li><a href="#">绿色食品产区</a></li><li><a href="#">源产地分布</a></li></ul></li>',
    '<li class="has-children" onclick="toggleSub(this)"><a href="#">种植体系 <span class="lang-en">Farming System</span></a><ul class="sub-menu"><li><a href="#">特质农品产区 <span class="lang-en">Special Ag. Zones</span></a></li><li><a href="#">绿色食品产区 <span class="lang-en">Green Food Zones</span></a></li><li><a href="#">源产地分布 <span class="lang-en">Origin Map</span></a></li></ul></li>'
)

cn = cn.replace(
    '<li class="has-children" onclick="toggleSub(this)"><a href="#">产品展示</a><ul class="sub-menu"><li><a href="#">主要产品</a></li><li><a href="#">在线商城</a></li></ul></li>',
    '<li class="has-children" onclick="toggleSub(this)"><a href="#">产品展示 <span class="lang-en">Products</span></a><ul class="sub-menu"><li><a href="#">主要产品 <span class="lang-en">Main Products</span></a></li><li><a href="#">在线商城 <span class="lang-en">Online Store</span></a></li></ul></li>'
)

cn = cn.replace(
    '<li class="has-children" onclick="toggleSub(this)"><a href="#">新闻中心</a><ul class="sub-menu"><li><a href="#">企业新闻</a></li><li><a href="#">媒体聚焦</a></li></ul></li>',
    '<li class="has-children" onclick="toggleSub(this)"><a href="#">新闻中心 <span class="lang-en">News</span></a><ul class="sub-menu"><li><a href="#">企业新闻 <span class="lang-en">Company News</span></a></li><li><a href="#">媒体聚焦 <span class="lang-en">Media Focus</span></a></li></ul></li>'
)

cn = cn.replace(
    '<li class="has-children" onclick="toggleSub(this)"><a href="#">联系我们</a><ul class="sub-menu"><li><a href="#">种植合作</a></li><li><a href="#">代理招商</a></li><li><a href="#">招聘信息</a></li></ul></li>',
    '<li class="has-children" onclick="toggleSub(this)"><a href="#">联系我们 <span class="lang-en">Contact Us</span></a><ul class="sub-menu"><li><a href="#">种植合作 <span class="lang-en">Farming Partnership</span></a></li><li><a href="#">代理招商 <span class="lang-en">Distribution Inquiry</span></a></li><li><a href="#">招聘信息 <span class="lang-en">Careers</span></a></li></ul></li>'
)

with open(r"D:\Workspace_Autoclaw\fuge-replica\index.html.bak", "w", encoding="utf-8") as f:
    f.write(cn)

print("Part 1 done - CSS + meta + mobile nav")
