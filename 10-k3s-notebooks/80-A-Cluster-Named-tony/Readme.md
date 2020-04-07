# Notes

create a new cluster named tony

available on api port 8080 and export port 80 to nginx loadbalanced

- try to attache other slaves/workers/agents to this api from a different host

- try to access nginx on port 80 but inside kubernets from my windows desktop

```
k3d create --name stag --api-port 6552 --publish 8082:80 --workers 1

k3d create --name tony --api-port 8080 --publish 80:80 --workers 1
```


# References

https://github.com/tonybutzer/k8s101/blob/master/pkg/k3s/Readme.md
