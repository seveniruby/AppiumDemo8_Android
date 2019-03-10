


def test_xpath():
    import xml.etree.ElementTree as ET

    root = ET.fromstring('<?xml version="1.0"?><node a="1"></node>')

    # Top-level elements
    print(len(root.findall("//node")))

def test_lxml():
    from lxml import etree
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