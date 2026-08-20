# deploy-agent

Track releases locally. Record version + sha256, list rollback candidates.

```python
from deploy_agent import ReleaseLog
log = ReleaseLog()
log.record("1.2.0", "abc")
```
