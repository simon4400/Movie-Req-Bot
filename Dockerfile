# Credit @VJ_Botz | YouTube: @Tech_VJ | Telegram: @KingVJ01

FROM python:3.10.13-slim-bullseye

# Install system packages
RUN apt update && apt upgrade -y && \
    apt install -y git

# Copy requirements file and install dependencies
COPY requirements.txt /requirements.txt
RUN pip3 install --upgrade pip && pip3 install -r /requirements.txt

# Create app directory
RUN mkdir /VJ-FILTER-BOT
WORKDIR /VJ-FILTER-BOT

# Copy all bot files
COPY . /VJ-FILTER-BOT

# Start the bot
CMD ["python", "bot.py"]
