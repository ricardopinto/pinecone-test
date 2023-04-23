FROM ubuntu:22.04

RUN apt update && apt install -y build-essential python3 python3-pip git

RUN git clone https://github.com/ggerganov/llama.cpp.git /llama.cpp

WORKDIR /llama.cpp

RUN make && make libllama.so

WORKDIR /app

RUN cp /llama.cpp/libllama.so .

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "qa_docs.py"]
