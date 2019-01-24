FROM python:3.6.4-alpine3.7

WORKDIR /usr/app

# PYTHONPATH に追加
ENV PYTHONPATH=/usr/app:$PYTHONPATH

# ライブラリをインストール
COPY ./Pipfile ./Pipfile.lock ./
RUN pip install --upgrade pip && pip install --no-cache-dir pipenv
RUN pipenv install --dev --system

# ソースをコピー
COPY ./setup.cfg ./
COPY src/ ./src

# テスト時のみ、開発環境用のライブラリをインストール
ARG TESTING
# RUN if [ -n "$TESTING" ]; then \
#     pipenv install --dev; \
# fi

RUN whoami
# RUN pipenv run pip freeze
CMD [ "python", "src/run.py" ]
