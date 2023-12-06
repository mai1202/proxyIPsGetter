# 代理 IP 获取器

本项目可用于从 [https://t.me/cf_push](https://t.me/cf_push) 获取反向代理 Cloudflare 的 IP，并合并成一个文件。

## 部署

需先安装 Python。

### 安装依赖
```
pip install pipenv
pipenv install
```

### 生成 ips.txt
可修改 get.py 中的 `zip_url` 和 `ports` 变量，更改 IP 压缩包的来源及筛选的端口。
```
pipenv run python get.py
```

### 设置定时任务（可选）
在 Linux 终端输入 `crontab -e`，在最后一行添加 `30 7 * * * cd /path/to/your/project && pipenv run python get.py`，保存退出即可。

### 生成链接（可选）
```
pipenv run python net.py
```
可将链接替换掉 [lee1080/CloudflareSpeedTestDDNS](https://github.com/lee1080/CloudflareSpeedTestDDNS/) 中 [./cf_ddns
/cf_ddns_cloudflare.sh](https://github.com/lee1080/CloudflareSpeedTestDDNS/blob/main/cf_ddns/cf_ddns_cloudflare.sh) 的 `https://cf.vbar.fun/zip_baipiao_eu_org/pr_ip.txt`。

```
nohup pipenv run python net.py &
```
使用 nohup 命令，可在后台运行，关闭终端后仍可继续运行。