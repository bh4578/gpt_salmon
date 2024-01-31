**1.初始化数据库（demo并未连接数据库，此步跳过）**  
python manage.py makemigrations  
python manage.py migrate  
**2.修改setting配置文件，如static_root路径，allow_host等**  
**3.python manage.py collectstatic 生成静态文件**  
**4.配置nginx服务器，修改nginx.conf**
**5.运行daphne异步服务器 daphne -p 8000 -b 0.0.0.0 your_project_name.asgi:application**  
**6.运行nginx**  
**7.因为gpt需要境外网络访问，因此需要开启代理，这里是clash，如何配置clash可以百度**  
开启clash命令：nohup ./clash -f config.yaml  
  
__不懂的命令可以问chatgpt__  
  
demo示例地址：  
http://110.41.48.238/  

gpt_salmon 文件夹中 存放配置文件
gpt_service 文件夹中存放gpt相关的代码
static 文件夹中存放静态文件，如图片、js文件、css文件等
templates文件夹中存放前端代码
views文件夹中存放后端渲染代码
