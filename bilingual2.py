with open(r"D:\Workspace_Autoclaw\fuge-replica\index.html.bak", "r", encoding="utf-8") as f:
    cn = f.read()

# Desktop navigation - replace effect-1 spans with bilingual
cn = cn.replace('<span class="effect-1">首页</span><span class="effect-1">首页</span>',
                '<span class="effect-1">首页 | Home</span><span class="effect-1">首页 | Home</span>')
cn = cn.replace('<span class="effect-1">关于我们</span><span class="effect-1">关于我们</span>',
                '<span class="effect-1">关于我们 | About Us</span><span class="effect-1">关于我们 | About Us</span>')
cn = cn.replace('<span class="effect-1">关于富葛</span><span class="effect-1">关于富葛</span>',
                '<span class="effect-1">关于富葛 | About Fuge</span><span class="effect-1">关于富葛 | About Fuge</span>')
cn = cn.replace('<span class="effect-1">种植体系</span><span class="effect-1">种植体系</span>',
                '<span class="effect-1">种植体系 | Farming</span><span class="effect-1">种植体系 | Farming</span>')
cn = cn.replace('<span class="effect-1">产品展示</span><span class="effect-1">产品展示</span>',
                '<span class="effect-1">产品展示 | Products</span><span class="effect-1">产品展示 | Products</span>')
cn = cn.replace('<span class="effect-1">新闻中心</span><span class="effect-1">新闻中心</span>',
                '<span class="effect-1">新闻中心 | News</span><span class="effect-1">新闻中心 | News</span>')
cn = cn.replace('<span class="effect-1">联系我们</span><span class="effect-1">联系我们</span>',
                '<span class="effect-1">联系我们 | Contact</span><span class="effect-1">联系我们 | Contact</span>')

# Header button
cn = cn.replace('<i class="fab fa-shopify"></i> 在线商城</span><span class="effect-1"><i class="fab fa-shopify"></i> 在线商城</span>',
               '<i class="fab fa-shopify"></i> 在线商城 | Online Store</span><span class="effect-1"><i class="fab fa-shopify"></i> 在线商城 | Online Store</span>')

# Variety section - bilingual subtitle + heading + tagline
cn = cn.replace('<p class="section-subtitle">FUGE KUDZU</p>',
                '<p class="section-subtitle">FUGE | 富葛鲜食葛根</p>')

# Live Well heading - replace with bilingual
cn = cn.replace('<h2 class="sec-title">懂生活 选富葛</h2>',
                '<h2 class="sec-title">懂生活 选富葛 <small class="lang-en">Live Well, Choose Fuge</small></h2>')

cn = cn.replace(
    '<p class="text-muted mt-3" style="font-size:0.95rem;">"富葛"的独特基因，成就卓尔不群的葛根产品——十斤鲜葛出一斤富葛鲜片</p>',
    '<p class="text-muted mt-3" style="font-size:0.95rem;">"富葛"的独特基因，成就卓尔不群的葛根产品——十斤鲜葛出一斤富葛鲜片<br><span class="lang-en" style="margin-top:5px;color:#aaa;">The unique genetics of Fuge create an exceptional kudzu product — 10 lbs of fresh kudzu yields 1 lb of Fuge fresh slices.</span></p>'
)

# Comparison table - bilingual headers
cn = cn.replace('<th>对比维度</th>', '<th>对比维度 <span class="lang-en">Comparison</span></th>')
cn = cn.replace('<th>富葛（鲜食葛根）</th>', '<th>富葛（鲜食葛根）<br><span class="lang-en">Fuge (Fresh Kudzu)</span></th>')
cn = cn.replace('<th>柴葛根</th>', '<th>柴葛根 <span class="lang-en">Wild Kudzu</span></th>')
cn = cn.replace('<th>粉葛根</th>', '<th>粉葛根 <span class="lang-en">Starch Kudzu</span></th>')

# Table rows
cn = cn.replace('<td>可食用部分</td>', '<td>可食用部分 <span class="lang-en">Edible Portion</span></td>')
cn = cn.replace('<span class="compare-badge">优</span>', '<span class="compare-badge">优 Best</span>')
cn = cn.replace('<td>食用方法</td>', '<td>食用方法 <span class="lang-en">Consumption</span></td>')
cn = cn.replace('<td><strong>一种蔬菜（直接食用）</strong></td>', '<td><strong>一种蔬菜（直接食用）</strong><br><span class="lang-en">A Vegetable (Eat Directly)</span></td>')
cn = cn.replace('<td>中药材及提取物</td>', '<td>中药材及提取物 <span class="lang-en">Herbal Medicine &amp; Extracts</span></td>')
cn = cn.replace('<td>制作葛根粉</td>', '<td>制作葛根粉 <span class="lang-en">Kudzu Starch Making</span></td>')

cn = cn.replace(
    '<td>葛根素含量<br><small>（每100g干品）</small></td>',
    '<td>葛根素含量<br><small>（每100g干品）<br><span class="lang-en">Puerarin (per 100g dry)</span></small></td>'
)

cn = cn.replace('<td>&gt;400mg（合格品）</td>', '<td>&gt;400mg（合格品）<br><span class="lang-en">Standard grade</span></td>')
cn = cn.replace('<td>&gt;2500mg（入药标准）</td>', '<td>&gt;2500mg（入药标准）<br><span class="lang-en">Pharmaceutical grade</span></td>')
cn = cn.replace('<td>&gt;8mg（优等品葛粉）</td>', '<td>&gt;8mg（优等品葛粉）<br><span class="lang-en">Premium starch</span></td>')
cn = cn.replace('<td>实际营养吸收比例</td>', '<td>实际营养吸收比例 <span class="lang-en">Nutrient Absorption Rate</span></td>')

with open(r"D:\Workspace_Autoclaw\fuge-replica\index.html.bak", "w", encoding="utf-8") as f:
    f.write(cn)

print("Part 2 done - Desktop nav + variety + comparison table")
