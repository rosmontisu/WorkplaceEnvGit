git pull origin - merge o
git fetch origin - merge x



>remote: Support for password authentication was removed on August 13, 2021.
>
>remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote->repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
>
>fatal: Authentication failed for 'https://github.com/rosmontisu/WorkplaceEnvGit.git/'

Developer setting -> personal access tokens   
repo -> generate token   

이후로는 평소대로 git config   
단, password 대신 token 입력

```
git config --global user.name 'rosmontisu'     
git config --global user.password 'my-token'
```
