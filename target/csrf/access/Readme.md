
- normal

```sh
curl -X POST -H "Content-Type: application/xml" -d @normal.xml http://127.0.0.1/parse
```

- xxe payload

```sh
curl -X POST -H "Content-Type: application/xml" -d @xxe_payload.xml http://127.0.0.1/parse
```
