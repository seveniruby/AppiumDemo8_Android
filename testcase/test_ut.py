

from lxml import etree

def test_xpath():
    import xml.etree.ElementTree as ET

    root = ET.fromstring('<?xml version="1.0"?><node a="1"></node>')

    # Top-level elements
    print(len(root.findall("//node")))

def test_lxml():

    text = '''
    <div>
        <ul>
             <li class="item-0"><a href="link1.html">first item</a></li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-inactive"><a href="link3.html">third item</a></li>
             <li class="item-1"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a>
         </ul>
     </div>
    '''
    html = etree.HTML(text)
    print(html)
    print(len(html.xpath("//ul")))

def test_encode():
    page_source="""
    <?xml version="1.0" encoding="UTF-8"?><hierarchy rotation="0"><android.widget.FrameLayout index="0" text="" class="android.widget.FrameLayout" package="com.xueqiu.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[221,363][1218,2113]" resource-id="" instance="0"><android.widget.FrameLayout index="0" text="" class="android.widget.FrameLayout" package="com.xueqiu.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[221,363][1218,2113]" resource-id="" instance="1"><android.widget.FrameLayout index="0" text="" class="android.widget.FrameLayout" package="com.xueqiu.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[221,363][1218,2113]" resource-id="android:id/content" instance="2"><android.widget.RelativeLayout index="0" text="" class="android.widget.RelativeLayout" package="com.xueqiu.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[221,363][1218,2113]" resource-id="" instance="0"><android.widget.ImageView NAF="true" index="0" text="" class="android.widget.ImageView" package="com.xueqiu.android" content-desc="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[1106,391][1218,503]" resource-id="com.xueqiu.android:id/cancel" instance="0"/><android.widget.FrameLayout index="1" text="" class="android.widget.FrameLayout" package="com.xueqiu.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[221,573][1218,1903]" resource-id="com.xueqiu.android:id/dialog_center" instance="3"><android.widget.TextView index="0" text="好的" class="android.widget.TextView" package="com.xueqiu.android" content-desc="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[299,1637][1139,1763]" resource-id="com.xueqiu.android:id/agree" instance="0"/></android.widget.FrameLayout></android.widget.RelativeLayout></android.widget.FrameLayout></android.widget.FrameLayout></android.widget.FrameLayout></hierarchy>
    """
    print(etree.HTML(page_source))