with open(r"D:\Workspace_Autoclaw\fuge-replica\index.html.bak", "r", encoding="utf-8") as f:
    cn = f.read()

# Products section
cn = cn.replace('<h2 class="sec-title">产品展示</h2>',
                '<h2 class="sec-title">产品展示 <small class="lang-en">Our Products</small></h2>')
cn = cn.replace('<p class="text-muted mt-2" style="font-size:0.9rem;">品质 | 传承 | 创新</p>',
                '<p class="text-muted mt-2" style="font-size:0.9rem;">品质 | 传承 | 创新 <span class="lang-en">Quality | Heritage | Innovation</span></p>')

# Product 1 - 富葛鲜片
cn = cn.replace('<span class="product-tag"><i class="fas fa-star me-1"></i>明星产品</span>',
                '<span class="product-tag"><i class="fas fa-star me-1"></i>明星产品 Star Product</span>')
cn = cn.replace('<h3 class="product-name">富葛鲜片</h3>',
                '<h3 class="product-name">富葛鲜片 <span class="lang-en">Fuge Fresh Slices</span></h3>')
cn = cn.replace(
    '<p class="product-desc">选十斤以上富葛，去皮去两头，整形切片，精选制成。十斤鲜葛出一斤富葛鲜片。-196℃超低温瞬冻锁鲜。</p>',
    '<p class="product-desc">选十斤以上富葛，去皮去两头，整形切片，精选制成。十斤鲜葛出一斤富葛鲜片。-196℃超低温瞬冻锁鲜。<br><span class="lang-en">Selected 10+ lb Fuge kudzu, peeled, trimmed and sliced. 10 lbs yields 1 lb of Fuge fresh slices. -196&deg;C flash frozen.</span></p>'
)

# Product 2 - 膳食纤维粉
cn = cn.replace('<span class="product-tag">特色产品</span>',
                '<span class="product-tag">特色产品 Specialty</span>')
cn = cn.replace('<h3 class="product-name">富葛膳食纤维粉</h3>',
                '<h3 class="product-name">富葛膳食纤维粉 <span class="lang-en">Dietary Fiber Powder</span></h3>')
cn = cn.replace(
    '<p class="product-desc">非传统葛根粉，膳食纤维76%NVD/100g，葛根素&gt;450mg/100g。冷水亦可冲调，宴前解酒、清畅护肠、调节三高。</p>',
    '<p class="product-desc">非传统葛根粉，膳食纤维76%NVD/100g，葛根素&gt;450mg/100g。冷水亦可冲调，宴前解酒、清畅护肠、调节三高。<br><span class="lang-en">76% dietary fiber NVD/100g, puerarin &gt;450mg/100g. Mixes with cold water. Great for digestion &amp; wellness.</span></p>'
)

# Product 3 - 富葛香十年典藏
cn = cn.replace('<span class="product-tag">高端礼盒</span>',
                '<span class="product-tag">高端礼盒 Premium Gift</span>')
cn = cn.replace('<h3 class="product-name">富葛香 · 十年典藏款</h3>',
                '<h3 class="product-name">富葛香 · 十年典藏款 <span class="lang-en">Fuge Aroma &middot; 10-Year Reserve</span></h3>')
cn = cn.replace(
    '<p class="product-desc">二十多道严苛工序精制而成，充分保留葛根活性成分和独特香气。药食同源，高端养生首选。</p>',
    '<p class="product-desc">二十多道严苛工序精制而成，充分保留葛根活性成分和独特香气。药食同源，高端养生首选。<br><span class="lang-en">20+ rigorous processes preserve active compounds and unique aroma. Premium wellness choice.</span></p>'
)

# Product 4 - 年份产地茶
cn = cn.replace('<span class="product-tag">茶系列</span>',
                '<span class="product-tag">茶系列 Tea Series</span>')
cn = cn.replace('<h3 class="product-name">富葛香 · 年份产地茶</h3>',
                '<h3 class="product-name">富葛香 · 年份产地茶 <span class="lang-en">Fuge Aroma &middot; Vintage Tea</span></h3>')
cn = cn.replace(
    '<p class="product-desc">精选大足、北碚缙云山、云南昌宁三地核心基地原料，五焙五陈工艺。大足/云南/缙云山三款可选。</p>',
    '<p class="product-desc">精选大足、北碚缙云山、云南昌宁三地核心基地原料，五焙五陈工艺。大足/云南/缙云山三款可选。<br><span class="lang-en">Three origins: Dazu, Jinyun Mt., Yunnan. Five-roast, five-age process. Three regional options.</span></p>'
)

# Product 5 - 养生茶
cn = cn.replace('<span class="product-tag">养生茶</span>',
                '<span class="product-tag">养生茶 Wellness Tea</span>')
cn = cn.replace('<h3 class="product-name">富葛香 · 葛根红茶养生茶</h3>',
                '<h3 class="product-name">富葛香 · 葛根红茶养生茶 <span class="lang-en">Fuge Aroma &middot; Kudzu Black Tea</span></h3>')
cn = cn.replace(
    '<p class="product-desc">采自缙云山脉富葛原香茶复配古树红茶，三焙三陈工艺，持久留香。日常养生饮用，有益血管健康。</p>',
    '<p class="product-desc">采自缙云山脉富葛原香茶复配古树红茶，三焙三陈工艺，持久留香。日常养生饮用，有益血管健康。<br><span class="lang-en">Fuge aroma tea from Jinyun Mt. blended with ancient tree black tea. Supports vascular health.</span></p>'
)

# Product 6 - 鲜浆面
cn = cn.replace('<span class="product-tag">日常主食</span>',
                '<span class="product-tag">日常主食 Daily Staple</span>')
cn = cn.replace('<h3 class="product-name">富葛鲜浆面</h3>',
                '<h3 class="product-name">富葛鲜浆面 <span class="lang-en">Fresh Kudzu Noodles</span></h3>')
cn = cn.replace(
    '<p class="product-desc">鲜葛全浆入面，鲜浆添加量高达30%。富含膳食纤维，快煮2分钟即熟，口感弹滑爽口。</p>',
    '<p class="product-desc">鲜葛全浆入面，鲜浆添加量高达30%。富含膳食纤维，快煮2分钟即熟，口感弹滑爽口。<br><span class="lang-en">30% fresh kudzu pulp in noodles. Rich in fiber. Ready in 2 minutes. Smooth &amp; springy.</span></p>'
)

# "了解详情" buttons
cn = cn.replace('<span class="effect-1">了解详情</span><span class="effect-1">了解详情</span>',
                '<span class="effect-1">了解详情 | Learn More</span><span class="effect-1">了解详情 | Learn More</span>')

with open(r"D:\Workspace_Autoclaw\fuge-replica\index.html.bak", "w", encoding="utf-8") as f:
    f.write(cn)

print("Part 5 done - Products")
