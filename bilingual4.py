with open(r"D:\Workspace_Autoclaw\fuge-replica\index.html.bak", "r", encoding="utf-8") as f:
    cn = f.read()

# Supply chain
cn = cn.replace('<h2 class="sec-title">全程自控 品质保障</h2>',
                '<h2 class="sec-title">全程自控 品质保障 <small class="lang-en">Full Chain, Total Quality</small></h2>')
cn = cn.replace('<p class="text-muted mt-2" style="font-size:0.9rem;">从育种到加工，全程自有可控</p>',
                '<p class="text-muted mt-2" style="font-size:0.9rem;">从育种到加工，全程自有可控<br><span class="lang-en">From breeding to processing — fully under our control</span></p>')

cn = cn.replace('<h5>自有品种<br>自育种苗</h5>', '<h5>自有品种 · 自育种苗<br><span class="lang-en">Own Variety · Self Bred</span></h5>')
cn = cn.replace('<p>西南大学与富葛实业共同培育鲜食葛根品种，确保品种特性持续稳定性</p>',
                '<p>西南大学与富葛实业共同培育鲜食葛根品种，确保品种特性持续稳定性<br><span class="lang-en">Southwest Univ. &amp; Fuge jointly cultivate fresh kudzu varieties</span></p>')

cn = cn.replace('<h5>自有基地<br>+订单基地</h5>', '<h5>自有基地 + 订单基地<br><span class="lang-en">Own Farms + Contract Farms</span></h5>')
cn = cn.replace('<p>自建标准化种植示范区1000亩，大足区域6000余亩，全国订单基地4万余亩</p>',
                '<p>自建标准化种植示范区1000亩，大足区域6000余亩，全国订单基地4万余亩<br><span class="lang-en">1,000 mu own farms, 6,000+ mu regional, 40,000+ mu nationwide</span></p>')

cn = cn.replace('<h5>自有<br>加工厂</h5>', '<h5>自有加工厂<br><span class="lang-en">Own Processing Facility</span></h5>')
cn = cn.replace('<p>-196℃超低温瞬冻锁鲜技术，15分钟锁住新鲜营养和水分</p>',
                '<p>-196℃超低温瞬冻锁鲜技术，15分钟锁住新鲜营养和水分<br><span class="lang-en">-196&deg;C flash freezing locks in freshness in 15 minutes</span></p>')

cn = cn.replace('<h5>西南大学<br>技术支撑</h5>', '<h5>西南大学技术支撑<br><span class="lang-en">SW Univ. Technical Support</span></h5>')
cn = cn.replace('<p>育种育苗、产品研发、食品加工与质量控制全方位技术支持</p>',
                '<p>育种育苗、产品研发、食品加工与质量控制全方位技术支持<br><span class="lang-en">Breeding, R&amp;D, processing &amp; QC support</span></p>')

# Farming system
cn = cn.replace('<h2 class="sec-title">富葛种植体系</h2>',
                '<h2 class="sec-title">富葛种植体系 <small class="lang-en">Fuge Farming System</small></h2>')

cn = cn.replace('<h4 class="feature-card-title"><a href="#">品种介绍</a></h4>',
                '<h4 class="feature-card-title"><a href="#">品种介绍 <span class="lang-en">Variety Info</span></a></h4>')
cn = cn.replace(
    '<p class="feature-card-text">富葛鲜食葛根，色泽洁白、纤维细腻、绵软化渣、味道清甜。与西南大学共同培育，推动农药"零"使用。</p>',
    '<p class="feature-card-text">富葛鲜食葛根，色泽洁白、纤维细腻、绵软化渣、味道清甜。与西南大学共同培育，推动农药"零"使用。<br><span class="lang-en">Fuge fresh kudzu — pure white, fine fiber, soft texture, naturally sweet. Zero-pesticide farming.</span></p>'
)

cn = cn.replace(
    '<p class="feature-card-text">精选全国优质产区、绿色种植的鲜食葛根富葛为原料，原料产地严格管控。</p>',
    '<p class="feature-card-text">精选全国优质产区、绿色种植的鲜食葛根富葛为原料，原料产地严格管控。<br><span class="lang-en">Premium growing regions with strict raw material quality control.</span></p>'
)

cn = cn.replace(
    '<p class="feature-card-text">实施年份筛选与分级制度，产品获国家绿色食品A级认证，确保品质溯源。</p>',
    '<p class="feature-card-text">实施年份筛选与分级制度，产品获国家绿色食品A级认证，确保品质溯源。<br><span class="lang-en">Year-based grading system. Green Food Grade A certified, fully traceable.</span></p>'
)

cn = cn.replace(
    '<p class="feature-card-text">自建重庆大足示范区1000亩，区域种植6000余亩，全国订单种植基地4万余亩。</p>',
    '<p class="feature-card-text">自建重庆大足示范区1000亩，区域种植6000余亩，全国订单种植基地4万余亩。<br><span class="lang-en">1,000 mu in Dazu, 6,000+ mu regional, 40,000+ mu nationwide.</span></p>'
)

with open(r"D:\Workspace_Autoclaw\fuge-replica\index.html.bak", "w", encoding="utf-8") as f:
    f.write(cn)

print("Part 4 done - Supply chain + Farming system")
