## Бот написанный с использованием контроля версий

#### 1) Первое, что делаем это инициализируем git в нашем проекте

`git init` - прописываем данную команду в терминале

#### 2) Добавляем данные о пользователе, который пишет данный проект *(опционально, можно не делать)*

`git config user.name 'username'` - добавляем имя пользователя <br>
`git config user.email 'email'` - добавляем почту пользователя

#### 3) Для проверки внесенных изменений используем команду

`git status` - проверит все файлы которые мы изменяли

#### 4) Добавим файл '.gitignore' чтобы не заливать в гит ненужные и системные папки которые могут появиться от самого pycharm полный код для пайтона можно взять по этой ссылке
`https://github.com/github/gitignore/blob/main/Python.gitignore`
#### 5) По умолчанию гит не следит за нашими файлами, те изменения которые мы будем в них вносить, учитываться не будут, нужно это исправить чтобы git следил за нашими файлами будем использовать следующую команду
`git add 'filename'` - можем указать сами за каким файлом нужно следить <br>
`git add .` - говорим чтобы следил за всеми файлами и папками в нашем проекте

#### После того как выполним данную команду, нужно ещё раз выполнить команду `git status` - чтобы проверить что гит начал следить за нашими файлами

```commandline
Changes to be committed:                      
  (use "git rm --cached <file>..." to unstage)
        new file:   .gitignore
        new file:   README.md
        new file:   main.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md
```

гит теперь следит за тем, что мы делаем с нашими файлами и в каких из них мы вносим изменения

