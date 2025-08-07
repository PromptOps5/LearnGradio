import gradio as gr
import re
import numpy as np
import pandas as pd
class FileUpload:
    def __init__(self) -> None:
        pass

    def chunkedFileContent(self,file):
        content = ""

        with open(file.name, 'r', encoding="utf-8") as f:
            content = f.read()
            clean_text = re.sub(r'\s+'," ",content).strip()
            words = clean_text.split()

            chunks=[]
            for i in range(0, len(words), 10):
                chunkWords = words[i:i+10]
                chunk = " ".join(chunkWords)
                chunks.append(chunk)
        return (chunks)

    def ChunkedFrames(self,file):
        content = ""
        with open(file.name, "r", encoding="utf-8") as fl:
            content = fl.read()
            clean_text = re.sub(r"\s+", " ", content).strip()
            words = clean_text.split()

            chunk_size = 10
            chunks = []
            chunk_count = 0
            for i in range(0, len(words), chunk_size):
                chunk_count += 1
                sentence = words[i:i+chunk_size]
                chunk = " ".join(sentence)
                chunks.append((chunk_count, chunk))

        df = pd.DataFrame(chunks, columns=["Chunk number", "Chunk"])
        return df

    def ChunkedFrameWithSlider(self,file,num):
        content = ""

        with open(file.name,'r', encoding="utf-8") as fl:
            content = fl.read()

            clean_text = re.sub(r'\s+', ' ', content).strip()
            words = clean_text.split()

            chunks=[]
            chunk_count=0

            for i in range(0,len(words),num):
                chunk_count += 1
                sentence = words[i:i+num]
                chunk = " ".join(sentence)
                chunks.append((chunk_count, chunk))
            
            df = pd.DataFrame(chunks, columns=["Chunk number", "Chunk"])
            return df


    def fileUploadInterface(self):
        demo = gr.Interface(
            fn = self.chunkedFileContent,
            inputs = gr.File(label="Upload file"),
            outputs=gr.Textbox(label="Chunk of words")
        )

        return demo
    
    def GetFileDataFrame(self):
        demo = gr.Interface(
            fn = self.ChunkedFrames,
            inputs = gr.File(label="Upload text file"),
            outputs = gr.DataFrame(label="Chunked frames from uploaded file")
        )

        return demo

    def GetFileFrameWithSlider(self):
        demo = gr.Interface(
            fn = self.ChunkedFrameWithSlider,
            inputs = [
                gr.File(label="Upload text file"),
                gr.Slider(minimum=1, maximum=12,step=1,label="Chunk size")
            ],
            outputs = gr.DataFrame(label="Chunk of words")
        )

        return demo