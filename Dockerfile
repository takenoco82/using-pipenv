FROM python:3.7.0-alpine3.7

WORKDIR /usr/app

# PYTHONPATH に追加
ENV PYTHONPATH=/usr/app:$PYTHONPATH

# ライブラリをインストール
COPY ./Pipfile ./Pipfile.lock ./
RUN pip install --no-cache-dir pipenv
RUN pipenv install --clear

# テスト時のみ、開発環境用のライブラリをインストール
ARG TEST
RUN if [ -n "$TEST" ]; then \
    pipenv install --dev --clear; \
fi

# ソースをコピー
COPY src/ ./src

CMD [ "pipenv", "run", "start" ]
