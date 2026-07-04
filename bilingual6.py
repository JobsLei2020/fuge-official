with open(r"D:\Workspace_Autoclaw\fuge-replica\index.html.bak", "r", encoding="utf-8") as f:
    cn = f.read()

# Gallery
cn = cn.replace('<h2 class="sec-title">产品画廊</h2>',
                '<h2 class="sec-title">产品画廊 <small class="lang-en">Product Gallery</small></h2>')

# News
cn = cn.replace('<h2 class="sec-title">新闻中心</h2>',
                '<h2 class="sec-title">新闻中心 <small class="lang-en">News</small></h2>')

cn = cn.replace(
    '<h4 class="blog-title"><a href="#">富葛鲜片获中国饭店行业协会"最佳火锅伴侣"称号</a></h4>',
    '<h4 class="blog-title"><a href="#">富葛鲜片获中国饭店行业协会"最佳火锅伴侣"称号<br><span class="lang-en">Fuge Fresh Slices Awarded Best Hotpot Companion</span></a></h4>'
)
cn = cn.replace(
    '<h4 class="blog-title"><a href="#">富葛实业获评"重庆名牌农产品" 好品质再获认可</a></h4>',
    '<h4 class="blog-title"><a href="#">富葛实业获评"重庆名牌农产品" 好品质再获认可<br><span class="lang-en">Fuge Named Chongqing Famous Agricultural Product</span></a></h4>'
)
cn = cn.replace(
    '<h4 class="blog-title"><a href="#">西南大学与富葛实业深化合作，共育鲜食葛根新品种</a></h4>',
    '<h4 class="blog-title"><a href="#">西南大学与富葛实业深化合作，共育鲜食葛根新品种<br><span class="lang-en">SW Univ. &amp; Fuge Deepen Cooperation on New Varieties</span></a></h4>'
)
cn = cn.replace(
    '<h4 class="blog-title"><a href="#">富葛香系列葛根茶新品上市，传承药食同源千年智慧</a></h4>',
    '<h4 class="blog-title"><a href="#">富葛香系列葛根茶新品上市，传承药食同源千年智慧<br><span class="lang-en">Fuge Aroma Tea Launched — Millennia of Medicine-Food Wisdom</span></a></h4>'
)

# CTA
cn = cn.replace(
    '<h2 class="sec-title text-white">种植合作 代理招商</h2>',
    '<h2 class="sec-title text-white">种植合作 · 代理招商 <small class="lang-en" style="color:rgba(255,255,255,0.5);font-size:0.8rem;">Farming Partnership &amp; Distribution</small></h2>'
)
cn = cn.replace(
    '<p class="text-white-50 mt-3" style="font-size:1.1rem;">我们期待与您合作共赢!</p>',
    '<p class="text-white-50 mt-3" style="font-size:1.1rem;">我们期待与您合作共赢!<br><span class="lang-en" style="color:rgba(255,255,255,0.4);font-size:0.85rem;">We look forward to partnering with you!</span></p>'
)
cn = cn.replace('<span class="effect-1">联系我们</span><span class="effect-1">联系我们</span>',
                '<span class="effect-1">联系我们 | Contact</span><span class="effect-1">联系我们 | Contact</span>')

# Footer
cn = cn.replace('<span class="effect-1">企业简介</span><span class="effect-1">企业简介</span>',
                '<span class="effect-1">企业简介 | Company</span><span class="effect-1">企业简介 | Company</span>')
cn = cn.replace('<span class="effect-1">品种介绍</span><span class="effect-1">品种介绍</span>',
                '<span class="effect-1">品种介绍 | Variety</span><span class="effect-1">品种介绍 | Variety</span>')
cn = cn.replace('<span class="effect-1">种植体系</span><span class="effect-1">种植体系</span>',
                '<span class="effect-1">种植体系 | Farming</span><span class="effect-1">种植体系 | Farming</span>')
cn = cn.replace('<span class="effect-1">产品展示</span><span class="effect-1">产品展示</span>',
                '<span class="effect-1">产品展示 | Products</span><span class="effect-1">产品展示 | Products</span>')
cn = cn.replace('<span class="effect-1">隐私保护</span><span class="effect-1">隐私保护</span>',
                '<span class="effect-1">隐私保护 | Privacy</span><span class="effect-1">隐私保护 | Privacy</span>')

# The "联系我们" in footer was already replaced in nav section, check if it still has Chinese
cn = cn.replace('<span class="effect-1">Contact Us</span><span class="effect-1">Contact Us</span>',
                '<span class="effect-1">联系我们 | Contact</span><span class="effect-1">联系我们 | Contact</span>')

# Footer address - already text
cn = cn.replace('<div>重庆大足区智凤街道(富葛园)</div>',
                '<div>重庆大足区智凤街道(富葛园)<br><span class="lang-en">Fuge Garden, Zhifeng Subdistrict, Dazu, Chongqing</span></div>')

cn = cn.replace('<a href="#">重庆富葛实业有限公司</a>',
                '<a href="#">重庆富葛实业有限公司 <span class="lang-en">Chongqing Fourgen Kudzu Industrial Co., Ltd.</span></a>')

with open(r"D:\Workspace_Autoclaw\fuge-replica\index.html.bak", "w", encoding="utf-8") as f:
    f.write(cn)

print("Part 6 done - Gallery + News + CTA + Footer")
