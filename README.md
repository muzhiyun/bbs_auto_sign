# bbs_auto_sign

基于python2.7

终于有空收拾好UA了 
已修改部分代码 邮件以html发送  邮件中注明用户名和当前积分

请搭配定时任务食用 适用其他论坛时请适当调整login_for_cookies.py中的post参数，第一次需运行login_for_cookies.py以获取cookies
可能需要将bbs.py中cookie.txt的路径改为绝对路径

crontab语句 例如 
20 12 * * * /usr/bin/python /etc/bbs/bbs.py

新手作品不够严谨 推荐使用自动签到框架 https://github.com/binux/qiandao

感谢来访
