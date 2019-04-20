# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:17:03 2019

@author: 28137
"""
import urllib.request

html_str = """
<body id = 'body',class = 'bodyname'>
<div id= 'content' class="ui container">

        <table id  = 'table' class="ui striped  table">
            <tr class ='1' >
                <th>姓名</th>
                <th>性别</th>
                <th>邮箱</th>
                <th>电话</th>
            </tr >
            <tr class ='2'>
                <td><a href="zhangwei">张伟</a></td>
                <td>男</td>
                <td>zhangwei@haoren.com</td>
                <td>12138-111</td>
            </tr>
            <tr class ='3'>
                <td><a href="yifei">一菲</a></td>
                <td>女</td>
                <td>yifei@haoren.com</td>
                <td>12138-112</td>
            </tr>
            <tr class ='4'>
                <td><a href="xiaoxian">小贤</a></td>
                <td>男</td>
                <td>xiaoxian@haoren.com</td>
                <td>12138-113</td>
            </tr>
            <tr class ='5'>
                <td><a href="meijia">美嘉</a></td>
                <td>女</td>
                <td>meijia@haoren.com</td>
                <td>12138-114</td>
            </tr>
            <tr class ='6'>
                <td><a href="xiaobu">小布</a></td>
                <td>男</td>
                <td>xiaobu@hundan.com</td>
                <td>12138-115</td>
            </tr>

        </table>
</div>
<div class = 'two div'> two div </div>
</body>
"""
html_str_2 = """
<body>
<div>

        <table>
            <tr>
                <th>姓名</th>
                <th>性别</th>
                <th>邮箱</th>
                <th>电话</th>
            </tr>
            <tr>
                <td><a href="zhangwei">张伟</a></td>
                <td>男</td>
                <td>zhangwei@haoren.com</td>
                <td>12138-111</td>
            </tr>
            <tr>
                <td><a href="yifei">一菲</a></td>
                <td>女</td>
                <td>yifei@haoren.com</td>
                <td>12138-112</td>
            </tr>
            <tr>
                <td><a href="xiaoxian">小贤</a></td>
                <td>男</td>
                <td>xiaoxian@haoren.com</td>
                <td>12138-113</td>
            </tr>
            <tr>
                <td><a href="meijia">美嘉</a></td>
                <td>女</td>
                <td>meijia@haoren.com</td>
                <td>12138-114</td>
            </tr>
            <tr>
                <td><a href="xiaobu">小布</a></td>
                <td>男</td>
                <td>xiaobu@hundan.com</td>
                <td>12138-115</td>
            </tr>

        </table>
</div>
</body>
"""




from lxml import etree

html = etree.HTML(html_str_2)