text = '''
<div class="basicList_info_area__17Xyo">
    <div class="basicList_title__3P9Q7">
        <a href="https://adcr.naver.com/adcr?x=dGuv3Yn2btkv071HS0a2cP///w==kILthdCb5qBu2MuFkWS611uPOTsos2EtlhewKBh0962Tc4MJLa1pPrltk7e65InzI6YTE/AncB5KWFqnGf47ol3FtuJlDDH/HEtxWOv30PjQyh7jLytBlmWPZv85G1RZh0xcFoKRbYLeHpppS73HfkjAcvxePU51yOObls8Yoy3Z7C7yPJKBDVhiHYat7I7qWYWA0EnVOyXB3AQn2hOlIvZtw6snYm1LjBK9h/yZd/RRXmFqqBEiIYYAGAH+d53AH1WSJEbKGCWteZ97fLLsVRJtPKu7utvOffK6lr5rvjtGAVip18WDVQQa7PcjiyPK1EisLeqPA506NIyq8Zzac/qdAoTIWgvpwSmonmPGG9wHf63XpDZDJkpf5bnmva0WZQqIqbrcrm/Bm8kZmyKUFHCFEfxUN6feCBQD8SO/h0U2IFbYZyjFRoZaAVwoYasx/RP4x31sWK3HpWoDOxpHnHugPR+uRTL8LaUi9KBwwEYPHaCHV+PgfQY0OknL/0JMnfSlmpjJWpwONko83stPJlbgFL1Tw97+RIDbfabESogosOuS532zmZSseqDPacIBk58vkEq60UYKSfTrjlN5IQ0JGLtk3QPNCkw3Il0fvNZRkl+xPw3qGhXGVEYoqqg33GWTZfg0zDIPmaxc5zr36e58XwMAxYza8NJCveLaci2R/q8yOd9R6vCzDQTed+qYIhV3lDocopYpLdwDsm136NA==" target="_blank" class="basicList_link__1MaTN" rel="noopener" data-nclick="N=a:lst*B.title,i:17840594493,r:3" title="한성컴퓨터 TFG AX9466">
            한성컴퓨터 TFG AX9466
        </a>
    </div>
</div>
<div class="basicList_price_area__1UXXR">
    <strong class="basicList_price__2r23_">
        <span>
            <span class="price_num__2WUXn">839,000원</span>
        </span>
    </strong>
</div>
<div class="basicList_desc__2-tko">
    <div class="basicList_detail_box__3ta3h">
        <a href="#" class="basicList_detail__27Krk" data-nclick="N=a:lst*B.modelvalue">
            CPU : 코어i5-9400F
        </a>
        <a href="#" class="basicList_detail__27Krk" data-nclick="N=a:lst*B.modelvalue">
            램용량 : 8GB
        </a>
        <a href="#" class="basicList_detail__27Krk" data-nclick="N=a:lst*B.modelvalue">
            SSD용량 : 256GB
        </a>
        <a href="#" class="basicList_detail__27Krk" data-nclick="N=a:lst*B.modelvalue">
            그래픽 : 지포스GTX1660
        </a>
    </div>
</div>
<div class="basicList_etc_box__1Jzg6">
    <span class="basicList_etc__2uAYO">
        등록일 <!-- -->2019.03.
    </span>
</div>
'''
temp = []
t = text.split('\n')
for i in range(len(t)):
    t[i] = t[i].strip()
    if t[i].startswith('<'):
        continue
    temp.append(t[i])
temp.pop(0)
temp.pop(-1)
for j in range(len(temp)):
    temp[j] = temp[j].split(' : ')
temp[0] = ['이름'] + temp[0]
st = temp[-1][0].replace(temp[-1][0][3:12], ' ')
temp[-1][0] = st[:3]
temp[-1].append(st[4:])

d = {}
for (key, value) in temp:
    d[key] = value
print(d)

import csv
with open('result.csv', 'wt', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(temp)
with open('result.csv', 'rt', encoding='utf-8') as f:
    print(f.read())