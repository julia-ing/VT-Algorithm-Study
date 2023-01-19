import time 
from sqlalchemy import Table, text

item = {
        "category": "isats",
        "origin": "localhost",
        "identifier": "cgroup_max_memory",
        "type": "event",
        "created": int(time.time() * 1000),
        "is_update": True,
        "primary_key": "cgroup_path",
        "max_usage": 2,
        "cgroup_path": "docker/cid",
    }

pkey_str = f"\"{item['primary_key'].upper()}\""
pvalue_str = f":{item['primary_key']}"
print(pkey_str)
print(pvalue_str)
print(text(f"WHERE {pkey_str}={pvalue_str}") # items에서 PK하나를 꺼내서 
)


"CATEGORY", "ORIGIN", "IDENTIFIER", "TYPE", "CREATED", "IS_UPDATE", "PRIMARY_KEY", "MAX_USAGE", "CGROUP_PATH"
:category, :origin, :identifier, :type, :created, :is_update, :primary_key, :max_usage, :cgroup_path


UPSERT items_isats_cgroup_max_memory 
VALUES (:category, :origin, :identifier, :type, :created, :is_update, :primary_key, :max_usage, :cgroup_path) 
WHERE CGROUP_PATH=:cgroup_path