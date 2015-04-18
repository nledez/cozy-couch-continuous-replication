# cozy-couch-continuous-replication
Maintain continuous CouchDB replication

# Install
```bash
git clone https://github.com/nledez/cozy-couch-continuous-replication.git
cd cozy-couch-continuous-replication
virtualenv/bin/pip install -r requirements.txt
```

# Launch it
```bash
virtualenv/bin/python cozy-couch-continuous-replication.py http://127.0.0.1:5984 cozy backup-cozy
```

# Automate it
Launch crontab
```bash
crontab -e
```

Paste crontab after fixing path (I install it in /root/cozy-couch-continuous-replication)
```
*/5 *  *   *   *     /root/cozy-couch-continuous-replication/virtualenv/bin/python /root/cozy-couch-continuous-replication/cozy-couch-continuous-replication.py http://127.0.0.1:5984 cozy backup-cozy > /dev/null 2>&1
```
