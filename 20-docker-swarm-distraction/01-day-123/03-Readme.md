# Swarm Addendum


# Reference
https://docs.docker.com/engine/reference/commandline/swarm_init/


1. push pem file
	- bscp ~/.ssh/CHS-LSDSDPAS-butzer.pem master

2. alias sshx='ssh -i /home/ubuntu//CHS-LSDSDPAS-butzer.pem '

3. add these hosts to /etc/hosts

```
10.12.68.238 master
10.12.69.193 ship0
10.12.68.62 ship1
```

4. Mess with Makefile
