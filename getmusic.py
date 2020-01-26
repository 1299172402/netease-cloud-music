
import requests
from bs4 import BeautifulSoup
import urllib.request
from lxml import html
import os
etree = html.etree


# 欢迎文字
print('\n\n')
print('####### 网易云音乐歌曲下载 #######\n')
# print('Author~~')
print('Jellow 看见我请一定一定叫我学习')
print('Creative By ZhiyuShang With Love\n')
# print('Thanks for being addicted')
print('')
print('使用说明：')
print('')

# 创建文件夹
path = 'E:/music'
print('1.下载文件将存到%s' % path)
if not os.path.exists(path):
    os.makedirs(path)
print('')
print('2.输入云村链接时去掉#/')
print('e.g.')
print('原链接：https://music.163.com/#/album?id=34678769')
print('请输入：https://music.163.com/album?id=34678769\n\n')

# 歌曲下载

headers = {
    'Referer': 'http://music.163.com/',
    'Host': 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
}

play_url = input('请输入云村列表/专辑链接：\n')

s = requests.session()
response = s.get(play_url, headers=headers).content


# 用bs4找出对应的歌曲名称和地址
s = BeautifulSoup(response, 'lxml')
main = s.find('ul', {'class': 'f-hide'})
# print(main.find_all('a'))
lists = []
for music in main.find_all('a'):
    list = []
    # print('{} : {}'.format(music.text, music['href']))
    musicUrl = 'http://music.163.com/song/media/outer/url' + music['href'][5:] + '.mp3'
    musicName = music.text
    list.append(musicName)
    list.append(musicUrl)
    # 歌曲信息加入lists
    lists.append(list)


for i in lists:
    url = i[1]
    name = i[0]
    print('正在下载', name)
    urllib.request.urlretrieve(url, 'E:/music/'+'%s' % name + '.mp3')
    print('下载成功')

print('')
print('')
print('所有歌曲下载完毕')
input('按Enter退出')
