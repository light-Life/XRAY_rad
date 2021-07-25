import threading
import time
import os

print("""选择要扫描的类型：
1 【rad+xray批量扫描】\033[31mxray: ./xray webscan --listen 127.0.0.1:7777 --html-output bug.html\033[0m
2 【xray被动扫描(配合awvs和bp)】
3 【rad单个爬取，导出为TXT文件】
""")
choice = input('请输入数字:')

localtime = time.localtime(time.time())

time_n = time.strftime("%Y%m%d%H%M%S", time.localtime())

if choice == '1':
  def rad(url):
    exp_rad=("./rad -t {} -http-proxy 127.0.0.1:7777 --no-banner").format(url)
    os.system(exp_rad)

  if __name__ == "__main__":
    urls = open('url.txt')
    for text in urls.readlines():
      data1 = text.strip('\n')
      rad(data1)
elif choice == '2':
  print("\n\033[1;32m[+]在挖了在挖了5555~\033[0m")
  exp = (("./xray webscan --listen 127.0.0.1:7777 --html-output {}.html").format(time_n))
  os.system(exp)

elif choice == '3':
  url = input("url:")
  print("\n\033[1;32m[+]在爬了在爬了5555~\033[0m")
  exp = (("./rad -t {} -text-output {}.txt").format(url,time_n))
  os.system(exp)



else:
  print('\n\033[1;31m[-] 不要做伞兵\033[0m')

