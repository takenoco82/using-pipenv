FROM python:3.7.0-alpine3.7

WORKDIR /usr/app

# PYTHONPATH に追加
ENV PYTHONPATH=/usr/app:$PYTHONPATH

# ライブラリをインストール
COPY ./Pipfile ./Pipfile.lock ./
RUN pip install --no-cache-dir pipenv
RUN pipenv install --clear

# ソースをコピー
COPY ./setup.cfg ./
COPY src/ ./src

# テスト時のみ、開発環境用のライブラリをインストール
ARG TESTING
RUN if [ -n "$TESTING" ]; then \
    pipenv install --dev --clear; \
fi

CMD [ "pipenv", "run", "start" ]
