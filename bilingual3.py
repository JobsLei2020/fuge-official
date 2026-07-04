with open(r"D:\Workspace_Autoclaw\fuge-replica\index.html.bak", "r", encoding="utf-8") as f:
    cn = f.read()

# Key highlights
cn = cn.replace('<p class="text-muted small mb-0">可食用部分</p>', '<p class="text-muted small mb-0">可食用部分<br><span class="lang-en">Edible Portion</span></p>')
cn = cn.replace('<p class="text-muted small mb-0">营养吸收比例</p>', '<p class="text-muted small mb-0">营养吸收比例<br><span class="lang-en">Absorption Rate</span></p>')
cn = cn.replace('<p class="text-muted small mb-0">十斤鲜葛出一斤片</p>', '<p class="text-muted small mb-0">十斤鲜葛出一斤片<br><span class="lang-en">10:1 Fresh-to-Sliced</span></p>')
cn = cn.replace('<p class="text-muted small mb-0">国家绿色食品认证</p>', '<p class="text-muted small mb-0">国家绿色食品认证<br><span class="lang-en">Green Food Certified</span></p>')

# About section
cn = cn.replace('<p class="section-subtitle" style="color:rgba(0,0,0,0.4);">ABOUT</p>',
                '<p class="section-subtitle" style="color:rgba(0,0,0,0.4);">ABOUT US</p>')
cn = cn.replace('<h2 class="sec-title">关于我们</h2>',
                '<h2 class="sec-title">关于我们 <small class="lang-en">About Us</small></h2>')
cn = cn.replace('<h4>懂生活，选富葛</h4>',
                '<h4>懂生活，选富葛 <span class="lang-en">Live Well, Choose Fuge</span></h4>')

# Certification section
cn = cn.replace('<h2 class="sec-title">品质认证</h2>',
                '<h2 class="sec-title">品质认证 <small class="lang-en">Certification</small></h2>')
cn = cn.replace('<p class="text-muted mt-2" style="font-size:0.9rem;">好品质，有凭证</p>',
                '<p class="text-muted mt-2" style="font-size:0.9rem;">好品质，有凭证 <span class="lang-en">Quality, Certified</span></p>')

cn = cn.replace('<h5>重庆名牌农产品</h5>', '<h5>重庆名牌农产品<br><span class="lang-en">Chongqing Famous Ag. Product</span></h5>')
cn = cn.replace('<p>重庆市农业农村委员会认定</p>', '<p>重庆市农业农村委员会认定<br><span class="lang-en">Certified by Chongqing Agri. Comm.</span></p>')

cn = cn.replace('<h5>全国特质农品</h5>', '<h5>全国特质农品<br><span class="lang-en">National Special Ag. Product</span></h5>')
cn = cn.replace('<p>国家级特色农产品认证</p>', '<p>国家级特色农产品认证<br><span class="lang-en">National Specialty Product Cert.</span></p>')

cn = cn.replace('<h5>国家绿色食品A级认证</h5>', '<h5>国家绿色食品A级认证<br><span class="lang-en">National Green Food Grade A</span></h5>')
cn = cn.replace('<p>绿色食品最高等级认证</p>', '<p>绿色食品最高等级认证<br><span class="lang-en">Highest Green Food Certification</span></p>')

cn = cn.replace('<h5>全国绿色食品博览会金奖</h5>', '<h5>全国绿色食品博览会金奖<br><span class="lang-en">National Green Food Expo Gold</span></h5>')
cn = cn.replace('<p>行业最高荣誉之一</p>', '<p>行业最高荣誉之一<br><span class="lang-en">Top Industry Honor</span></p>')

cn = cn.replace('<h5>最受欢迎农产品奖</h5>', '<h5>最受欢迎农产品奖<br><span class="lang-en">Most Popular Ag. Product Award</span></h5>')
cn = cn.replace('<p>中国国际农产品博览会</p>', '<p>中国国际农产品博览会<br><span class="lang-en">China Intl. Ag. Products Expo</span></p>')

cn = cn.replace('<h5>最佳火锅伴侣</h5>', '<h5>最佳火锅伴侣<br><span class="lang-en">Best Hotpot Companion</span></h5>')
cn = cn.replace('<p>中国饭店行业协会评选</p>', '<p>中国饭店行业协会评选<br><span class="lang-en">China Hotel Assoc. Award</span></p>')

cn = cn.replace('<h5>重庆市地方标准起草单位</h5>', '<h5>重庆市地方标准起草单位<br><span class="lang-en">Chongqing Local Std. Drafter</span></h5>')
cn = cn.replace('<p>行业标准制定者</p>', '<p>行业标准制定者<br><span class="lang-en">Industry Standard Setter</span></p>')

cn = cn.replace('<h5>标准化种植示范区</h5>', '<h5>标准化种植示范区<br><span class="lang-en">Standardized Demo Farm</span></h5>')
cn = cn.replace('<p>重庆市富葛标准化种植示范区</p>', '<p>重庆市富葛标准化种植示范区<br><span class="lang-en">Fuge Standardized Demo Farm</span></p>')

with open(r"D:\Workspace_Autoclaw\fuge-replica\index.html.bak", "w", encoding="utf-8") as f:
    f.write(cn)

print("Part 3 done - Highlights + About + Certification")
