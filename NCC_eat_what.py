from datetime import date
import random
from pyecharts import options as opts
from pyecharts.charts import Tree
dishes_noon = ['武大自助', '卤肉饭', '麻辣烫', '武大自助']
dishes_nignt = ['点菜', '铁板饭', '武大自助', '鸡公煲']
noodles = ['炒面', '鱼粉']
random.shuffle(dishes_noon)
random.shuffle(dishes_nignt)
random.shuffle(noodles)
mydate = ['周一', '周二', '周三', '周四', '周五', '周六']
num = 0
data = [{"name": "本周菜单", "children":[]}]
for i in range(0, 6):
    if i == 0 or i == 3:
        data[0]["children"].append({"name": mydate[i],"children": [{"name": "中午:华科士"}, {"name": f"晚上:{noodles[(i+1)%4]}"}]})
        print(f"{mydate[i]}, 华科士 + {noodles[(i+1)%4]}")
    else:
        data[0]["children"].append({"name": mydate[i],"children": [{"name": f"中午:{dishes_noon[num]}"}, {"name": f"晚上:{dishes_nignt[num]}"}]})
        print(f"{mydate[i]}, {dishes_noon[num]} + {dishes_nignt[num]}")
        num += 1
c = (
    Tree()
    .add("", 
        data,
        symbol="roundRect",
        symbol_size=20,
        orient="TB",
        layout="radial",
        collapse_interval=1,
        is_roam=True)
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove")
    )
)
c.render()