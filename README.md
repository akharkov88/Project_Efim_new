git remote remove origin - удалить ветку

git remote --verbose   - посмотреть

git branch  name - создание веток

git checkout name - переключиться на ветку

git checkout - b name - создать и переключиться на ветку

git remote add origin https://github.com/akharkov88/test.git

git remote set-url master https://github.com/akharkov88/ProjectEfim.git

git status

git push --set-upstream master master

git push --set-upstream master testing

git pull - обновить данные

git config --global alias.add-commit '!git add -A && git commit'

git add-commit -m 'My commit message'

git clone -b testing  https://github.com/akharkov88/ProjectEfim

uvicorn main:app

uvicorn main:app --reload - обновление при изменениях

--------------------------------------------------
module 'pkgutil' has no attribute 'ImpImporter'. Did you mean: 'zipimporter'
-------------------------------------------------


В терминале Linux / macOS:

python -m ensurepip --upgrade
В Windows:

py -m ensurepip --upgrade
тогда :

pip install --upgrade setuptools


-------------------------------------------------