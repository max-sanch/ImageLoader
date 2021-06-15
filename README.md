# Тестовое задание для idaproject


* [Инструкции](#guides)
    * [Запуск приложения](#launch-app)
        * [На Windows](#Windows)
        * [На Linux](#Linux)

## <a name="guides"></a> Инструкции

### <a name="launch-app"></a>Запуск приложения

Для запуска приложения вам необходимы `Docker`, `docker-compose` и `git`.
<br>
Сервис работает на порту 8080.

#### <a name="Windows"></a>На Windows

1) Установите [git](https://git-scm.com/downloads) и [Docker Desktop](https://www.docker.com/products/docker-desktop)

2) Скачайте проект с GitHub:
   
        git clone https://github.com/max-sanch/ImageLoader.git

3) Перейдите в деректорию проекта и введите:

	    docker-compose up --build

#### <a name="Linux"></a>На Linux

1) Установите [Docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-ru)

2) Установите docker-compose:

        sudo apt install docker-compose

3) При необходимости установите [git](https://git-scm.com/downloads)

4) Скачайте проект с GitHub:
   
        sudo git clone https://github.com/max-sanch/ImageLoader.git
    
5) Перейдите в деректорию проекта и введите:

	    sudo docker-compose up --build