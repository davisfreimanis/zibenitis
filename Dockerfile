FROM python:3.6

RUN apt-get update && apt-get install -y build-essential libpq-dev git sqlite3 locales locales-all curl apt-transport-https

ENV LANG lv_LV.UTF-8
ENV LC_ALL lv_LV.UTF-8
ENV LANGUAGE lv_LV.UTF-8

WORKDIR /app

########
# NODE #
########
ENV NVM_DIR /root/.nvm
ENV NODE_VERSION 9.8.0

# Install nvm with node and npm
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash \
    && . $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default

ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/v$NODE_VERSION/bin:$PATH

########
# YARN #
########
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    && apt-get update && apt-get install -y --no-install-recommends yarn

# Copy and install python requirements
COPY requirements.txt /app
RUN pip3 install -r requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]