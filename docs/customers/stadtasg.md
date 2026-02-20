# Ersetze französischsprachige HLS Links durch deutsche Versionen

```sql
update resources
  set url = replace(url,'hls-dhs-dss.ch/fr','hls-dhs-dss.ch/de')
  where url like 'https://hls-dhs-dss.ch/fr/articles/%';
```
