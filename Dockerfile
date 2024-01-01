FROM ubuntu

ENV LANG C.UTF-8

RUN ln -fs /usr/share/zoneinfo/Asia/Taipei /etc/localtime

RUN apt-get update && apt-get install -y \
    tzdata \
    vim

RUN apt-get install -y ssh

RUN echo 'root:12345678' | chpasswd

RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

RUN sed -i 's/#X11DisplayOffset 10/X11DisplayOffset 10/' /etc/ssh/sshd_config

RUN sed -i 's/#X11UseLocalhost yes/X11UseLocalhost no/' /etc/ssh/sshd_config

RUN mkdir ~/.ssh

RUN touch ~/.ssh/authorized_keys

RUN echo "" >> ~/.ssh/authorized_keys

RUN env >> /etc/environment

CMD /bin/sh -c 'service ssh restart && bash'
# sudo docker build -t default
# sudo docker run -itd -v /home:/home -p 12345:22 --restart=unless-stopped --name default --shm-size 2G --privileged default
